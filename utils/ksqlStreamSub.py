import logging
from ksql import KSQLAPI
logging.basicConfig(level=logging.DEBUG)
client = KSQLAPI('http://localhost:8088')

#client.ksql('show tables')

query = client.query('select * from stream01')
for item in query: print(item)

