import dweepy
import os
import time
import schedule
from conexao import Conexao

def Dweepy():

    iot = 'Weather_station_001'

    url = dweepy.get_latest_dweet_for(iot)

    dict = url[0]
    
    longdate = dict['created']

    temperature = dict['content']['temperature']

    humidity = dict['content']['humidity']

    pressure = dict['content']['pressure']
    
    date = longdate[:10]
    
    stamptime = longdate[11:19]
    
    Conexao(iot).iotDS().insert_one(dict)

    print('=============== Weather_station_001 =====================')
    print('Current temperature....',str(temperature)+'°C')
    print('Current humidity.......', humidity)
    print('Current pressure.......', pressure,'PSI')
    print('Date: ',date)
    print('TIme: ',stamptime)
    print('Done!')
    print('=========================================================')
            
schedule.every(1).seconds.do(Dweepy)

while True:
    
    schedule.run_pending()
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')