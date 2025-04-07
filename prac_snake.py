import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

x, y = 400, 300
size = 30
dx, dy = 0, 0
speed = 5
green = (0, 255, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 72)


running = True

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -speed, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = speed, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -speed
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, speed
    
    x += dx
    y += dy
    
    if x < 0 or x + size > 800 or y < 0 or y + size > 600:
        text = font.render('Game Over', True, (255, 0, 0))
        screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.time.delay(2000)  # 2초 동안 보여주기
        running = False

    
    screen.fill(white)
    pygame.draw.rect(screen, green, (x, y, size, size))
    pygame.display.flip()
    clock.tick(60)
                

pygame.quit()