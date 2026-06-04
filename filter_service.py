from flask import Flask, request, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "employee_name": "John Smith", "type": "Unauthorized Access", "severity": "High", "status": "Open"},
    {"id": 2, "employee_name": "Sarah Lee", "type": "Phishing Email", "severity": "Medium", "status": "Closed"},
    {"id": 3, "employee_name": "Bob Johnson", "type": "Policy Violation", "severity": "Low", "status": "Under Review"}
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
