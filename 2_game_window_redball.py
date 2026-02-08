import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Window") 

while True:
    pygame.draw.circle(screen, (255, 0, 0), (200, 200), 10) # 화면의 200, 200 위치에, RGB 값이 (255, 0, 0)인 반지름 10짜리 원을 그립니다
    pygame.display.flip() # 화면을 업데이트하여 원이 보이도록 함
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
