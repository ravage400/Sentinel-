from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        user_input = request.form['text']
        result = analyze_text(user_input)  # Basic keyword detection
    
    return render_template("index.html", result=result)

def analyze_text(text):
    """Basic keyword-based misinformation detection"""
    misinformation_keywords = ["fake news", "hoax", "conspiracy", "misleading", "false claims"]
    
    for keyword in misinformation_keywords:
        if keyword.lower() in text.lower():
            return "⚠️ Potential misinformation detected!"
    
    return "✅ No misinformation detected."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
