from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.core.files.storage import FileSystemStorage
import zlib
from google import genai
from dotenv import load_dotenv
import os


# ===============================
# GEMINI CONFIGURATION (NEW SDK)
# ===============================

load_dotenv()

client = genai.Client(
    api_key="AIzaSyCkUMs6TQa_qUGaNiQjKeNFzdRo43STuL4" 
)


# ===============================
# BASIC PAGES
# ===============================

def base(request):
    return render(request, 'base.html')


def UserHome(request):
    return render(request, 'users/UserHome.html')


def logout_view(request):
    request.session.flush()
    return redirect('base')


# ===============================
# REGISTRATION
# ===============================

def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been successfully registered')
            return render(request, 'UserRegistration.html')
        else:
            messages.error(request, 'Email or Mobile Already Exists')
    else:
        form = UserRegistrationForm()

    return render(request, 'UserRegistration.html', {'form': form})


# ===============================
# LOGIN
# ===============================

def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('password')

        try:
            user = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)

            if user.status == "activated":
                request.session['id'] = user.id
                request.session['loggeduser'] = user.name
                return redirect('UserHome')
            else:
                messages.error(request, 'Your account is not activated.')

        except UserRegistrationModel.DoesNotExist:
            messages.error(request, 'Invalid Login ID or Password')

    return render(request, 'UserLogin.html')


# ===============================
# PLANTUML ENCODING
# ===============================

def plantuml_encode(text):
    deflate = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15)
    compressed = deflate.compress(text.encode('utf-8')) + deflate.flush()
    return encode_plantuml_base64(compressed)


def encode_plantuml_base64(data):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    result = ""
    i = 0

    while i < len(data):
        b1 = data[i]
        b2 = data[i + 1] if i + 1 < len(data) else 0
        b3 = data[i + 2] if i + 2 < len(data) else 0
        i += 3

        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F

        result += (
            alphabet[c1 & 0x3F] +
            alphabet[c2 & 0x3F] +
            alphabet[c3 & 0x3F] +
            alphabet[c4 & 0x3F]
        )

    return result


# ===============================
# MAIN GENERATOR (CODE <-> DIAGRAM)
# ===============================

import base64
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

def generator_view(request):
    ai_response = ""
    diagram_url = ""
    mode = request.POST.get("mode", "code_to_diagram")
    language = request.POST.get("language", "Python")

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        uploaded_file = request.FILES.get("code_file")

        try:
            # =============================
            # HANDLE FILE UPLOAD
            # =============================
            encoded_image = None
            mime_type = None

            if uploaded_file:
                fs = FileSystemStorage()
                filename = fs.save(uploaded_file.name, uploaded_file)
                file_path = fs.path(filename)

                # If image uploaded
                if uploaded_file.content_type.startswith("image"):
                    with open(file_path, "rb") as f:
                        image_bytes = f.read()

                    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
                    mime_type = uploaded_file.content_type

                # If text file uploaded
                else:
                    with open(file_path, "r", encoding="utf-8") as f:
                        user_input += "\n" + f.read()

            # =============================
            # CODE → DIAGRAM
            # =============================
            if mode == "code_to_diagram":

                prompt = f"""
Convert the following {language} code into a PlantUML diagram.
Return ONLY valid PlantUML code between @startuml and @enduml.

{user_input}
"""

                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt,
                )

                plantuml_code = response.text.strip()

                if plantuml_code.startswith("@startuml"):
                    encoded = plantuml_encode(plantuml_code)
                    diagram_url = f"https://www.plantuml.com/plantuml/png/{encoded}"
                else:
                    ai_response = plantuml_code

            # =============================
            # DIAGRAM → CODE
            # =============================
            else:

                # If image diagram uploaded
                if encoded_image:

                    response = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=[
                            {
                                "role": "user",
                                "parts": [
                                    {
                                        "text": f"Convert this diagram into {language} code. Return only clean code without explanation."
                                    },
                                    {
                                        "inline_data": {
                                            "mime_type": mime_type,
                                            "data": encoded_image
                                        }
                                    }
                                ]
                            }
                        ],
                    )

                    ai_response = response.text.strip()

                # If PlantUML text pasted
                else:

                    prompt = f"""
Convert the following PlantUML diagram into {language} code.
Return only clean code without explanation.

{user_input}
"""

                    response = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=prompt,
                    )

                    ai_response = response.text.strip()

        except Exception as e:
            ai_response = f"Error: {str(e)}"

    return render(request, "users/generator.html", {
        "ai_response": ai_response,
        "diagram_url": diagram_url,
        "mode": mode,
        "language": language,
    })

