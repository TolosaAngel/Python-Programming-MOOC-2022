from random import *
import time
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Rock:
    window = pygame.display.set_mode((640, 480))

    def __init__(self):
        self.image = pygame.image.load("rock.png")
        self.x = int(random() * (Rock.window.get_width() - self.image.get_width())) 
        self.y = - int(random() * 1500) 

    def new_coordenates(self):
        self.x = int(random() * (Rock.window.get_width() - self.image.get_width())) 
        self.y = - int(random() * 1500) 

robot = pygame.image.load("robot.png")

x = window.get_width() / 2 - robot.get_width() / 2

to_right = False
to_left = False

points = 0

rocks = []

for i in range(7):
    rocks.append(Rock())

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    for rock in rocks:
        window.blit(rock.image, (rock.x, rock.y))
        pygame.display.flip()

        if rock.y > window.get_height():
            game_font = pygame.font.SysFont("Arial", 50)
            game_over_message = game_font.render(f"Game over!", True, (255, 0, 0))
            window.blit(game_over_message, (window.get_width()/2- game_over_message.get_width()/2, window.get_height()/2- game_over_message.get_height()/2))
            pygame.display.flip()
            
            time.sleep(3)

            for rock in rocks:
                rock.new_coordenates()

            
            x = window.get_width() / 2 - robot.get_width() / 2
            points = 0
        else:
            rock.y += 3

        window.blit(robot, (x, window.get_height()-robot.get_height()))

        if to_right and (x + robot.get_width() < window.get_width()):
            x += 2
        if to_left and x > 0:
            x -= 2

        match_in_x = x - robot.get_width()/2 <= rock.x <= x + robot.get_width()/2
        match_in_y = window.get_height() - robot.get_height() <= rock.y <= window.get_height() 

        if match_in_x and match_in_y:
            points += 1
            rock.new_coordenates()

        game_font = pygame.font.SysFont("Arial", 24)
        text = game_font.render(f"Points: {points}", True, (255, 0, 0))
        window.blit(text, (window.get_width() - text.get_width() - 15, 15))

    window.fill((0, 0, 0))
    clock.tick(30)