import os
from flask import Flask, render_template

app = Flask(__name__)

# Set this in Render's environment variables.
# Use the GHL calendar PERMANENT LINK (the widget/booking URL), it goes inside the iframe.
CALENDAR_URL = os.environ.get("CALENDAR_URL", "")
CONTACT_EMAIL = "info@advisorautomationsgroup.com"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book")
def book():
    """Booking page with the GHL calendar embedded in an iframe.
    If the calendar link is not set yet, show the email fallback instead."""
    if CALENDAR_URL:
        return render_template("book.html", calendar_url=CALENDAR_URL)
    return render_template("book_fallback.html", email=CONTACT_EMAIL)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
