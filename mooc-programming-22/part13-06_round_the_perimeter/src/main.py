import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 5
direction = "x"
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if direction == "x":
        x += velocity
    else:
        y += velocity

    if velocity > 0 and y+robot.get_height() >= window.get_height() or velocity < 0 and y <= 0:
        direction = "x"
        velocity = -velocity

    if velocity > 0 and x+robot.get_width() >= window.get_width() or velocity < 0 and x <= 0:
        direction = "y"

    clock.tick(60)