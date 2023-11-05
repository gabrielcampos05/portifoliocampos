#Gabriel Campos Amaral Ribeiro
#Agendamento de tarefas

import schedule
import time
from schedule import repeat,every

#Estutura para repetir o que esta em baixo
@repeat(every().minute)
#Tarefa a ser agendada
def tarefa():
    print('TESTANDO !!!')

#Aqui definimos quando iremos repetir cada coisa
#Schedule -> Agende

#schedule.every().second.do(tarefa)

#schedule.every(5).seconds.do(tarefa)

#schedule.every().day.at('05:50').do(tarefa)

#schedule.every().hour.at(':57').do(tarefa)

#schedule.every().second.until('15:01').do(tarefa)

while True:
    #Roda o programa
    schedule.run_pending()
    #Tempo de espera em [segundos]
    time.sleep(1)

