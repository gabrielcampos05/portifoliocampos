#Gabriel Campos Amaral Ribeiro
#04/11/2023

#Programa para fornecer notificação no Windows

from winotify import Notification, audio

notificacao = Notification(app_id="Notificação", title="TESTE", 
                           msg="Testando winotify",
                           duration="short",
                           icon=r"C:\Users\gabri\OneDrive\Imagens\Capturas de tela\Captura de tela 2023-07-19 121753.png")

#Audio para a notificação
notificacao.set_audio(audio.SMS, loop=False)

#Ação(botão) para a notificação
notificacao.add_actions(label="Youtube", launch="https://www.youtube.com/")

notificacao.show()

