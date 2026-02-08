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

ball_1_x, ball_2_x, ball_3_x, ball_4_x, ball_5_x = 100, 150, 200, 250, 300
ball_1_y, ball_2_y, ball_3_y, ball_4_y, ball_5_y = 100, 100, 100, 100, 100
ball_1_x_speed, ball_2_x_speed, ball_3_x_speed, ball_4_x_speed, ball_5_x_speed = 1, 2, 3, 4, 5
ball_1_y_speed, ball_2_y_speed, ball_3_y_speed, ball_4_y_speed, ball_5_y_speed = 1, 2, 3, 4, 5
game_over = False
font = pygame.font.SysFont(None, 60)

def is_collision(x1, y1, x2, y2, radius):
    dx = x1 - x2
    dy = y1 - y2
    distance = dx*dx + dy*dy
    return distance < (radius * 2) * (radius * 2)

while True:
    # 화면을 검정 화면으로 초기화 한다.
    screen.fill((0, 0, 0))
    # 공을 그리는데, x와 y 위치에 그린다.
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)

    pygame.draw.circle(screen, (0, 0, 255), (ball_1_x, ball_1_y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (ball_2_x, ball_2_y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (ball_3_x, ball_3_y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (ball_4_x, ball_4_y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (ball_5_x, ball_5_y), 10)

    # 벽과의 충돌 계산
    if ball_1_x < 10 or ball_1_x > 800 - 10:
        ball_1_x_speed *= -1
    if ball_1_y < 10 or ball_1_y > 600 - 10:
        ball_1_y_speed *= -1
    if ball_2_x < 10 or ball_2_x > 800 - 10:
        ball_2_x_speed *= -1
    if ball_2_y < 10 or ball_2_y > 600 - 10:
        ball_2_y_speed *= -1
    if ball_3_x < 10 or ball_3_x > 800 - 10:
        ball_3_x_speed *= -1
    if ball_3_y < 10 or ball_3_y > 600 - 10:
        ball_3_y_speed *= -1
    if ball_4_x < 10 or ball_4_x > 800 - 10:
        ball_4_x_speed *= -1
    if ball_4_y < 10 or ball_4_y > 600 - 10:
        ball_4_y_speed *= -1
    if ball_5_x < 10 or ball_5_x > 800 - 10:
        ball_5_x_speed *= -1
    if ball_5_y < 10 or ball_5_y > 600 - 10:
        ball_5_y_speed *= -1

    if not game_over:
        if is_collision(x, y, ball_1_x, ball_1_y, 10):
            game_over = True
        if is_collision(x, y, ball_2_x, ball_2_y, 10):
            game_over = True
        if is_collision(x, y, ball_3_x, ball_3_y, 10):
            game_over = True
        if is_collision(x, y, ball_4_x, ball_4_y, 10):
            game_over = True
        if is_collision(x, y, ball_5_x, ball_5_y, 10):
            game_over = True
    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (250, 250))

    ball_1_x += ball_1_x_speed
    ball_2_x += ball_2_x_speed
    ball_3_x += ball_3_x_speed
    ball_4_x += ball_4_x_speed
    ball_5_x += ball_5_x_speed
    ball_1_y += ball_1_y_speed
    ball_2_y += ball_2_y_speed
    ball_3_y += ball_3_y_speed
    ball_4_y += ball_4_y_speed
    ball_5_y += ball_5_y_speed
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