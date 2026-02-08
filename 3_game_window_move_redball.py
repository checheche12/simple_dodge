import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Window") 

# pygame 의 타이머를 불러옴
clock = pygame.time.Clock()
# 공의 위치와 속도를 설정
x = 200
y = 200
speed = 3

while True:
    # 화면을 검정 화면으로 초기화 한다.
    screen.fill((0, 0, 0))
    # 공을 그리는데, x와 y 위치에 그린다.
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)
    pygame.display.flip()
    # 현재 눌려있는 키 상태를 가져옴
    keys = pygame.key.get_pressed()

    # 좌우 이동
    # 좌측은 speed 만큼 x 위치를 빼 준다.
    if keys[pygame.K_LEFT]:
        x -= speed
    # 우측은 speed 만큼 x 위치를 더해준다.
    if keys[pygame.K_RIGHT]:
        x += speed

    # 상하 이동
    # 위쪽은 speed 만큼 y 위치를 빼 준다.
    if keys[pygame.K_UP]:
        y -= speed
    # 위쪽은 speed 만큼 y 위치를 더해 준다.
    if keys[pygame.K_DOWN]:
        y += speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 60 프레임을 위해 추가
    clock.tick(60)