'''
Create music player with keyboard controller. 
You have to be able to press keyboard: play, stop, next and previous as some keys. 
Player has to react to the given command appropriately.'''


import pygame
pygame.init()
screen = pygame.display.set_mode((960, 600))
songs = ['ride.mp3','eminem.mp3','maniac.mp3','gorillaz.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_SPACE:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
    pygame.display.flip()