import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

x = 50
incrementer = 15
y = 50

for columns in range(10):
    for rows in range(10):
        window.blit(robot, (x,y))
        x += robot.get_width()
    x = 50 + incrementer
    incrementer += 15
    y += 25

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()