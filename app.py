from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Sample FAQs and data
faq_data = {
    "fever": "For fever: rest, fluids, and monitoring temperature are recommended. Consult a doctor if it persists.",
    "cold": "For cold: stay hydrated, rest, and avoid unnecessary medication."
}

symptom_data = {
    "fever": "You might have a viral infection. Stay hydrated and consult a doctor if needed.",
    "body pain": "This may be due to overexertion or infection. Rest and fluids are helpful."
}

vaccination_schedule = {
    "child": "BCG, OPV, Hepatitis B, DPT, MMR are recommended for children aged 0-5.",
    "adult": "Annual flu vaccine, Tetanus booster, and others are recommended."
}

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
    
    # Check FAQs
    for key in faq_data:
        if key in text:
            return jsonify({"response": faq_data[key]})
    
    # Check symptoms
    for key in symptom_data:
        if key in text:
            return jsonify({"response": symptom_data[key]})
    
    # Vaccination query
    if "vaccination" in text or "टीकाकरण" in text:
        if "child" in text or "बच्चे" in text:
            return jsonify({"response": vaccination_schedule["child"]})
        elif "adult" in text or "वयस्क" in text:
            return jsonify({"response": vaccination_schedule["adult"]})
        else:
            return jsonify({"response": "Please specify age group: child or adult."})
    
    return jsonify({"response": "I'm sorry, I couldn't find relevant information. Please try again."})


@app.route('/api/history', methods=['GET'])
def history():
    return jsonify({"history": user_data})


if __name__ == "__main__":
    app.run(debug=True)
