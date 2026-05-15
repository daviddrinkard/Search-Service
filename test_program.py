import requests

# Request Data From Search Service
response = requests.get("http://localhost:5000/search?keyword=Policy")

# Print Status Code
print("Status Code:", response.status_code)

# Print Data Received From Search Service
print("Response Data:")
print(response.json())
