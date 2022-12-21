import requests

# Replace YOUR_API_KEY with your Google Maps API key
api_key = 'YOUR_API_KEY'

# Set the location and radius for the search
location = '39.9042,116.407396'  # Coordinates for Beijing, China
radius = 5000  # Search within a 5 km radius

# Set the search parameters
params = {
    'location': location,
    'radius': radius,
    'type': 'restaurant',
    'keyword': 'Turkish',
    'key': api_key
}

# Send the request to the Google Maps API
response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=params)

# Check the status code of the response
if response.status_code == 200:
    # Load the response data as a JSON
    data = response.json()
    # Print the name and address of each restaurant
    for restaurant in data['results']:
        print(restaurant['name'])
        print(restaurant['vicinity'])
        print()
else:
    print('An error occurred.')
