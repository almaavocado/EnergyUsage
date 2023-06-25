import json
import time
import requests

CACHE_FILE_PATH = 'cache.json'
CACHE_EXPIRATION_TIME = 3600  # Default: 1 hour

'''Responsible for reading data from the cache file. 
It tries to open the file, load the JSON data, and check if the cache is still valid based on the timestamp 
and the expiration time defined by CACHE_EXPIRATION_TIME. 
If the cache is valid, it returns the cached data.'''
def read_from_cache():
    try:
        with open(CACHE_FILE_PATH, 'r') as file:
            cache_data = json.load(file)
            if cache_data['timestamp'] + CACHE_EXPIRATION_TIME >= time.time():
                return cache_data['data']
    except (IOError, json.JSONDecodeError, KeyError):
        pass
    return None

'''
Takes data as input, creates a cache_data dictionary containing the current timestamp 
and the data,
and writes this dictionary as JSON into the cache file specified by CACHE_FILE_PATH.
'''
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

'''
ends a GET request to a specific API endpoint ('https://sandbox.voltus.co/2022-04-15/sites') to retrieve data. 
If the response is successful (HTTP status code 200), it returns the JSON response data.

'''
def fetch_data():
    try:
        response = requests.get('https://sandbox.voltus.co/2022-04-15/sites', headers={'X-Voltus-API-Key': 'secret'})
        if response.ok:
            return response.json()
    except requests.RequestException as e:
        # Handle fetch data errors
        print(f"Error fetching data: {e}")
    return None

'''
The main entry point. It first checks if a refresh parameter is provided and, if set to False, 
attempts to read the data from the cache using the read_from_cache() function. 
If the data is available in the cache, it is returned.

'''
def get_sites(refresh=False):
    if not refresh:
        data = read_from_cache()
        if data is not None:
            return data

    data = fetch_data()
    if data is not None:
        write_to_cache(data)

    return data

'''
If the data is not found in the cache or a refresh is requested, 
the fetch_data() function is called to retrieve the data from the API.
If the data is successfully fetched, it is written to the cache using the write_to_cache() function.
The get_sites() function returns the fetched data, whether it was from the cache or the API.
'''

# Usage example
sites = get_sites()
if sites is not None:
    # Process the sites data
    print(sites)
