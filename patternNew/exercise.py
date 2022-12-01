import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
jsonresult=response.json()

print(response)
print(jsonresult)

toprint=json.dumps({'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, sort_keys=True, indent=4)
print(toprint)

toload=json.loads(toprint)
print(toload)