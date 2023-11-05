#Gabriel Campos Amaral Ribeiro
#08/05/2023

import pygame

#Inicia o mixer
pygame.init()

#Carrega o arquivo mp3
pygame.mixer.music.load('minhamusica.mp3')

#Inicia a reprodução
pygame.mixer.music.play()

#Verifica se a reprodução esta ativa
while pygame.mixer.music.get_busy():
    continue

#Fim do mixer
pygame.event.wait()