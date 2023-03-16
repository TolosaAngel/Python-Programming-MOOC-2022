import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
angle_incrementer = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    for i in range(10):
        x = 320+math.cos(angle)*100-robot.get_width()/2
        y = 240+math.sin(angle)*100-robot.get_height()/2

        window.blit(robot, (x, y))
        pygame.display.flip()
        angle += 0.628

    angle_incrementer += 0.01
    angle = angle_incrementer

    clock.tick(60)