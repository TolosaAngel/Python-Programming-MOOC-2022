from random import *
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = int(random() * (window.get_width() - robot.get_width())) 
y = int(random() * (window.get_height() - robot.get_height()))
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    in_range_x = x - robot.get_width() / 2 <= target_x <= x + robot.get_width() / 2
    in_range_y = y - robot.get_height() / 2 <= target_y <= y + robot.get_height() / 2
    
    if in_range_x and in_range_y:
        x = int(random() * (window.get_width() - robot.get_width())) 
        y = int(random() * (window.get_height() - robot.get_height()))

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)