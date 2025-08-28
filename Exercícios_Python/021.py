# Mundo 1 - Exercício 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Resolvido com auxílio.

import pygame

pygame.init()
pygame.mixer.music.load("021.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(1000)

