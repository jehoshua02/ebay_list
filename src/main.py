import os.path
_dir = os.path.dirname(os.path.realpath(__file__))

# Trying to use Trading API https://github.com/timotheus/ebaysdk-python/wiki/Trading-API-Class
from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError, ConnectionResponseError
try:
    config_file = _dir + '/../config/ebay.yaml'
    api = Trading(config_file=config_file, domain='api.sandbox.ebay.com')
    response = api.execute('GetUser', {})
    print(response.dict())
    print(response.reply)
except ConnectionError as e:
    print(e)
    print(e.response.dict())