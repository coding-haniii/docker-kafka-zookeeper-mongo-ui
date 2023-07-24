import logging
from ksql import KSQLAPI
from datetime import datetime
from pytz import timezone

logging.basicConfig(level=logging.DEBUG)
client = KSQLAPI('http://localhost:8088')
localtime = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')


client.ksql("INSERT INTO stream01 (id, time, no) VALUES ('haeun pyUp', '2023-07-20 19:40:10', 6);")
client.ksql("INSERT INTO stream01 (id, time, no) VALUES ('haeun pyUp', '2023-07-20 19:40:10', 7);")
client.ksql("INSERT INTO stream01 (id, time, no) VALUES ('haeun pyUp', '2023-07-20 19:40:10', 8);")

