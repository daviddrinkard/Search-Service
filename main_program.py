import requests

SEARCH_SERVICE_URL = "http://localhost:5000/search"
FILTER_SERVICE_URL = "http://localhost:5001/filter"
SORT_SERVICE_URL = "http://localhost:5002/sort"
REPORT_SERVICE_URL = "http://localhost:5003/report"

incidents = [
    {"id": 1, "employee_name": "John Smith", "type": "Unauthorized Access", "severity": "High", "status": "Open"},
    {"id": 2, "employee_name": "Sarah Lee", "type": "Policy Violation", "severity": "Medium", "status": "Closed"}
]


def add_incident():
    print("\nAdd Incident")

    new_id = len(incidents) + 1
    employee_name = input("Enter employee name: ")
    incident_type = input("Enter incident type: ")
    severity = input("Enter severity: ")
    status = input("Enter status: ")

    new_incident = {
        "id": new_id,
        "employee_name": employee_name,
        "type": incident_type,
        "severity": severity,
        "status": status
    }

    incidents.append(new_incident)

    print("\nIncident added:")
    print(new_incident)


def search_incidents():
    keyword = input("Enter keyword to search for: ")

    response = requests.get(SEARCH_SERVICE_URL, params={"keyword": keyword})

    print("\nRequest sent to Small Pool Search Service:")
    print(f"GET /search?keyword={keyword}")
    print("Response received:")
    print(response.json())


def update_incident():
    print("\nUpdate Incident")

    try:
        incident_id = int(input("Enter incident ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for incident in incidents:
        if incident["id"] == incident_id:
            print("\nCurrent incident:")
            print(incident)

            new_status = input("Enter new status or press Enter to keep current: ")
            new_severity = input("Enter new severity or press Enter to keep current: ")

            confirm = input("Confirm update? Type yes to update or no to cancel: ")

            if confirm.lower() != "yes":
                print("Update canceled.")
                return

            if new_status:
                incident["status"] = new_status
            if new_severity:
                incident["severity"] = new_severity

            print("\nIncident updated:")
            print(incident)
            return

    print("Incident not found.")


def filter_incidents():
    status = input("Enter status to filter by, like Open, Closed, or Under Review: ")

    response = requests.get(FILTER_SERVICE_URL, params={"status": status})

    print("\nRequest sent to Big Pool Filter Service:")
    print(f"GET /filter?status={status}")
    print("Response received:")
    print(response.json())


def sort_incidents():
    sort_by = input("Sort by id, employee_name, type, severity, or status: ")
    order = input("Order asc or desc: ")

    response = requests.get(
        SORT_SERVICE_URL,
        params={"sort_by": sort_by, "order": order}
    )

    print("\nRequest sent to Big Pool Sort Service:")
    print(f"GET /sort?sort_by={sort_by}&order={order}")
    print("Response received:")
    print(response.json())


def generate_report():
    response = requests.get(REPORT_SERVICE_URL)

    print("\nRequest sent to Big Pool Report Service:")
    print("GET /report")
    print("Response received:")
    print(response.json())


def view_all_incidents():
    print("\nAll Incidents")

    if not incidents:
        print("No incidents found.")
        return

    for incident in incidents:
        print(
            f"{incident['id']}. "
            f"{incident['employee_name']} | "
            f"{incident['type']} | "
            f"{incident['severity']} | "
            f"{incident['status']}"
        )


def show_menu():
    print("\nIncident Management System")
    print("--------------------------------")
    print("1. Add Incident")
    print("2. View Incidents")
    print("3. Search Incidents")
    print("4. Update Incident")
    print("5. Filter Incidents")
    print("6. Sort Incidents")
    print("7. Generate Incident Report")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_incident()
        elif choice == "2":
            view_all_incidents()
        elif choice == "3":
            search_incidents()
        elif choice == "4":
            update_incident()
        elif choice == "5":
            filter_incidents()
        elif choice == "6":
            sort_incidents()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Exiting Incident Management System.")
            break
        else:
            print("Invalid option. Please choose 1-8.")


if __name__ == "__main__":
    main()
