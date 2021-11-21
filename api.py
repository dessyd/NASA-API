import configparser

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