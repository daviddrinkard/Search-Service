from flask import Flask, request, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "type": "Unauthorized Access", "status": "Open", "date": "2026-06-01"},
    {"id": 2, "type": "Phishing Email", "status": "Closed", "date": "2026-05-28"},
    {"id": 3, "type": "Policy Violation", "status": "Under Review", "date": "2026-06-03"},
]

@app.route("/filter", methods=["GET"])
def filter_records():
    status = request.args.get("status")

    if not status:
        return jsonify({"error": "Status is required"}), 400

    results = [
        record for record in records
        if record["status"].lower() == status.lower()
    ]

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5001)
