import requests, configparser

def get_api_key(section: str):
    config = configparser.ConfigParser()
    config.read('apis.conf')
    api_key = config[section]["api"]
    return api_key

def get_api_endpoint(section: str):
    config = configparser.ConfigParser()
    config.read('endpoints.conf')
    endpoint = config[section]["endpoint"]
    return endpoint

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