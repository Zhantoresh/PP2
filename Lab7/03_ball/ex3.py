import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
x = 200  # x and y are coordinates of the center
y = 200
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 400 - 25:
        x += 20
        x = min(x,400 - 25)
    if keys[pygame.K_LEFT] and x > 25:
        x -= 20
        x = max(x, 25)
    if keys[pygame.K_DOWN] and y < 400 - 25:
        y += 20
        y = min(y,400-25)
    if keys[pygame.K_UP] and y > 25:
        y -= 20
        y = max(y, 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(60)