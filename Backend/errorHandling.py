import requests

api_key = 'secret'
url = 'https://sandbox.voltus.co/2022-04-15/sites'

headers = {
    'Accept': 'application/json',
    'X-Voltus-API-Key': api_key
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an exception for non-2xx status codes

    data = response.json()
    sites = data['sites']

    for site in sites:
        site_id = site['id']
        site_name = site['name']
        print(f"Site ID: {site_id}")
        print(f"Site Name: {site_name}")
        print("-------------------")

except requests.exceptions.RequestException as e:
    print(f"Error occurred during the API request: {e}")

except KeyError:
    print("Invalid response format. Failed to retrieve site data.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
