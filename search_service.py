from flask import Flask, request, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "employee_name": "John Smith", "type": "Unauthorized Access", "severity": "High", "status": "Open"},
    {"id": 2, "employee_name": "Sarah Lee", "type": "Phishing Email", "severity": "Medium", "status": "Closed"},
    {"id": 3, "employee_name": "Bob Johnson", "type": "Policy Violation", "severity": "Low", "status": "Under Review"}
]


@app.route("/search", methods=["GET"])
def search_records():
    keyword = request.args.get("keyword")

    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    results = []

    for record in records:
        for value in record.values():
            if keyword.lower() in str(value).lower():
                results.append(record)
                break

    return jsonify(results)


if __name__ == "__main__":
    app.run(port=5000)
