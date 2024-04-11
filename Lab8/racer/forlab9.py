import pygame
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5*3
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):     
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED//3)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coins(pygame.sprite.Sprite):
    def __init__(self, supercoin = False):
        super().__init__()
        if supercoin:
            self.image = pygame.image.load("supercoin.png")
        else:    
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

def generate_coins(supercoin = False):
    new_coin = Coins(supercoin)
    coins.add(new_coin)
    all_sprites.add(new_coin)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
     

P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User events
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
# Generate super coins every 6 seconds
SUPERCOIN_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(SUPERCOIN_EVENT, 6000)  
# Generate coins every 3 seconds
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_EVENT, 3000)  


# Load sounds and set up channels
pygame.mixer.init()
crash_sound = pygame.mixer.Sound('crash.wav')
background_sound = pygame.mixer.Sound('background.wav')
background_sound.play(-1)  # Looping background sound

current_coin = None
while True:
    was_supercoin = False
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == SUPERCOIN_EVENT:
            was_supercoin = True        
            generate_coins(supercoin = True)
            current_coin = "super"
        if event.type == COIN_EVENT and was_supercoin == False:
            generate_coins()
            current_coin = "regular"
        if event.type == QUIT:
            pygame.quit()
            

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_collected = font_small.render(f"Coins: {COINS}", True, (0,200,20))

    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected, (300, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        background_sound.stop()
        crash_sound.play()
        time.sleep(2)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        

    # Check for collision with coins
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    if coin_collisions:
        if current_coin == "super":
            COINS += 2
        else:
            COINS += 1
        SPEED+=1    
    pygame.display.update()
    FramePerSec.tick(FPS)