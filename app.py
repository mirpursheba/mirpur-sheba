from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/services")
def services():
    return send_file("services.html")

@app.route("/contact")
def contact():
    return send_file("contact.html")

@app.route("/style.css")
def style():
    return send_file("style.css", mimetype="text/css")

@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Us - MIRPUR SHEBA</title>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <h1>MIRPUR SHEBA</h1>
        <p>Complete Cleaning Solutions</p>
        <p>Professional Home & Office Cleaning Services.</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
