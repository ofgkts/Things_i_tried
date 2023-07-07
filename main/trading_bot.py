import json
import requests
import time
from winotify import Notification, audio 
# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
# Making list for multiple crypto's
currencies = ["BTCUSDT"]
j = 0
limit=[30274]
while True:
    
    for i in range(len(currencies)):
        
        # completing API for request
        url = key+currencies[j]  
        data = requests.get(url)
        data = data.json()
        j = j+1
        if float(data['price'])>limit[i]:
            a=Notification(app_id='ofgkts price alarm bot ',
                            title='price alert for'+currencies[i],
                            msg=f"{currencies[i]} has reached {data['price']}")
            
            a.set_audio(audio.LoopingAlarm2,loop=True)
            a.show()
        time.sleep(1)
        

