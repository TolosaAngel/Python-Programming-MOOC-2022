import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

original_width = robot.get_width()
width = 100

for i in range(1,12):
    window.blit(robot, (width, 100))
    width = original_width * i

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()