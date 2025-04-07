import pygame
pygame.init()

import random

food_size = 30
def new_food():
    fx = random.randint(0, (800 - food_size) // food_size) * food_size
    fy = random.randint(0, (600 - food_size) // food_size) * food_size
    return fx, fy



screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

x, y = 400, 300 # 시작할 좌표 설정
size = 30
dx, dy = 0, 0 # 벡터 계산을 위한 변수 설정
speed = 30 # 벡터값 갱신을 위한 값
green = (0, 255, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 72)
RED = ((255, 0, 0))

food_x , food_y = new_food()
    

running = True

while running:
    screen.fill((255, 255, 255)) # 화면 하얀색
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # 종료를 위한 조건 확인 -> 조건 달성 시 종료
            
        elif event.type == pygame.KEYDOWN: # 이벤트 분기 확인 -> 키보드가 눌릴 때
            new_dx, new_dy = dx, dy # 입력 방향 저장
            
            if event.key == pygame.K_LEFT: 
                new_dx, new_dy = -speed, 0 # 방향을 설정, speed값만큼 이동 
            elif event.key == pygame.K_RIGHT:
                new_dx, new_dy = speed, 0
            elif event.key == pygame.K_UP:
                new_dx, new_dy = 0, -speed
            elif event.key == pygame.K_DOWN:
                new_dx, new_dy = 0, speed

            if not (new_dx == -dx and new_dy == -dy): # 입력한 방향이 현재 방향과 정반대일때
                dx, dy = new_dx, new_dy # 입력값 무시 
                
    x += dx # 해당 방향으로 벡터값 갱신 
    y += dy
    
    
    
    if x == food_x and y == food_y:
        food_x, food_y = new_food()    
        screen.blit(text, (200, 200))
        running = False
    
    if x < 0 or x + size > 800 or y < 0 or y + size > 600: # 각 방향의 끝에 도달했을때
        text = font.render('Game Over', True, (255, 0, 0)) # 텍스트 설정
        screen.blit(text, (250, 250)) # 텍스트 출력
        pygame.display.flip() # 결과값 화면에 반환
        pygame.time.delay(2000)  # 2초 동안 보여주기
        running = False # 작동 종료 

    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))


    pygame.draw.rect(screen, green, (x, y, size, size)) # 도형 그리기(뱀 머리)
    pygame.display.flip() # 그린 사각형 화면에 반환
    clock.tick(10) # FPS 설정 


pygame.quit()