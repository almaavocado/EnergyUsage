import argparse
import requests

MAX_REDIRECTS = 5

# Function to retrieve sites from the Voltus API
def get_sites(api_key, page, per_page):
    base_url = 'https://sandbox.voltus.co'
    sites_endpoint = '/2022-04-15/sites'

    headers = {
        'Accept': 'application/json',
        'X-Voltus-API-Key': api_key
    }

    params = {'page': page, 'per_page': per_page}

    redirect_count = 0
    while redirect_count < MAX_REDIRECTS:
        try:
            url = f"{base_url}{sites_endpoint}"

            # Send a GET request to the API endpoint with provided headers and parameters
            response = requests.get(url, headers=headers, params=params, allow_redirects=False)
            response.raise_for_status()

            if response.status_code == 200:
                # If the response is successful (HTTP status code 200), return the JSON data
                return response.json()

            elif response.status_code == 302 and 'Location' in response.headers:
                redirect_url = response.headers['Location']

                # Make a request to the redirect URL
                response = requests.get(redirect_url, headers=headers, allow_redirects=False)
                response.raise_for_status()

                if response.status_code == 200:
                    # If the response is successful after following the redirect, return the JSON data
                    return response.json()

            else:
                # Unexpected response from the API
                print("Unexpected response from the API:")
                print(response.content.decode())
                break

        except requests.exceptions.RequestException as e:
            # Error occurred during the API request
            print(f"Error occurred during the API request: {e}")
            return None

        except Exception as e:
            # Unexpected error occurred
            print(f"An unexpected error occurred: {e}")
            return None

        redirect_count += 1

    # Exceeded the maximum number of redirects
    print("Exceeded the maximum number of redirects.")
    return None

# Function to display the retrieved sites with optional filtering and sorting
def display_sites(sites, filter_criteria=None, sort_attribute=None):
    if not sites:
        print("Failed to retrieve sites.")
        return

    # Apply filtering based on filter_criteria
    filtered_sites = sites
    if filter_criteria:
        filtered_sites = [site for site in sites if filter_criteria.lower() in site['name'].lower() or
                          filter_criteria.lower() in site['customer_location_id'].lower()]

    # Apply sorting based on sort_attribute
    if sort_attribute:
        if sort_attribute == "name":
            filtered_sites = sorted(filtered_sites, key=lambda site: site['name'])
        elif sort_attribute == "location":
            filtered_sites = sorted(filtered_sites, key=lambda site: site['customer_location_id'])
        elif sort_attribute == "meters":
            filtered_sites = sorted(filtered_sites, key=lambda site: len(site['meters']))

    # Display the site information
    for site in filtered_sites:
        site_id = site['id']
        site_name = site['name']
        customer_location_id = site['customer_location_id']
        meters = site['meters']

        print(f"Site ID: {site_id}")
        print(f"Site Name: {site_name}")
        print(f"Customer Location ID: {customer_location_id}")
        print("Meters:")
        for meter in meters:
            meter_id = meter['id']
            meter_name = meter['name']
            print(f"  - Meter ID: {meter_id}")
            print(f"    Meter Name: {meter_name}")
        print("-------------------")

# Main function to run the program
def main():
    parser = argparse.ArgumentParser(description="Voltus API Site List CLI")
    parser.add_argument("api_key", help="Your Voltus API key")

    args = parser.parse_args()
    api_key = args.api_key

    page = 0
    per_page = 10  # Set the number of items per page

    filter_criteria = args.filter
    sort_attribute = args.sort

    while True:
        # Retrieve sites from the Voltus API
        response = get_sites(api_key, page, per_page)
        if response is None:
            break

        sites = response.get('sites', [])

        # Display the retrieved sites with filtering and sorting
        display_sites(sites, filter_criteria, sort_attribute)

        if len(sites) < per_page:
            break

        # Ask the user if they want to view the next page or quit
        page += 1
        next_page = input("Press Enter to view the next page, or enter 'q' to quit: ")
        if next_page.lower() == 'q':
            break

if __name__ == "__main__":
    main()
