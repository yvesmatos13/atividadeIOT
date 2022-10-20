import os
import time
import schedule
from servico import servico
            
schedule.every(1).seconds.do(servico.dweepy)

while True:
    
    schedule.run_pending()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')