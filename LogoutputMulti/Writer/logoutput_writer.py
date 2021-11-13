#!/Users/admin/anaconda/bin/python3
import uuid
import datetime
import time

while True:
    print (f"<p>{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}  {str(uuid.uuid4())}")
    time.sleep(5)
