import requests

endpoint = 'http://httpbin.org/status/200'
endpoint = 'http://httpbin.org/anything'

get_response = requests.get(endpoint, json={'query':'hello world'})
print(get_response.status_code)