import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))
window_width = window.get_width()
window_height = window.get_height()

robot = pygame.image.load("robot.png")
player1_robot = robot
player2_robot = robot

robot_width = robot.get_width()
robot_height = robot.get_height()

x = window_width/2 - robot_width/2 - 100
y = window_height/2 - robot_height/2
x2 = window_width/2 - robot_width/2 + 100
y2 = window_height/2 - robot_height/2

player1_to_up = False
player1_to_down = False
player1_to_right = False
player1_to_left = False

player2_to_up = False
player2_to_down = False
player2_to_right = False
player2_to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_to_up = True
            if event.key == pygame.K_DOWN:
                player1_to_down = True
            if event.key == pygame.K_LEFT:
                player1_to_left = True
            if event.key == pygame.K_RIGHT:
                player1_to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_to_up = False
            if event.key == pygame.K_DOWN:
                player1_to_down = False
            if event.key == pygame.K_LEFT:
                player1_to_left = False
            if event.key == pygame.K_RIGHT:
                player1_to_right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player2_to_up = True
            if event.key == pygame.K_s:
                player2_to_down = True
            if event.key == pygame.K_a:
                player2_to_left = True
            if event.key == pygame.K_d:
                player2_to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2_to_up = False
            if event.key == pygame.K_s:
                player2_to_down = False
            if event.key == pygame.K_a:
                player2_to_left = False
            if event.key == pygame.K_d:
                player2_to_right = False

        if event.type == pygame.QUIT:
            exit()

    if player1_to_up and y > 0:
        y -= 5
    if player1_to_down and (y + robot_height < window_height):
        y += 5
    if player1_to_right and (x + robot_width < window_width):
        x += 5
    if player1_to_left and x > 0:
        x -= 5

    if player2_to_up and y2 > 0:
        y2 -= 5
    if player2_to_down and (y2 + robot_height < window_height):
        y2 += 5
    if player2_to_right and (x2 + robot_width < window_width):
        x2 += 5
    if player2_to_left and x2 > 0:
        x2 -= 5    

    window.fill((0, 0, 0))
    window.blit(player1_robot, (x, y))
    window.blit(player2_robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)