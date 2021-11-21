import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "P9mHHXcyeZ5k0DONYAdNYBqjfVou274xsUw7S29Q"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)

photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
print(photos[1]["img_src"])