from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def analyze_logs(log_text):
    results = []

    rules = [
        {
            "keywords": ["failed login", "invalid password", "login failed"],
            "risk": "Medium",
            "reason": "This may indicate someone is trying to guess a password.",
            "action": "Check the username, IP address, and number of failed attempts."
        },
        {
            "keywords": ["unauthorized", "permission denied", "access denied"],
            "risk": "High",
            "reason": "This may indicate an attempt to access a restricted resource.",
            "action": "Review the account, source IP, and accessed file or service."
        },
        {
            "keywords": ["root login", "admin login"],
            "risk": "High",
            "reason": "Administrator-level login activity can be risky if unexpected.",
            "action": "Confirm whether this admin login was authorized."
        },
        {
            "keywords": ["error", "critical"],
            "risk": "Low",
            "reason": "Errors may show system issues or failed services.",
            "action": "Review the error message and check system health."
        },
        {
            "keywords": ["warning"],
            "risk": "Low",
            "reason": "Warnings may point to unusual but not always dangerous activity.",
            "action": "Monitor this event and look for repeated warnings."
        },
        {
            "keywords": ["brute force", "multiple failed attempts"],
            "risk": "High",
            "reason": "Repeated failed attempts may indicate a brute-force attack.",
            "action": "Consider locking the account or blocking the source IP."
        }
    ]

    lines = log_text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        lower_line = line.lower()

        for rule in rules:
            if any(keyword in lower_line for keyword in rule["keywords"]):
                results.append({
                    "line_number": line_number,
                    "log_entry": line,
                    "risk": rule["risk"],
                    "reason": rule["reason"],
                    "action": rule["action"]
                })
                break

    return results


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    original_logs = ""

    if request.method == "POST":
        pasted_logs = request.form.get("log_text", "")

        uploaded_file = request.files.get("log_file")

        if uploaded_file and uploaded_file.filename != "":
            file_content = uploaded_file.read().decode("utf-8", errors="ignore")
            original_logs = file_content
        else:
            original_logs = pasted_logs

        if original_logs.strip():
            results = analyze_logs(original_logs)

    return render_template("index.html", results=results, original_logs=original_logs)


if __name__ == "__main__":
    app.run(debug=True)