import dweepy
from conexao import conexao

class servico():
    def dweepy():

        iots = ['Weather_station_001', 'roster.capably.sleepy.chamber', 'checkers.castrate.fur.husky', 'ViljaminCO2']
        
        for iot in iots:

            url = dweepy.get_latest_dweet_for(iot)

            dict = url[0]

            longdate = dict['created']

            temperature = dict['content']['temperature']

            humidity = dict['content']['humidity']

            pressure = dict['content']['pressure']

            date = longdate[:10]

            stamptime = longdate[11:19]

            conexao(iot).iotDS().insert_one(dict)

            print('===============',iot,'=====================')
            print('Current temperature....',str(temperature)+'°C')
            print('Current humidity.......', humidity)
            print('Current pressure.......', pressure,'PSI')
            print('Date: ',date)
            print('TIme: ',stamptime)
            print('Done!')