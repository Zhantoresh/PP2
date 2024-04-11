'''
1)Draw rectangle
2)Draw circle
3)Eraser
4)Color selection
'''
import pygame 

pygame.init() 


WIDTH = 800 
HEIGHT = 600

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)


colordict = {
    "red":colorRED,
    "green":colorGREEN,
    "blue":colorBLUE,
    "yellow":colorYELLOW
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))

base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)
screen.fill(colorWHITE)


LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

mode = "rectangle"
color_mode = "red"


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


done = False

while not done:

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
           
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                
                if mode == "rectangle":
                    pygame.draw.rect(screen, colordict[color_mode], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                if mode == "circle":
                    pygame.draw.circle(screen, colordict[color_mode], (prevX,prevY),abs(currX-prevX), THICKNESS)
                if mode == "eraser":
                    pygame.draw.circle(screen, colorWHITE, (currX,currY), 20)
                    base_layer.blit(screen, (0,0)) #позволяет сохранить изменения после применения ластика
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            if mode == "rectangle":
                pygame.draw.rect(screen, colordict[color_mode], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            if mode == "circle":
                pygame.draw.circle(screen, colordict[color_mode], (prevX,prevY),abs(currX-prevX), THICKNESS)
                base_layer.blit(screen, (0,0))#сохраняет предыдущие рисунка на экран base_layer
            

        if event.type == pygame.KEYDOWN: 
            
            
            if event.key == pygame.K_SPACE:
                mode = "circle"
                print("drawing mode switched to circle")
            if event.key == pygame.K_ESCAPE:
                mode = "rectangle"
                print("drawing mode switched to rectangle")
            if event.key == pygame.K_e:
                mode = "eraser"
                print("eraser was chosen")

            elif event.key == pygame.K_r:
                color_mode = "red"
                print("now the color is red")
            elif event.key == pygame.K_b:
                color_mode = "blue"
                print("now the color is blue")
            elif event.key == pygame.K_g:
                color_mode = "green"
                print("now the color is green")
            elif event.key == pygame.K_y:
                color_mode = "yellow"
                print("now the color is yellow")
        

    pygame.display.flip()