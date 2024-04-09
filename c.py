import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)
colorPINK = (255, 192, 203)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

colordict = {
    "red": colorRED,
    "blue": colorBLUE,
    "green": colorGREEN,
    "yellow": colorYELLOW,
    "pink": colorPINK
}

LMBpressed = False
THICKNESS = 5

drawing_mode = "rectangle"
current_color = "red"
eraser = False

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(center, radius):
    pygame.draw.circle(screen, colordict[current_color], center, radius, THICKNESS)

done = False

while not done:
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                if drawing_mode == "rectangle":
                    if not eraser:
                        pygame.draw.rect(screen, colordict[current_color], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                    else:
                        pygame.draw.line(screen, colorBLACK,(currX, currY), (prevX, prevY), 20)
                elif drawing_mode == "circle":
                    radius = max(abs(currX - prevX), abs(currY - prevY))
                    center = (prevX, prevY)
                    if not eraser:
                        calculate_circle(center, radius)
                    else:
                        pygame.draw.line(screen, colorBLACK,(currX, currY), (prevX, prevY), 20)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if drawing_mode == "rectangle":
                if not eraser:
                    pygame.draw.rect(screen, colordict[current_color], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                else:
                    pygame.draw.line(screen, colorBLACK,(currX, currY), (prevX, prevY), 20)
            elif drawing_mode == "circle":
                radius = max(abs(currX - prevX), abs(currY - prevY))
                center = (prevX, prevY)
                if not eraser:
                    calculate_circle(center, radius)
                else:
                    pygame.draw.rect(screen, colorBLACK,(currX, currY), (prevX, prevY), 20)
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                drawing_mode = "circle"
                print("Drawing mode switched to circle")
            elif event.key == pygame.K_ESCAPE:  
                drawing_mode = "rectangle"
                print("Drawing mode switched to rectangle")
            elif event.key == pygame.K_b:
                current_color = "blue"
                print("blue color was chosen")
            elif event.key == pygame.K_g:
                current_color = "green"
                print("green color was chosen")
            elif event.key == pygame.K_y:
                current_color = "yellow"
                print("yellow color was chosen")
            elif event.key == pygame.K_p:
                current_color = "pink"
                print("pink color was chosen")
            elif event.key == pygame.K_r:
                current_color = "red"
                print("red color was chosen")
            elif event.key == pygame.K_e:
                eraser = not eraser
                if eraser:
                    print("Eraser mode activated")
                else:
                    print("Eraser mode deactivated")

    pygame.display.flip()