import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
window_width = window.get_width()
window_height = window.get_height()

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

x = window_width/2 - robot_width/2
y = window_height/2 - robot_height/2

to_up = False
to_down = False
to_right = False
to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    if to_up and y > 0:
        y -= 5
    if to_down and (y + robot_height < window_height):
        y += 5
    if to_right and (x + robot_width < window_width):
        x += 5
    if to_left and x > 0:
        x -= 5

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)