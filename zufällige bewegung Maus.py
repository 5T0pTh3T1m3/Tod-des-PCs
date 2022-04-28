from pynput.mouse import Controller
import random
import time
import pygame

pygame.init()

width = pygame.display.list_modes()[0][0]
height = pygame.display.list_modes()[0][1]

mouse = Controller()
times = time.time()

while True:
    mouse.position = (random.randint(0,int(width)), random.randint(0,int(height)))