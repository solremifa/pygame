import pygame
pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dino')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

char_run_img = pygame.image.load('char_run.png')
char_run_img = pygame.transform.scale(char_run_img, (200, 200))

char_jump_img = pygame.image.load('char_jump.png')
char_jump_img = pygame.transform.scale(char_jump_img, (200, 200))

char_slide_img = pygame.image.load('char_slide.png')
char_slide_img = pygame.transform.scale(char_slide_img, (200, 250))

dino = pygame.Rect(50, HEIGHT - 60, 60, 60)

gravity = 1
velocity = 0
is_jumping = False
is_sliding = False

running = True
while running:
    screen.fill(WHITE)

    # 1. 이벤트 처리 - 점프 상태만 갱신
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not is_jumping:
                if is_sliding:
                    velocity = -18
                else:
                    velocity = -15
                
                is_jumping = True
            if event.key == pygame.K_DOWN and not is_sliding:
                is_sliding = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is_sliding = False        
                

    # 2. 프레임마다 중력/점프 계산
    if is_jumping:
        dino.y += velocity
        velocity += gravity

        if dino.y >= HEIGHT - dino.height:
            dino.y = HEIGHT - dino.height
            is_jumping = False
            velocity = 0  # ← 깔끔하게 초기화

    # 3. 렌더링
    if is_jumping:
        screen.blit(char_jump_img, (dino.x, dino.y - char_jump_img.get_height() + dino.height))
    elif is_sliding:
        screen.blit(char_slide_img, (dino.x, dino.y - char_slide_img.get_height() + dino.height))

    else:
        screen.blit(char_run_img, (dino.x, dino.y - char_run_img.get_height() + dino.height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
