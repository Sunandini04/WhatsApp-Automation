import requests
import schedule
import time
from credentials import mobile_number

def send_text():
    payload = {
        'phone': mobile_number,
        'message': 'Hey there! What’s up?',
        'key': 'textbelt'
    }
    response = requests.post('https://textbelt.com/text', data=payload)
    print(response.json())


schedule.every(10).seconds.do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)
