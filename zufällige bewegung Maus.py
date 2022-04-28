from pynput.mouse import Controller
import random
import time
import pygame
pygame.init()
mouse = Controller()
#Nur für Testzwecke
'''
times = time.time()
while time.time() - times < 1:
    mouse.position = (random.randint(0,pygame.display.list_modes()[0][0]), random.randint(0,pygame.display.list_modes()[0][1]))
'''
while True:
    mouse.position = (random.randint(0,pygame.display.list_modes()[0][0]), random.randint(0,pygame.display.list_modes()[0][1]))