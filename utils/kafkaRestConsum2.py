import requests
import json

headers = {
    'Content-Type': 'application/vnd.kafka.v2+json',
}

data = '{"topics":["person"]}'

response = requests.post('http://localhost:8082/consumers/consumer_a/instances/consumer_a_instance/subscription', headers=headers, data=data)

print(response)
print(response.text)

