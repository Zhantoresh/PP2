'''
Create a simple clock application (only with minutes and seconds) 
which is synchronized with system clock.
Use Mickey's right hand as minutes arrow and left - as seconds. '''
import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 1200, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))


seconds = pygame.image.load("/Users/1/Desktop/PP2/Lab7/01_mickeymouse/leftarm.png")
minutes = pygame.image.load("/Users/1/Desktop/PP2/Lab7/01_mickeymouse/rightarm.png")

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

   
    minute_angle = -minute_time * 6 
    second_angle = -second_time * 6 

    
    rotated_minutes = pygame.transform.rotate(minutes, minute_angle)
    rotated_seconds = pygame.transform.rotate(seconds, second_angle)

    
    screen.blit(background, (0, 0))

    
    screen.blit(rotated_minutes, (600 - rotated_minutes.get_width()//2, 500 - rotated_minutes.get_height()//2))  
    screen.blit(rotated_seconds, (600 - rotated_seconds.get_width()//2, 500 - rotated_seconds.get_height()//2)) #right arm parameters: (63, 1050)
    pygame.display.flip()