# gen-ai-for-code-to-diagram-diagram-to-code
# 🚀 Generative AI for Diagrams as Code and Code as Diagrams

## 📌 Project Overview

This project is a web-based application that leverages Generative AI to convert:

* 💻 **Code → UML Diagrams (PlantUML)**
* 📊 **Diagrams → Source Code**

It also provides **AI-powered improvement tips** to enhance code quality and diagram structure.

Built using **Django (Backend)** and **Google Gemini API**, this system helps developers, students, and professionals visualize and understand code more effectively.

---

## 🎯 Key Features

* 🔄 Convert **Code to Diagram** (PlantUML)
* 🔁 Convert **Diagram to Code**
* 📁 Upload code files or diagram images (PNG/JPG)
* 🤖 AI-generated **Improvement Tips**
* 🔐 User Authentication System (Login/Register)
* 🧑‍💼 Admin Dashboard
* 🌐 Clean UI for interaction

---

## 🛠️ Tech Stack

| Layer        | Technology Used      |
| ------------ | -------------------- |
| Frontend     | HTML, CSS, Bootstrap |
| Backend      | Django (Python)      |
| Database     | MySQL                |
| AI Model     | Google Gemini API    |
| Diagram Tool | PlantUML             |

---

## 📂 Project Structure

```
project/
│
├── users/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│
├── admins/
│   ├── views.py
│
├── templates/
│   ├── users/
│   ├── admins/
│
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd your-project-folder
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in root:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5️⃣ Database Setup (MySQL)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'codetodiagram',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 6️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🔑 API Configuration

This project uses **Google Gemini API**.

In `views.py`:

```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
```

---

## 🔄 How It Works

### 🧩 Code → Diagram

1. User inputs code or uploads file
2. AI converts code to PlantUML
3. Diagram is generated using PlantUML server
4. AI provides improvement tips

---

### 🧩 Diagram → Code

1. User uploads diagram (image or text)
2. AI processes image/text
3. Converts into structured code
4. Provides optimization tips

---
## 📸 Outputs

<img width="696" height="370" alt="Screenshot 2026-03-22 231513" src="https://github.com/user-attachments/assets/728d1259-158b-43ff-93c6-af6a32bde71b" />

<img width="744" height="419" alt="Screenshot 2026-03-22 231534" src="https://github.com/user-attachments/assets/f748114d-e70e-4dc6-94f6-6ca4c2a50d5c" />
<img width="739" height="467" alt="Screenshot 2026-03-22 231546" src="https://github.com/user-attachments/assets/235110c8-9e4b-4540-9c15-07b531b9d5a5" />


<img width="763" height="428" alt="Screenshot 2026-03-22 231554" src="https://github.com/user-attachments/assets/039ae49d-cf28-4c0c-80b3-7189e68be639" />


<img width="770" height="472" alt="Screenshot 2026-03-22 231604" src="https://github.com/user-attachments/assets/84552e05-c610-438f-9d5d-12525f63e470" />

<img width="835" height="478" alt="Screenshot 2026-03-22 231611" src="https://github.com/user-attachments/assets/4adaeeff-c0e5-44a0-bfd5-ebd26d36bc55" />
<img width="855" height="474" alt="Screenshot 2026-03-22 231619" src="https://github.com/user-attachments/assets/19a94b61-9fd3-4ecf-a917-2a787c8207bf" />
<img width="806" height="446" alt="Screenshot 2026-03-22 231625" src="https://github.com/user-attachments/assets/a19f224a-de65-47d6-a080-896765f58c66" />

## 📸 Features Explained

### 📁 File Upload Support

* `.py`, `.txt` for code
* `.png`, `.jpg` for diagrams

### 🤖 AI Tips

* Code quality suggestions
* Readability improvements
* Best practices

---

## ⚠️ Common Issues & Fixes

### ❌ UTF-8 Decode Error

```
'utf-8' codec can't decode byte 0x89
```

✔ Fix: Open image files in binary mode (`rb`)

---

### ❌ NoReverseMatch Error

✔ Fix: Ensure URL name matches in `urls.py`

---

### ❌ django_session Table Missing

✔ Fix:

```bash
python manage.py migrate
```

---

### ❌ API Errors

| Error               | Solution                 |
| ------------------- | ------------------------ |
| 404 Model Not Found | Use correct Gemini model |
| 429 Quota Exceeded  | Enable billing           |
| 503 Server Busy     | Retry or switch model    |

---

## 🔒 Security Notes

* Do NOT expose API keys in public repositories
* Use `.env` for sensitive data
* Enable Django security settings in production

---

## 🚀 Future Enhancements

* 🌍 Deploy on cloud (AWS / Azure)
* 📊 Advanced UML types (Sequence, Class diagrams)
* 🧠 Local AI model support (offline)
* 🎤 Voice input for code generation
* 📱 Responsive mobile UI

---

## 👨‍💻 Author

**Saikumar Bommali**

* 🎓 B.Tech Project
* 💡 Focus: Generative AI + Software Engineering

---

## 📜 License

This project is for educational purposes.

---

## ⭐ Acknowledgements

* Google Gemini API
* Django Framework
* PlantUML

---

## 💬 Final Note

This project demonstrates the power of **Generative AI in software visualization**, making development faster, smarter, and more intuitive.

---
