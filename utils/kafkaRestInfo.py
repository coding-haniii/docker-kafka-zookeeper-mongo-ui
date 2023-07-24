import requests
import json
response = requests.get('http://localhost:8082/topics/person/')
print(response)
print(json.dumps(response.json(), indent=4))
