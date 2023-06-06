import requests

# Set the API endpoint URL and API key
url = 'https://sandbox.voltus.co/2022-04-15/sites'
api_key = 'secret'

# Set the headers with the API key
headers = {
    'X-Voltus-API-Key': api_key
}

# Send the GET request to the API
response = requests.get(url, headers=headers)

# Process the response
if response.status_code == 200:
    data = response.json()
    
    # Extract the current energy usage value from the response
    current_usage = data['usage']
    
    # Display energy usage as a numerical value
    print(f"Current Energy Usage: {current_usage} kWh")
    
    # Display energy usage as a progress bar (assuming maximum usage of 100 kWh)
    max_usage = 100
    progress = min(current_usage, max_usage) / max_usage
    progress_bar_length = 20
    filled_length = int(progress * progress_bar_length)
    bar = '#' * filled_length + '-' * (progress_bar_length - filled_length)
    print(f"Energy Usage Progress: [{bar}] {progress * 100:.2f}%")
    
else:
    print(f'Error: {response.status_code}')
