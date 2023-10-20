import requests
import json

# Define the URL for retrieving email domains data
domain_url = "http://<your_url>/rest/migration/latest/email/domains"

# Set headers for the HTTP request, including the Authorization token
domain_headers = {
    "Accept": "application/json",
    "Authorization": "Bearer <your_personal_access_token>"
}

# Send an HTTP GET request to retrieve available domains data
response = requests.get(domain_url, headers=domain_headers)

# Parse the response JSON data
json_data = response.json()

# Extract the list of available domains from the JSON data
domains = json_data["availableDomains"]

# Loop through each domain in the list
for domain in domains:

    # Define the URL for updating domain rules
    domain_decision_url = "http://<your_url>/rest/migration/latest/email/domain-rules"

    # Set headers for the HTTP request, including the Authorization token and content type
    domain_decision_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_personal_access_token>"
    }

    # Prepare a JSON payload with the domain name and the rule to be applied (e.g., "TRUSTED")
    payload = json.dumps({
        "domainName": domain["domainName"],
        "rule": "TRUSTED"
    })

    # Send an HTTP PUT request to update the domain with the specified rule
    response = requests.put(domain_decision_url, headers=domain_decision_headers, data=payload)
