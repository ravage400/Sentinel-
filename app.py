from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    chart_data = {"positive": 0, "negative": 0, "neutral": 0}

    if request.method == 'POST':
        user_input = request.form['text']
        result = analyze_text(user_input)

        # Generate random chart data for now
        chart_data = {
            "positive": random.randint(20, 50),
            "negative": random.randint(10, 40),
            "neutral": random.randint(10, 40)
        }

    return render_template("index.html", result=result, chart_data=chart_data)

# Simple function to detect misinformation keywords
def analyze_text(text):
    misinformation_keywords = ["fake news", "hoax", "conspiracy", "misleading", "false claims"]
    for keyword in misinformation_keywords:
        if keyword.lower() in text.lower():
            return "⚠️ Potential misinformation detected!"
    return "✅ No misinformation detected."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
