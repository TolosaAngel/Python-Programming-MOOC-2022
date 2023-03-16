from random import random
import time
import pygame

pygame.init()
pygame.display.set_caption("My own game - A rain of coins")

window = pygame.display.set_mode((800, 600))
game_font = pygame.font.SysFont("ComicSans", 10)
clock = pygame.time.Clock()

class Entity:
    def __init__(self, image: str):
        self.name = image[:-4]
        self.image = pygame.image.load(image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(random() * (window.get_width() - self.image.get_width())) 
        self.y = - int(random() * 1500) 

    def reposition(self):
        self.x = int(random() * (window.get_width() - self.image.get_width()))
        self.y = - int(random() * 1500) 

    def refresh(self):
        window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

        match_in_x = robot.x - robot.width/2 - self.width/2 <= self.x <= robot.x + robot.width/2 + self.width/2
        match_in_y = window.get_height() - robot.height - self.height -60 <= self.y <= window.get_height() - 60

        if match_in_x and match_in_y:
            self.reposition()
            
            if self.name == "coin":
                Coin.coins += 1
                Robot.points += 10
            elif self.name == "monster":
                Robot.life -= 1
                Robot.points -= 10

        if self.y >= window.get_height() - self.height - 60:
            self.reposition()
        else:
            self.y += 5 + Robot.points * 0.01

class Robot(Entity):
    life = 5
    speed_boost = 0
    points = 0

    def __init__(self, image: str):
        super().__init__(image)
        self.x = window.get_width() / 2 - self.width / 2
        self.y = window.get_height() - self.height - 60

    def reposition(self):
        self.x = window.get_width() / 2 - self.width / 2 
        self.y = window.get_height() - self.height - 60

class Coin(Entity):
    coins = 0

    def __init__(self, image: str):
        super().__init__(image)

class Monster(Entity):
    def __init__(self, image: str):
        super().__init__(image)

def restart(message: str):
    if message == "Game Over !":
        final_message_font = pygame.font.SysFont("ComicSans", 50)
        final_message = final_message_font.render(message, True, (0, 0, 0))
        window.blit(final_message, (window.get_width()/2- final_message.get_width()/2, window.get_height() / 6))
        message = "Restarting..."

    final_message_font = pygame.font.SysFont("ComicSans", 20)
    
    if Robot.points<0:
        Robot.points = 0

    restart_message = final_message_font.render(message, True, (0, 0, 0))
    window.blit(restart_message, (window.get_width()/2- restart_message.get_width()/2, window.get_height() / 3.5))
    final_score_message = final_message_font.render(f"Score: {Robot.points}", True, (0, 0, 0))
    window.blit(final_score_message, (window.get_width()/2- final_score_message.get_width()/2, window.get_height() / 3))

    pygame.display.flip()   
    time.sleep(2)
    
    Robot.life = 5
    Robot.speed_boost = 0
    Robot.points = 0
    Coin.coins = 0

    robot.reposition()
    for coin in coins: coin.reposition()
    for monster in monsters: monster.reposition()

def text():
    life_status_text = game_font.render(f"HEALTH", True, (255, 0, 0))
    window.blit(life_status_text, (87 - life_status_text.get_height(), window.get_height() - 50 - life_status_text.get_height() / 2))
    
    coins_status_text = game_font.render(f"COINS", True, (0, 0, 0))
    window.blit(coins_status_text, (225- coins_status_text.get_height(), window.get_height() - 50 - coins_status_text.get_height() / 2))

    coin_text = game_font.render(f": {Coin.coins}", True, (0, 0, 0))
    window.blit(coin_text, (230, window.get_height() - coin_text.get_height() - 18))

    shop1 = game_font.render("Press 1 to BUY LIFE for 10 coins", True, (0, 0, 0))
    window.blit(shop1, (window.get_width() - shop1.get_width() - 350, window.get_height() - shop1.get_height() - 45))
    
    shop2 = game_font.render("Press 2 to BOOST ROBOT SPEED for 15 coins", True, (0, 0, 0))
    window.blit(shop2, (window.get_width() - shop1.get_width() - 350, window.get_height() - shop1.get_height() - 25))
    
    shop3 = game_font.render("Press 3 to ELIMINATE NEAR MONSTERS for 20 coins", True, (0, 0, 0))
    window.blit(shop3, (window.get_width() - shop1.get_width() - 350, window.get_height() - shop1.get_height() - 5))

    menu1 = game_font.render("Press R to RESTART", True, (0, 0, 0))
    window.blit(menu1, (window.get_width() - menu1.get_width() - 100, window.get_height() - menu1.get_height() - 36))
    
    menu2 = game_font.render("Press Q to QUIT", True, (0, 0, 0))
    window.blit(menu2, (window.get_width() - menu1.get_width() - 100, window.get_height() - menu1.get_height() - 12))

def draw_hud():
    window.fill((64, 207, 255))
    pygame.draw.rect(window, (10, 255, 10), (0, window.get_height() - 60, window.get_width(), window.get_height()))
    
    text()

    x = 20
    life = Robot.life

    for iteration_for_circle in range(5):
        if life > 0:
            pygame.draw.circle(window, (240, 0, 0), (x, window.get_height() - 25), 10)
            life -= 1
        else:
            pygame.draw.circle(window, (240, 0, 0), (x, window.get_height() - 25), 10, 2)
        
        x += 35

    pygame.draw.circle(window, 	(255, 255, 0), (x + 20, window.get_height() - 25), 10)

robot = Robot("robot.png")
to_left = False
to_right = False

coins = [Coin("coin.png") for i in range(8)]
monsters = [Monster("monster.png") for i in range(8)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if Coin.coins >= 10 and Robot.life < 5:
                    Coin.coins -= 10
                    Robot.life += 1
            if event.key == pygame.K_2:
                if Coin.coins >= 15:
                    Coin.coins -= 15
                    Robot.speed_boost += 5
            if event.key == pygame.K_3:
                if Coin.coins >= 20:
                    Coin.coins -= 20
                    for monster in monsters: monster.reposition()
            if event.key == pygame.K_r:
                restart("Restarting...")
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_a:
                to_left = True
            if event.key == pygame.K_d:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_left = False
            if event.key == pygame.K_d:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    draw_hud()

    window.blit(robot.image, (robot.x, robot.y))

    for coin in coins: coin.refresh()
    for monster in monsters: monster.refresh()

    if to_right and (robot.x + robot.width < window.get_width()):
        robot.x += 10 + Robot.speed_boost
    if to_left and robot.x > 0:
        robot.x -= 10 + Robot.speed_boost

    if Robot.life == 0:
        restart("Game Over !")

    clock.tick(30)