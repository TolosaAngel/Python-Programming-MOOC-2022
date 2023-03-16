import pygame
import math
import datetime

pygame.init()

display = pygame.display.set_mode((800,800))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

def convert(R, theta):
    x = math.sin(2*math.pi*theta/360)*R
    y = math.cos(2*math.pi*theta/360)*R
    return (x+400, -(y-400))

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        display.fill((0,0,0))
        pygame.draw.circle(display, (255, 0, 0), (400, 400), 15)
        pygame.draw.circle(display, (255,0,0), (400,400), 400, 5)
        
        R = 280
        theta = (hour + minute/60 + second/3600) * (360/12) 
        pygame.draw.line(display, (0,0,255), (400,400), convert(R, theta), 5)

        R = 350
        theta = (minute + second/60) * (360/60) 
        pygame.draw.line(display, (0,50,255), (400,400), convert(R, theta), 5)

        R = 380
        theta = second * (360/60) 
        pygame.draw.line(display, (0,100,255), (400,400), convert(R, theta), 5)

        pygame.display.update()
        clock.tick(50)

game()