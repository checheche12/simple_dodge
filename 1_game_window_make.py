import sys              # 프로그램을 종료하기 위해 sys.exit()를 사용하기 위한 모듈
import pygame           # 게임 화면, 입력, 이벤트 처리를 위한 pygame 라이브러리

pygame.init()           # pygame에서 사용하는 모든 기능을 초기화 (이 줄이 없으면 pygame 기능들이 정상 동작하지 않음)
screen = pygame.display.set_mode((800, 600)) # 가로 800, 세로 600 크기의 게임 창을 생성 screen 변수는 우리가 그림을 그릴 도화지
pygame.display.set_caption("Pygame Window") # 게임 창의 제목(상단 바에 표시되는 텍스트)을 설정

while True: # 게임 루프 게임은 한 번 실행되고 끝나는 것이 아니라 계속 반복되면서 동작해야 하므로 무한 반복 사용. 종료는 루프 안에서 시킨다.
    for event in pygame.event.get():  # 발생한 모든 이벤트를 하나씩 가져옴. 창 닫기, 키 입력, 마우스 입력 등
        if event.type == pygame.QUIT: # 만약 이벤트의 종류가 "창 닫기"라면
            pygame.quit() # pygame을 정상적으로 종료
            sys.exit()   # 프로그램 자체를 완전히 종료
