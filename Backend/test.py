import requests

# Set the API endpoint URL
url = 'https://sandbox.voltus.co/2022-04-15/sites'

# Set the headers with the API key
headers = {
    'X-Voltus-API-Key': 'secret'
}

# Send the GET request to the API
response = requests.get(url, headers=headers)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Access and utilize the energy usage data as per your requirements
    print(data)
else:
    print(f'Error: {response.status_code}')
