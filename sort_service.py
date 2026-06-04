from flask import Flask, request, jsonify

app = Flask(__name__)

records = [
    {"id": 1, "employee_name": "John Smith", "type": "Unauthorized Access", "severity": "High", "status": "Open"},
    {"id": 2, "employee_name": "Sarah Lee", "type": "Phishing Email", "severity": "Medium", "status": "Closed"},
    {"id": 3, "employee_name": "Bob Johnson", "type": "Policy Violation", "severity": "Low", "status": "Under Review"}
]


@app.route("/sort", methods=["GET"])
def sort_records():
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")

    valid_fields = ["id", "employee_name", "type", "severity", "status"]

    if sort_by not in valid_fields:
        return jsonify({"error": "Invalid sort field"}), 400

    reverse_order = order.lower() == "desc"

    sorted_records = sorted(
        records,
        key=lambda record: str(record[sort_by]).lower(),
        reverse=reverse_order
    )

    return jsonify(sorted_records)


if __name__ == "__main__":
    app.run(port=5002)
