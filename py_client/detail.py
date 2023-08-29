import requests

endpoint = 'http://localhost:8000/api/products/1/' # localhost:8000/api/

get_response = requests.get(endpoint)
print(get_response.json())
