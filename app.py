import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Set this in Render's environment variables once you have the GHL calendar link.
CALENDAR_URL = os.environ.get("CALENDAR_URL", "")
CONTACT_EMAIL = "info@advisorautomationsgroup.com"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book")
def book():
    """Every Book an Intro Call button routes here.
    If the GHL calendar link is set, send them straight to it.
    If not, fall back to a simple contact page so no click is ever wasted."""
    if CALENDAR_URL:
        return redirect(CALENDAR_URL, code=302)
    return render_template("book_fallback.html", email=CONTACT_EMAIL)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
