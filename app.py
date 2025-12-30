from flask import Flask, request, jsonify, render_template
import json
import random

app = Flask(__name__)

# Comprehensive health knowledge base
health_data = {
    # Symptoms and remedies
    "fever": {
        "response": "For fever, I recommend: Rest well, stay hydrated with plenty of fluids, monitor your temperature regularly. If fever persists above 102°F (39°C) for more than 3 days or is accompanied by severe symptoms, please consult a doctor immediately.",
        "tips": ["Drink water frequently", "Take lukewarm baths", "Wear light clothing", "Rest adequately"]
    },
    "cold": {
        "response": "For common cold: Stay hydrated, get plenty of rest, use steam inhalation for congestion. Avoid unnecessary antibiotics unless prescribed by a doctor. Cold typically resolves in 7-10 days.",
        "tips": ["Warm liquids help", "Vitamin C rich foods", "Adequate sleep", "Wash hands frequently"]
    },
    "cough": {
        "response": "For cough: Stay hydrated, try honey and warm water, avoid irritants like smoke. If cough persists for more than 2 weeks or includes blood, see a doctor immediately.",
        "tips": ["Honey soothes throat", "Stay hydrated", "Use a humidifier", "Avoid dusty areas"]
    },
    "headache": {
        "response": "For headache: Rest in a quiet, dark room, stay hydrated, apply cold compress to forehead. If severe or recurring, consult a healthcare provider.",
        "tips": ["Stay hydrated", "Reduce screen time", "Practice relaxation", "Regular sleep schedule"]
    },
    "body pain": {
        "response": "Body pain may be due to overexertion, dehydration, or viral infection. Rest, stay hydrated, and gentle stretching can help. If pain persists or worsens, consult a doctor.",
        "tips": ["Gentle stretching", "Warm compress", "Adequate rest", "Stay hydrated"]
    },
    "stomach ache": {
        "response": "For stomach ache: Eat light, easily digestible foods, stay hydrated, avoid spicy or oily foods. If accompanied by severe pain, vomiting, or fever, seek medical attention.",
        "tips": ["Light meals", "Ginger tea", "Avoid heavy foods", "Stay hydrated"]
    },
    
    # Nutrition
    "nutrition": {
        "response": "A balanced diet includes: fruits, vegetables, whole grains, lean proteins, and healthy fats. Aim for 5 servings of fruits and vegetables daily, stay hydrated with 8-10 glasses of water.",
        "tips": ["Colorful plate", "Whole grains", "Lean proteins", "Healthy fats"]
    },
    "diet": {
        "response": "Healthy eating habits: Eat regular meals, include variety in your diet, limit processed foods and added sugars, control portion sizes, and stay physically active.",
        "tips": ["Regular meal times", "Portion control", "Limit sugar", "Cook at home"]
    },
    "vitamins": {
        "response": "Essential vitamins: Vitamin C (citrus fruits), Vitamin D (sunlight, fish), Vitamin A (carrots, leafy greens), B vitamins (whole grains, eggs). A balanced diet usually provides adequate vitamins.",
        "tips": ["Eat variety", "Fresh fruits", "Leafy greens", "Sunlight exposure"]
    },
    
    # Exercise and fitness
    "exercise": {
        "response": "Regular exercise is vital for health! Aim for 150 minutes of moderate activity weekly. This can include walking, jogging, cycling, or swimming. Start slow and gradually increase intensity.",
        "tips": ["30 min daily walk", "Stretching exercises", "Stay consistent", "Warm up properly"]
    },
    "fitness": {
        "response": "Fitness tips: Combine cardio, strength training, and flexibility exercises. Stay active throughout the day, take stairs, walk during breaks. Consistency is key!",
        "tips": ["Mix activities", "Stay active daily", "Set realistic goals", "Track progress"]
    },
    
    # Mental health
    "stress": {
        "response": "Managing stress: Practice deep breathing, meditation, regular exercise, adequate sleep, and connect with loved ones. If stress feels overwhelming, consider talking to a counselor.",
        "tips": ["Deep breathing", "Meditation", "Regular exercise", "Talk to someone"]
    },
    "anxiety": {
        "response": "For anxiety: Practice mindfulness, maintain regular sleep schedule, exercise regularly, limit caffeine. Professional help is available and effective if anxiety persists.",
        "tips": ["Mindfulness practice", "Regular routine", "Limit caffeine", "Seek support"]
    },
    "sleep": {
        "response": "Good sleep hygiene: Maintain consistent sleep schedule, create dark and cool bedroom, avoid screens 1 hour before bed, limit caffeine after 2 PM. Adults need 7-9 hours of sleep.",
        "tips": ["Consistent schedule", "Dark room", "No screens before bed", "7-9 hours nightly"]
    },
    
    # First aid
    "cut": {
        "response": "For minor cuts: Clean with water, apply pressure to stop bleeding, use antiseptic, cover with clean bandage. For deep cuts, seek medical attention immediately.",
        "tips": ["Clean thoroughly", "Apply pressure", "Use antiseptic", "Keep covered"]
    },
    "burn": {
        "response": "For minor burns: Cool with running water for 10-20 minutes, don't apply ice directly, cover with sterile gauze. For severe burns, seek emergency medical care.",
        "tips": ["Cool with water", "Don't use ice", "Cover gently", "Avoid ointments"]
    },
}

vaccination_schedule = {
    "child": "Recommended vaccinations for children (0-5 years): BCG, OPV/IPV, Hepatitis B, DPT, Hib, Rotavirus, PCV, MMR, Varicella. Follow your pediatrician's schedule for timely immunization.",
    "adult": "Adult vaccinations: Annual flu vaccine, Tetanus booster every 10 years, Hepatitis B, HPV (for eligible age groups), Pneumococcal vaccine for 65+. Consult your doctor for personalized recommendations.",
    "elderly": "For elderly (65+): Annual flu vaccine, Pneumococcal vaccine, Shingles vaccine, Tetanus booster. These are important for preventing serious illnesses."
}

# Health tips
health_tips = [
    "💧 Drink at least 8 glasses of water daily to stay hydrated!",
    "🚶 Take a 30-minute walk daily for better cardiovascular health.",
    "🥗 Include 5 servings of fruits and vegetables in your daily diet.",
    "😴 Get 7-9 hours of quality sleep every night.",
    "🧘 Practice 10 minutes of meditation or deep breathing daily.",
    "🤸 Stretch regularly to improve flexibility and reduce injury risk.",
    "🧼 Wash hands frequently with soap and water for 20 seconds.",
    "☀️ Get some sunlight daily for Vitamin D.",
    "🎵 Take breaks from screen time to reduce eye strain.",
    "💚 Regular health check-ups can detect issues early!"
]

# Quick suggestions for UI
quick_suggestions = [
    "What to do for fever?",
    "Healthy diet tips",
    "Exercise recommendations",
    "Stress management",
    "Child vaccination schedule",
    "Sleep better",
]

user_data = []  # In-memory user data storage


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    text = data.get('text', '').lower()
    language = data.get('language', 'english')
    
    # Save user message
    user_data.append({"text": text, "language": language})
    
    # Greeting handling
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good evening', 'namaste']
    if any(greeting in text for greeting in greetings):
        tip = random.choice(health_tips)
        return jsonify({
            "response": f"Hello! 👋 I'm your HealthMate assistant. I can help you with health information, symptoms, nutrition, exercise, and more. How can I assist you today?\n\n{tip}"
        })
    
    # Help command
    if 'help' in text:
        return jsonify({
            "response": "I can help you with:\n• Common symptoms and remedies\n• Nutrition and diet advice\n• Exercise and fitness tips\n• Mental health support\n• Vaccination schedules\n• First aid guidance\n\nJust ask me anything about your health!"
        })
    
    # Check health data
    for keyword, data_obj in health_data.items():
        if keyword in text:
            response = data_obj["response"]
            if "tips" in data_obj:
                tips_text = "\n\n📝 Quick Tips:\n" + "\n".join([f"• {tip}" for tip in data_obj["tips"]])
                response += tips_text
            return jsonify({"response": response})
    
    # Vaccination query
    if "vaccination" in text or "vaccine" in text or "immunization" in text or "टीकाकरण" in text:
        if "child" in text or "baby" in text or "infant" in text or "बच्चे" in text:
            return jsonify({"response": vaccination_schedule["child"]})
        elif "adult" in text or "वयस्क" in text:
            return jsonify({"response": vaccination_schedule["adult"]})
        elif "elderly" in text or "senior" in text or "old" in text:
            return jsonify({"response": vaccination_schedule["elderly"]})
        else:
            return jsonify({
                "response": "I can help with vaccination information! Please specify:\n• Child vaccination\n• Adult vaccination\n• Elderly vaccination"
            })
    
    # Emergency keywords
    emergency_keywords = ['emergency', 'urgent', 'severe pain', 'chest pain', 'difficulty breathing', 'unconscious']
    if any(keyword in text for keyword in emergency_keywords):
        return jsonify({
            "response": "⚠️ This seems like an emergency! Please call emergency services immediately or visit the nearest hospital. In India, call 102 (Ambulance) or 112 (Emergency)."
        })
    
    # Random health tip
    if 'tip' in text or 'tips' in text:
        return jsonify({"response": random.choice(health_tips)})
    
    # Default response
    return jsonify({
        "response": "I'm not sure about that. I can help with symptoms, nutrition, exercise, mental health, vaccinations, and first aid. Try asking 'help' to see what I can do, or click on the quick suggestions below!"
    })


@app.route('/api/suggestions', methods=['GET'])
def suggestions():
    return jsonify({"suggestions": quick_suggestions})


@app.route('/api/health-tip', methods=['GET'])
def health_tip():
    return jsonify({"tip": random.choice(health_tips)})


@app.route('/api/history', methods=['GET'])
def history():
    return jsonify({"history": user_data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
