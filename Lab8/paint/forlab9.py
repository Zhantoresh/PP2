'''
1)Draw square
2)Draw right triangle
3)Draw equilateral triangle
4)Draw rhombus
5)Comment your code
'''
import pygame  # Импортирование библиотеки

pygame.init()  # Инициализация

# Константные переменные
WIDTH = 800
HEIGHT = 600
colorWHITE = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Создание базового слоя
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorWHITE)
screen.fill(colorWHITE)
pygame.display.set_caption("Paint")

# Создание объекта часов для контроля частоты смены кадров
clock = pygame.time.Clock()

# Логическое значение для отслеживания нажатия левой кнопки мыши
LMBpressed = False
THICKNESS = 5  # Thickness of drawing lines

# Переменные для отслеживания текущего и предыдущего положения мыши
currX = 0
currY = 0

prevX = 0
prevY = 0

# Режим рисования фигур
mode = "rectangle"
color_mode = "red"  # Изначальный цвет 

# Функция для вычисления прямоугольника на основе положения мыши
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Функция для вычисления вершин равностороннего треугольника
def calculate_equilateral_triangle(x1, y1, x2, y2):
    side_length = abs(x2 - x1)  # Calculate side length based on mouse positions
    height = int(side_length * (3 ** 0.5) / 2)  # Calculate height of equilateral triangle
    return ((x1, y1), ((x1 + x2) // 2, y1 - height), (x2, y1))  # Return vertices of triangle

def draw_rhombus(screen, color, rect):
    points = [rect.midtop, rect.midright, rect.midbottom, rect.midleft]
    pygame.draw.polygon(screen, color, points,THICKNESS)  # Draw the rhombus

# Статус игрового цикла
done = False

# Главный игровой цикл
while not done:

    # Проверка на события клавиш
    pressed = pygame.key.get_pressed()
    shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))  # Обновите экран при нажатии левой кнопки мыши
        if event.type == pygame.QUIT:
            done = True  # Выход из игрового цикла, если окно закрыто

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Запись предыдущего положения мыши при нажатии левой кнопки мыши
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                # Обновление позиции мыши при движении
                currX = event.pos[0]
                currY = event.pos[1]

                # Рисование основанное на режим 
                if mode == "rectangle":
                    pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "circle":
                    pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                elif mode == "righttriangle":
                    pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                elif mode == "triangle":
                    pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                elif mode == "rhombus":
                    rect1 = calculate_rect(prevX, prevY, currX, currY)
                    draw_rhombus(screen, color_mode, rect1)
                elif mode == "sguare":
                    # Координаты квадрата
                    top_left = (min(prevX, currX), min(prevY, currY))
                    side_length = min(abs(currX - prevX), abs(currY - prevY))
                    # Рисование квадрата
                    pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                elif mode == "eraser":
                    pygame.draw.circle(screen, (255, 255, 255), (currX, currY), THICKNESS)
                    base_layer.blit(screen, (0, 0))  # Обновление базового слоя для ластика

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Запись текущей позиции мыши при отпускании 
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]

            # Рисование в соответствии с выбранным режимом при отпущенной кнопке мыши
            if mode == "rectangle":
                pygame.draw.rect(screen, color_mode, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Обновление базового слоя после рисования
            elif mode == "circle":
                pygame.draw.circle(screen, color_mode, (prevX, prevY), abs(currX - prevX), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Обновление базового слоя после рисования
            elif mode == "righttriangle":
                pygame.draw.polygon(screen, color_mode, ((prevX, prevY), (prevX, currY), (currX, currY)), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Обновление базового слоя после рисования
            elif mode == "triangle":
                pygame.draw.polygon(screen, color_mode, calculate_equilateral_triangle(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))  # Обновление базового слоя после рисования
            elif mode == "rhombus":
                rect1 = calculate_rect(prevX, prevY, currX, currY)
                draw_rhombus(screen, color_mode, rect1)
                base_layer.blit(screen, (0, 0))
            elif mode == "sguare":
                # Исчисление координат квадрата
                top_left = (min(prevX, currX), min(prevY, currY))
                side_length = min(abs(currX - prevX), abs(currY - prevY))
                # Рисование квадрата
                pygame.draw.rect(screen, color_mode, (top_left[0], top_left[1], side_length, side_length), THICKNESS)
                base_layer.blit(screen, (0, 0)) 


        if event.type == pygame.KEYDOWN:
            # Управление ключевыми событиями 
            
            if event.key == pygame.K_ESCAPE:
                done = True  # Выход при нажатии на ESC

            # Смена режима рисования
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_r:
                mode = "rectangle"
            if event.key == pygame.K_t:
                mode = "righttriangle"
            if event.key == pygame.K_v:
                mode = "triangle"
            if event.key == pygame.K_h:
                mode = "rhombus"
            if event.key == pygame.K_e:
                mode = "eraser"
            if event.key == pygame.K_s:
                mode = "sguare"

            # Смена цвета для рисования
            if event.key == pygame.K_r and shift_held:
                color_mode = "red"
            if event.key == pygame.K_b and shift_held:
                color_mode = "blue"
            if event.key == pygame.K_g and shift_held:
                color_mode = "green"
            if event.key == pygame.K_k and shift_held:
                color_mode = "black"
            

    pygame.display.flip()  # Обновление дисплея
    clock.tick(10000000)  # Ограничение частоты кадров, чтобы избежать чрезмерной перегрузки процессора