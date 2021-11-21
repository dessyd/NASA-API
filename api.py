import configparser

def get_api_key(section: str):
    config = configparser.ConfigParser()
    config.read('apis.conf')
    try:
        api_key = config.get(section, "api")
    except (configparser.NoSectionError, configparser.NoOptionError):
        api_key = None
    return api_key

def get_api_endpoint(section: str):
    config = configparser.ConfigParser()
    config.read('endpoints.conf')
    try:
        endpoint = config.get(section, "endpoint")
    except (configparser.NoSectionError, configparser.NoOptionError):
        endpoint = None
    return endpoint