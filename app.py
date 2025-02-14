from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the AI model once (Fast Processing)
print("Loading AI model... This may take a few seconds.")
nlp = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")
print("AI model loaded successfully!")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        user_input = request.form['text']
        result = analyze_text(user_input)  # AI analysis
    
    return render_template("index.html", result=result)

def analyze_text(text):
    """Use the AI model to detect misinformation"""
    labels = ["true", "false", "misleading"]
    result = nlp(text, candidate_labels=labels)
    return f"Prediction: {result['labels'][0]} (Confidence: {round(result['scores'][0] * 100, 2)}%)"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
