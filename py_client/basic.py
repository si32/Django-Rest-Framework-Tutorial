import requests

# endpoint = 'http://httpbin.org/status/200'
endpoint = 'http://localhost:8000/api/' # localhost:8000/api/

get_response = requests.post(endpoint, json={'content':'Hello world'})
print(get_response.status_code)
print(get_response.json())
# print(get_response.headers)
# print(get_response.text)
