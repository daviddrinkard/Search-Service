import requests

print("Incident Tracker Main Program")
print("--------------------------------")

# Small Pool Microservice: Search Service
search_response = requests.get("http://localhost:5000/search?keyword=Policy")
print("\nSmall Pool Microservice: Search Service")
print("Request: GET /search?keyword=Policy")
print("Response:")
print(search_response.json())

# Big Pool Microservice #1: Filter Service
filter_response = requests.get("http://localhost:5001/filter?status=Open")
print("\nBig Pool Microservice #1: Filter Service")
print("Request: GET /filter?status=Open")
print("Response:")
print(filter_response.json())

# Big Pool Microservice #2: Sort Service
sort_response = requests.get("http://localhost:5002/sort?sort_by=date&order=desc")
print("\nBig Pool Microservice #2: Sort Service")
print("Request: GET /sort?sort_by=date&order=desc")
print("Response:")
print(sort_response.json())

# Big Pool Microservice #3: Report Service
report_response = requests.get("http://localhost:5003/report")
print("\nBig Pool Microservice #3: Report Service")
print("Request: GET /report")
print("Response:")
print(report_response.json())
