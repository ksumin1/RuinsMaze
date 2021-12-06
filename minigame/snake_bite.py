import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN,\
    K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect
# 타임안에 살아남거나 일정이상 몸집 키우면 클리어
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("timer")
FPSCLOCK = pygame.time.Clock()
font = pygame.font.Font('DungGeunMo.ttf',40)

total_time = 30
start_timer = pygame.time.get_ticks()

FOODS = []
SNAKE = []
(W, H) = (20, 20)

def add_food():
    # 임의의 장소에 먹이를 배치
    while True:
        pos = (random.randint(0, W-1), random.randint(0, H-1))
        if pos in FOODS or pos in SNAKE:
            continue
        FOODS.append(pos)
        break

def move_food(pos):
    # 먹이를 다른 장소로 이동
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()

def paint(message):
    # 화면 전체 그리기
    screen.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(screen, (0, 255, 0),
                            Rect(food[0]*30, food[1]*30, 30, 30))
    for body in SNAKE:
        pygame.draw.rect(screen, (0, 255, 255),
                         Rect(body[0]*30, body[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(screen, (64, 64, 64), (index * 30, 0),
                         (index*30, 600))
        pygame.draw.line(screen, (64, 64, 64), (0, index * 30),
                         (600, index*30))
    if message != None:
        screen.blit(message, (150, 300))
    pygame.display.update()

def main():
    myfont = pygame.font.SysFont(None, 80)
    key = K_DOWN
    message = None
    game_over = False
    SNAKE.append((int(W/2), int(H/2)))
    for _ in range(10):
        add_food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() - start_timer) / 1000
        # 타이머
        timer = font.render("timer: " + str(int(total_time - elapsed_time)), True, (255, 255, 255))
        # 경과 시간 표시
        screen.blit(timer, (10, 10))

        if total_time - elapsed_time <= 0:
            print("타임아웃")
            pygame.quit()

        if not game_over:
            if key == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif key == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif key == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif key == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)

            if head in SNAKE or \
               head[0] < 0 or head[0] >= W or \
               head[1] < 0 or head[1] >= H:
                message = myfont.render("Game Over!",
                                        True, (255, 255, 0))
                game_over = True

            SNAKE.insert(0, head)
            if head in FOODS:
                move_food(head)
            else:
                SNAKE.pop()

        paint(message)
        FPSCLOCK.tick(5)

if __name__ == '__main__':
    main()
