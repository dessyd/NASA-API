import requests
from apis import get_api_key, get_api_endpoint

section = "nasa"

endpoint = get_api_endpoint(section)
api_key = get_api_key(section)

query_params = {"api_key": api_key, "earth_date": "2020-07-01"}

try:
    response = requests.get(endpoint, params=query_params)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)  

photos = response.json()["photos"]
if len(photos) > 0:
    print(photos[1]["img_src"])
else:
    print("No photos found")