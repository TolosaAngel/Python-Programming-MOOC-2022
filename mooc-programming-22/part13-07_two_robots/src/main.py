import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x = 0
x2 = 0
y = 50
y2 = 150
velocity = 3
velocity2 = 4

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x += velocity
    x2 += velocity2

    if velocity > 0 and x+robot.get_width() >= window.get_width():
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    if velocity2 > 0 and x2+robot2.get_width() >= window.get_width():
        velocity2 = -velocity2
    if velocity2 < 0 and x2 <= 0:
        velocity2 = -velocity2    

    clock.tick(60)