import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 0
y = 0
velocity_x = 5
velocity_y = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    x += velocity_x
    y += velocity_y

    if velocity_x > 0 and x+ball.get_width() >= window.get_width() or velocity_x < 0 and x <= 0:
        velocity_x = - velocity_x

    if velocity_y > 0 and y+ball.get_height() >= window.get_height() or velocity_y < 0 and y <= 0:
        velocity_y = - velocity_y

    clock.tick(60)