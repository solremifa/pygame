import pygame
import random

pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 게임 단위 설정
size = 30
speed = size  # 한 번에 이동할 거리 = 격자 크기와 동일

# 초기 뱀 설정
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = 0, 0
snake = [(x, y)]  # 뱀의 몸 좌표 리스트

# 먹이 생성 함수
def new_food():
    fx = random.randint(0, (WIDTH - size) // size) * size
    fy = random.randint(0, (HEIGHT - size) // size) * size
    return fx, fy

food_x, food_y = new_food()

# 폰트
font = pygame.font.SysFont(None, 72)

running = True
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_dx, new_dy = dx, dy
            if event.key == pygame.K_LEFT:
                new_dx, new_dy = -speed, 0
            elif event.key == pygame.K_RIGHT:
                new_dx, new_dy = speed, 0
            elif event.key == pygame.K_UP:
                new_dx, new_dy = 0, -speed
            elif event.key == pygame.K_DOWN:
                new_dx, new_dy = 0, speed

            if not (new_dx == -dx and new_dy == -dy):  # 반대 방향 차단
                dx, dy = new_dx, new_dy

    # 위치 이동
    x += dx
    y += dy
    snake.append((x, y))  # 머리 위치 추가

    # 충돌 감지 (Rect 기반)
    head = pygame.Rect(x, y, size, size)
    food = pygame.Rect(food_x, food_y, size, size)

    if head.colliderect(food):
        food_x, food_y = new_food()  # 먹이 새로 생성
        # pop 안 함 → 몸통 길어짐
    else:
        snake.pop(0)  # 먹이 안 먹었으면 꼬리 제거

    # 벽 충돌 감지
    if x < 0 or x + size > WIDTH or y < 0 or y + size > HEIGHT:
        text = font.render("Game Over", True, RED)
        screen.blit(text, (250, 250))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    # 자기 자신과 충돌 감지 (머리는 제외)
    if (x, y) in snake[:-1]:
        text = font.render("Self Crash!", True, RED)
        screen.blit(text, (220, 250))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    # 먹이 그리기
    pygame.draw.rect(screen, RED, (food_x, food_y, size, size))

    # 뱀 그리기
    for sx, sy in snake:
        pygame.draw.rect(screen, GREEN, (sx, sy, size, size))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
