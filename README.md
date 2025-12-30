# 🏥 HealthMate - Your Personal Health Assistant

A beautiful, modern health chatbot with glassmorphism UI design that provides personalized health information, wellness advice, and support for common health queries.

![HealthMate Preview](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)

## ✨ Features

### 🎨 Beautiful Modern UI
- **Glassmorphism Design** with stunning gradient backgrounds
- **Smooth Animations** for messages, typing indicators, and interactions
- **Responsive Layout** - works perfectly on mobile, tablet, and desktop
- **Health-Themed Color Palette** with soothing teal and purple gradients
- **Message Bubbles** with distinct styling for user and bot
- **Typing Indicators** for natural conversation flow

### 🏥 Comprehensive Health Information
- **Symptoms & Remedies** - Fever, cold, cough, headache, body pain, stomach ache, etc.
- **Nutrition Advice** - Healthy diet tips, vitamins, and balanced nutrition
- **Exercise & Fitness** - Workout recommendations and fitness tips
- **Mental Health Support** - Stress management, anxiety relief, and sleep tips
- **First Aid Guidance** - Basic first aid for cuts, burns, and minor injuries
- **Vaccination Schedules** - For children, adults, and elderly

### 🚀 Interactive Features
- **Quick Suggestion Chips** - One-click access to common health queries
- **Voice Input** - Speak your queries using voice recognition
- **Multi-language Support** - English and Hindi
- **Welcome Screen** - Friendly greeting with health tips
- **Real-time Responses** - Instant health advice

## 📸 Screenshots

*(Add screenshots here after deployment)*

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
- **Fonts**: Google Fonts (Inter)
- **Design**: Modern UI/UX with accessibility features

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jyoti429/healthmate-chatbot.git
   cd healthmate-chatbot
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🌐 Deployment

### Deploy to Render (Recommended - Free)

1. **Create a free account** at [Render.com](https://render.com)

2. **Create a new Web Service**
   - Connect your GitHub repository
   - Choose Python environment
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

3. **Add gunicorn to requirements.txt**
   ```bash
   echo "gunicorn==21.2.0" >> requirements.txt
   git add requirements.txt
   git commit -m "Add gunicorn for deployment"
   git push
   ```

### Deploy to Railway

1. **Create account** at [Railway.app](https://railway.app)
2. **New Project** → **Deploy from GitHub**
3. **Select repository** and deploy
4. Railway will auto-detect Flask and deploy

### Deploy to PythonAnywhere

1. **Create account** at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. **Upload code** via Git or Files
3. **Set up web app** with Flask
4. **Configure WSGI file** to point to your app

## 📱 Usage

### Ask Health Questions
Simply type or speak your health-related questions:
- "What to do for fever?"
- "Healthy diet tips"
- "Exercise recommendations"
- "How to manage stress?"

### Use Quick Suggestions
Click on the suggestion chips below the chat to quickly ask common questions.

### Voice Input
Click the microphone button 🎤 to use voice input (requires microphone permission).

### Switch Language
Use the language selector in the header to switch between English and Hindi.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

**HealthMate is for informational purposes only.** This chatbot provides general health information and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

In case of **medical emergencies**, call your local emergency number immediately:
- India: 102 (Ambulance) or 112 (Emergency)
- US: 911
- UK: 999

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

Created with ❤️ by [Jyoti429](https://github.com/Jyoti429)

## 🙏 Acknowledgments

- Flask framework for the backend
- Google Fonts for beautiful typography
- Modern web design inspiration from healthcare applications

---

**⭐ Star this repository if you find it helpful!**
