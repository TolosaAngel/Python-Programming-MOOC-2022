import pygame
from random import *

pygame.init()

window = pygame.display.set_mode((800, 600))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

for i in range(1000):
    x = int(random() * (window.get_width() - robot.get_width())) 
    y = int(random() * (window.get_height() - robot.get_height()))
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()