import json
import time
import requests

CACHE_FILE_PATH = 'cache.json'
CACHE_EXPIRATION_TIME = 3600  # Default: 1 hour

def read_from_cache():
    try:
        with open(CACHE_FILE_PATH, 'r') as file:
            cache_data = json.load(file)
            if cache_data['timestamp'] + CACHE_EXPIRATION_TIME >= time.time():
                return cache_data['data']
    except (IOError, json.JSONDecodeError, KeyError):
        pass
    return None

def write_to_cache(data):
    cache_data = {
        'timestamp': time.time(),
        'data': data
    }
    try:
        with open(CACHE_FILE_PATH, 'w') as file:
            json.dump(cache_data, file)
    except IOError:
        pass

def fetch_data():
    try:
        response = requests.get('https://sandbox.voltus.co/2022-04-15/sites', headers={'X-Voltus-API-Key': 'secret'})
        if response.ok:
            return response.json()
    except requests.RequestException as e:
        # Handle fetch data errors
        print(f"Error fetching data: {e}")
    return None

def get_sites(refresh=False):
    if not refresh:
        data = read_from_cache()
        if data is not None:
            return data

    data = fetch_data()
    if data is not None:
        write_to_cache(data)

    return data

# Usage example
sites = get_sites()
if sites is not None:
    # Process the sites data
    print(sites)
