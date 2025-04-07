import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

x, y = 400, 300 # 시작할 좌표 설정
size = 30 
dx, dy = 0, 0 # 벡터 계산을 위한 변수 설정
speed = 5 # 벡터값 갱신을 위한 값
green = (0, 255, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 72)


running = True

while running:
    screen.fill((255, 255, 255)) # 화면 하얀색
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # 종료를 위한 조건 확인 -> 조건 달성 시 종료
            
        elif event.type == pygame.KEYDOWN: # 이벤트 분기 확인 -> 키보드가 눌릴 때
            if event.key == pygame.K_LEFT: 
                dx, dy = -speed, 0 # 방향을 설정, speed값만큼 이동 
            elif event.key == pygame.K_RIGHT:
                dx, dy = speed, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -speed
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, speed
    
    x += dx # 해당 방향으로 벡터값 갱신 
    y += dy
    
    if x < 0 or x + size > 800 or y < 0 or y + size > 600: # 각 방향의 끝에 도달했을때
        text = font.render('Game Over', True, (255, 0, 0)) # 텍스트 설정
        screen.blit(text, (250, 250)) # 텍스트 출력
        pygame.display.flip() # 결과값 화면에 반환
        pygame.time.delay(2000)  # 2초 동안 보여주기
        running = False # 작동 종료 

    
    screen.fill(white)
    pygame.draw.rect(screen, green, (x, y, size, size))
    pygame.display.flip()
    clock.tick(60) # FPS 60으로 설정 
                

pygame.quit()