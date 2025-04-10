import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dino')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)

# 이미지 불러오기 및 크기 조정
char_run_img = pygame.image.load('dino_assets/char_run.png')
char_run_img = pygame.transform.scale(char_run_img, (200, 200))

char_jump_img = pygame.image.load('dino_assets/char_jump.png')
char_jump_img = pygame.transform.scale(char_jump_img, (200, 200))

char_slide_img = pygame.image.load('dino_assets/char_slide.png')
char_slide_img = pygame.transform.scale(char_slide_img, (200, 250))

# 공룡 위치(논리적 위치 기준)
dino = pygame.Rect(50, HEIGHT - 60, 60, 60)

# 초기 장애물 설정
def create_obstacle():
    kind = random.choice(["ground", "air"])
    if kind == "ground":  # 점프로 넘는 장애물
        obstacle = pygame.Rect(WIDTH, HEIGHT - 60, 40, 60)  # 바닥에 붙은 장애물
        obstacle_hitbox = pygame.Rect(WIDTH + 5, HEIGHT - 55, 30, 40)
    else:  # 슬라이딩으로 통과하는 장애물 (공중)
        obstacle = pygame.Rect(WIDTH, HEIGHT - 130, 40, 30)  # 위에 떠 있는 장애물
        obstacle_hitbox = pygame.Rect(WIDTH + 5, HEIGHT - 185, 30, 20)
    return kind, obstacle, obstacle_hitbox

obstacle_type, obstacle, obstacle_hitbox = create_obstacle()
obstacle_speed = 7

# 점프 관련 변수
gravity = 1
velocity = 0
is_jumping = False
is_sliding = False

running = True
while running:
    screen.fill(WHITE)

    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not is_jumping:
                velocity = -18 if is_sliding else -15
                is_jumping = True
            if event.key == pygame.K_DOWN and not is_sliding:
                is_sliding = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is_sliding = False

    # 2. 점프 로직
    if is_jumping:
        dino.y += velocity
        velocity += gravity
        if dino.y >= HEIGHT - dino.height:
            dino.y = HEIGHT - dino.height
            is_jumping = False
            velocity = 0

    # 3. 공룡 이미지 상태
    if is_jumping:
        active_img = char_jump_img
    elif is_sliding:
        active_img = char_slide_img
    else:
        active_img = char_run_img

    draw_y = dino.y - active_img.get_height() + dino.height + 20
    screen.blit(active_img, (dino.x, draw_y))

    # 4. 공룡 히트박스
    if is_sliding:
        hitbox = pygame.Rect(dino.x + 50, draw_y + 140, 60, 90)
    else:
        hitbox = pygame.Rect(dino.x + 50, draw_y + 60, 60, 90)
    

    # 5. 장애물 이동 및 재생성
    obstacle.x -= obstacle_speed
    obstacle_hitbox.x = obstacle.x + 5  # 오프셋 유지
    obstacle_hitbox.y = obstacle.y + 10

    if obstacle.right < 0:
        obstacle_type, obstacle, obstacle_hitbox = create_obstacle()

    pygame.draw.rect(screen, (0, 0, 0), obstacle)            # 장애물 시각화
    
    
    # pygame.draw.rect(screen, (0, 0, 255), obstacle_hitbox, 2)  # 장애물 히트박스 시각화
    # pygame.draw.rect(screen, (255, 0, 0), hitbox, 2) # 공룡 히트박스 시각화
    
    
    # 6. 충돌 판정
    if hitbox.colliderect(obstacle_hitbox):
        if obstacle_type == "air" and is_sliding:
            pass  # 슬라이딩으로 통과 성공
        elif obstacle_type == "ground" and is_jumping:
            pass  # 점프로 회피 성공
        else:
            print("충돌!")
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

