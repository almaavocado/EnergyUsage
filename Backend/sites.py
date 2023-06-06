import requests

api_key = 'secret'
url = 'https://sandbox.voltus.co/2022-04-15/sites'

headers = {
    'Accept': 'application/json',
    'X-Voltus-API-Key': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    sites = data['sites']
    
    for site in sites:
        site_id = site['id']
        site_name = site['name']
        print(f"Site ID: {site_id}")
        print(f"Site Name: {site_name}")
        print("-------------------")
else:
    print(f"Failed to retrieve sites. Error: {response.status_code}")
