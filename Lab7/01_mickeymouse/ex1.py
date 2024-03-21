'''
Create a simple clock application (only with minutes and seconds) 
which is synchronized with system clock.
Use Mickey's right hand as minutes arrow and left - as seconds. '''
import pygame
import datetime
pygame.init()

WIDTH, HEIGHT = 1200, 1000
midle = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

seconds = pygame.image.load("/Users/1/Desktop/PP2/Lab7/01_mickeymouse/leftarm.png")
minutes = pygame.image.load("/Users/1/Desktop/PP2/Lab7/01_mickeymouse/rightarm.png")
rectsec = seconds.get_rect()
rectmin = minutes.get_rect()
rectsec.center = midle 
rectmin.center = midle


background = pygame.image.load("/Users/1/Desktop/PP2/Lab7/01_mickeymouse/mainclock.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time_now = datetime.datetime.now()
    minute_time = time_now.minute 
    second_time = time_now.second

  
    angle1 = -minute_time * 6 
    leg1 = pygame.transform.rotate(minutes, angle1)
    rect1 = leg1.get_rect(center=rectmin.center)

    angle2 = -second_time * 6  
    leg2 = pygame.transform.rotate(seconds, angle2)
    rect2 = leg2.get_rect(center=rectsec.center)

    
    screen.blit(background, (0, 0))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)

    pygame.display.flip()
    clock.tick(60)