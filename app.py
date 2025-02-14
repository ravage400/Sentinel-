from flask import Flask, render_template
import os

# Initialize Flask app
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template("index.html")  # Loads index.html from the templates folder

# Ensure the app runs on the correct port for Heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from Heroku or default to 5000
    app.run(host="0.0.0.0", port=port)
