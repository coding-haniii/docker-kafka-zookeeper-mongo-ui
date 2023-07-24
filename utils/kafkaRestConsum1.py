import requests
import json
headers = {
    'Content-Type': 'application/vnd.kafka.v2+json',
}

data = '{"name": "consumer_a_instance", "format": "json", "auto.offset.reset": "earliest"}'

response = requests.post('http://localhost:8082/consumers/consumer_a', headers=headers, data=data)

print(response)
print(json.dumps(response.json(), indent=4))

