import requests
import json
from datetime import datetime
from pytz import timezone

headers = {
    'Content-Type': 'application/vnd.kafka.json.v2+json',
}
localtime = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
print(localtime)
data = '{"records":[{"value":{"id":"haeun", "time":"' + localtime + '"}}]}'

response = requests.post('http://localhost:8082/topics/person', headers=headers, data=data)

print(response)
print(json.dumps(response.json(), indent=4))
