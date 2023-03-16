from random import *
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Robot:
    window = pygame.display.set_mode((640, 480))

    def __init__(self):
        self.image = pygame.image.load("robot.png")
        self.x = int(random() * (Robot.window.get_width() - self.image.get_width())) 
        self.y = - int(random() * 1200) 

    def new_coordenates(self):
        self.x = int(random() * (Robot.window.get_width() - self.image.get_width())) 
        self.y = - int(random() * 1200) 

robots = []

for i in range(7):
    robots.append(Robot())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for robot in robots:
        window.blit(robot.image, (robot.x, robot.y))
        pygame.display.flip()

        if robot.y > 0 and robot.y + robot.image.get_height() >= window.get_height():
            if robot.x > window.get_height() / 2:
                robot.x += 3
            else:
                robot.x -= 3
        else:
            robot.y += 3

        if robot.x + robot.image.get_width() < 0 or robot.x - robot.image.get_width() > window.get_width():
            robot.new_coordenates()

    window.fill((0, 0, 0))
    clock.tick(30)