import requests
import json

headers = {
    'Accept': 'application/vnd.kafka.json.v2+json',
}

response = requests.get('http://localhost:8082/consumers/consumer_a/instances/consumer_a_instance/records', headers=headers)
print(response)
print(json.dumps(response.json(), indent=4))

