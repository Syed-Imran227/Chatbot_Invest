# 💰 Chatbot Invest - AI Finance Advisor

Welcome to **Chatbot Invest**, an intelligent finance advisor web application built with **Django** and powered by **Google Gemini** generative AI. This application is designed to help users get personalized investment advice tailored to their financial profiles and goals.

## 🚀 Features

- **👤 User Authentication:** Secure registration and login functionality.
- **📊 Financial Profiles:** Users can create and manage their financial profiles and set specific investment goals.
- **🧠 Generative AI Advice:** Leverages Google Gemini to generate highly tailored, actionable investment strategies.
- **💬 Interactive Chat:** An interactive AI financial advisor for real-time guidance.
- **📝 Advice History:** Keeps track of previous investment advice for easy reference.
- **🎨 Modern UI:** A clean, responsive design using Django Templates and Bootstrap.

## 🛠️ Technology Stack

- **Backend:** Python, Django
- **Database:** SQLite (local development), PostgreSQL (production/Render)
- **AI Integration:** Google Gemini API
- **Frontend:** HTML/CSS, Bootstrap
- **Deployment:** Render (configured with WhiteNoise for static files and Gunicorn as the WSGI HTTP server)

## 📁 Project Structure

- `finance_advisor/` - The main Django project directory containing all the application logic, settings, and templates.
- `render.yaml` & `Procfile` - Configuration files for deployment on Render.
- `DEPLOYMENT_CHECKLIST.md` & `RENDER_DEPLOYMENT_GUIDE.md` - Documentation and guides for deploying the application.

## ⚙️ Quick Start (Local Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Chatbot_Invest.git
   cd Chatbot_Invest/finance_advisor
   ```

2. **Set up virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the `finance_advisor` directory:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   GEMINI_API_KEY=your_google_generative_ai_key
   GEMINI_MODEL=models/gemini-1.5-flash
   ```

4. **Run Migrations & Start Server:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

For detailed deployment instructions on Render, please refer to the [`RENDER_DEPLOYMENT_GUIDE.md`](./RENDER_DEPLOYMENT_GUIDE.md).
