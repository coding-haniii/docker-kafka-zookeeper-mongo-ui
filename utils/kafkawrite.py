from kafka import KafkaProducer
import json 
from json import dumps
from datetime import datetime
from pytz import timezone
	
p = KafkaProducer(bootstrap_servers = ['localhost:9092'], value_serializer = lambda x:dumps(x).encode('utf-8'))

data = {'haeun': 'send to localhost:9092', 'time':datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}

p.send('testdb1.book', value = data)

p.flush()
