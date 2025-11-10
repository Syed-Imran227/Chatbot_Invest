# 💰 AI Finance Advisor (Django + Gemini)

An intelligent finance advisor web app built with **Django**, powered by **Google Gemini** models, and backed by **SQLite**. This application helps users get personalized investment advice based on their financial profile.

---

## 🚀 Features

- 👤 User authentication and profile management
- 📊 Financial profile creation with investment goals
- 🧠 Generates tailored investment advice using Google Gemini
- 💬 Interactive chat with AI financial advisor
- 📝 Tracks investment advice history
- 🎨 Clean, modern UI with responsive design

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (Django ORM)
- **AI:** Google Gemini (Generative AI via API)
- **Frontend:** Django Templates + Bootstrap
- **Sanitizing & Formatting:** `markdown` and `bleach`

---

## ⚙️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/finance-advisor.git
cd finance-advisor
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

### 6. Configure Gemini API Access

Create a Google Generative AI API key and store it securely. For local development you can export the key before running the server:

```bash
export GEMINI_API_KEY="your-google-generative-ai-key"
export GEMINI_MODEL="models/gemini-1.5-flash"  # optional override
```

On Windows PowerShell:

```powershell
$Env:GEMINI_API_KEY = "your-google-generative-ai-key"
$Env:GEMINI_MODEL = "models/gemini-1.5-flash"
```

---

## 📝 Usage

1. Register a new account or log in
2. Create your financial profile with investment goals
3. Get personalized investment advice
4. Chat with the AI advisor for more detailed guidance

---

## 🔒 Environment Variables

Create a `.env` file in the project root with the following variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
GEMINI_API_KEY=your_google_generative_ai_key
GEMINI_MODEL=models/gemini-1.5-flash
```
