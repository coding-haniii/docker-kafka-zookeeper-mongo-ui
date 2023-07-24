import logging
from ksql import KSQLAPI
from datetime import datetime
from pytz import timezone

logging.basicConfig(level=logging.DEBUG)
client = KSQLAPI('http://localhost:8088')

client.ksql("CREATE STREAM stream01 (id VARCHAR, time VARCHAR, no int) WITH (kafka_topic='stream01', value_format='json', partitions=1);")


