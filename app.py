from flask import Flask, request
import csv, os

app = Flask(__name__)

@app.route("/")
def home():
    with open("form.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    file_exists = os.path.isfile("submissions.csv")

    with open("submissions.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Email", "Message"])

        writer.writerow([name, email, message])

    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
