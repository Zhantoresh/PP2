import pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

colorred = (255, 0, 0)
colorblue = (0, 0, 255)
colorwhite = (255, 255, 255)
colorblack = (0, 0, 0)

Thickness = 5

LMBpressed = False

currx = 0
curry = 0

base_layer = pygame.Surface((width, height))

prevx = 0
prevy = 0

done = False

while not done:
    
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer,(0, 0))
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
            prevx = event.pos[0]
            prevy = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:",event.pos)
            if LMBpressed:
                
                currx = event.pos[0]
                curry = event.pos[1]
                pygame.draw.rect(screen, colorred, (event.pos[0],event.pos[1], Thickness, Thickness))
                
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currx = event.pos[0]
            currx = event.pos[1]
            pygame.draw.rect(screen, colorred, (prevx, prevy,currx-prevx,curry-currx),Thickness )
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS:
                Thickness += 1
                print("increased thickness")
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                Thickness -= 1
        

    #pygame.draw.line(screen, colorred, (prevx,prevy),(currx,curry))
   

    pygame.display.flip()