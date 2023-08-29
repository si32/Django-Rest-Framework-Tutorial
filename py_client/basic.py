import requests

# endpoint = 'http://httpbin.org/status/200'
endpoint = 'http://localhost:8000/api/' # localhost:8000/api/

get_response = requests.get(endpoint, json={'query':'hello world'})
print(get_response.status_code)
print(get_response.json()['message'])
