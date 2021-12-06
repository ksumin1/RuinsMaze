import pygame
import minigame
import os,random
class Start:
    def __init__(self):
        # pygame 초기화
        pygame.init()
        # screen 객체 저장 / 창 설정
        self.screen = pygame.display.set_mode((955, 955))
        pygame.display.set_caption("Ruins Maze")
        # 이미지 불러오기
        self.start_bg_Img = pygame.image.load("img/startImg.png")
        # 폰트
        font = pygame.font.Font('img/DungGeunMo.ttf',40)
        self.startTxT = font.render('space를 누르면 시작!', True, (255, 255, 255))
        # 실행
        self.start()

    def start(self):
        while True:
            # 배경그리기
            self.screen.blit(self.start_bg_Img, (0, 0))
            # 폰트
            self.screen.blit(self.startTxT, (300,700))
            for event in pygame.event.get():  # 이벤트가 발생했는지 여부
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인지
                    pygame.quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]: # 스페이스바가 눌렸을때 게임 시작작
               Main()
            pygame.display.update()
        # pygame 종료
        pygame.quit()


class Main:
    def __init__(self):
        # pygame 초기화
        pygame.init()
        # screen 객체 저장 / 창 설정
        self.screen = pygame.display.set_mode((950, 950))
        pygame.display.set_caption("Ruins Maze")
        # 미니게임 불러오기

        # 이미지 불러오기
        self.CharacterImg = pygame.image.load("img/character(front).png")
        self.MapImg = pygame.image.load("img/map.png")
        # 캐릭터 이동 좌표
        self.to_x = 0
        self.to_y = 0
        self.character_x_position = 20
        self.character_y_position = 0
        # 캐릭터 이미지
        self.images_left = [pygame.image.load("img/character(left).gif"), pygame.image.load("img/character(left)_2.png"), pygame.image.load("img/character(left).gif"), pygame.image.load("img/character(left)_3.png")]
        self.images_right = [pygame.image.load("img/character(right).gif"), pygame.image.load("img/character(right)_2.png"), pygame.image.load("img/character(right).gif"), pygame.image.load("img/character(right)_3.png")]
        self.images_front = [pygame.image.load("img/character(front).png"), pygame.image.load("img/character(front)_2.png"), pygame.image.load("img/character(front).png"), pygame.image.load("img/character(front)_3.png")]
        self.images_behind = [pygame.image.load("img/character(behind).gif"), pygame.image.load("img/character(behind)_2.png"), pygame.image.load("img/character(behind).gif"), pygame.image.load("img/character(behind)_3.png")]
        self.state = 0
        self.direction = 'front'
        # 미로 맵
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():  # 이벤트가 발생했는지 여부
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인지
                    pygame.quit()

                if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
                    if event.key == pygame.K_LEFT:  # 왼쪽
                        self.CharacterImg = self.images_left[0]
                        self.direction = 'left'
                        self.state = 1
                        self.to_x -= 3

                    elif event.key == pygame.K_RIGHT:  # 오른쪽
                        self.CharacterImg = self.images_right[0]
                        self.direction = 'right'
                        self.state = 1
                        self.to_x += 3
                    elif event.key == pygame.K_UP:  # 위
                        self.CharacterImg = self.images_behind[0]
                        self.direction = 'front'
                        self.state = 1
                        self.to_y -= 3
                    elif event.key - - pygame.K_DOWN:  # 아래
                        self.CharacterImg = self.images_front[0]
                        self.direction = 'behind'
                        self.state = 1
                        self.to_y += 3

                if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0
                # 캐릭터가 창 밖으로 나가지 못하게 하기
                if self.character_x_position < 0:
                    self.character_x_position = 0
                elif self.character_x_position > 855:
                    self.character_x_position = 855

                if self.character_y_position < 0:
                    self.character_y_position = 0
                elif self.character_y_position > 855:
                    self.character_y_position = 855

            # 배경그리기
            self.screen.blit(self.MapImg, (0, 0))
            # 캐릭터 움직임 적용
            if self.map[(self.character_x_position+45)//45][(self.character_y_position+45)//45] == 1:
                self.character_x_position = self.character_x_position
                self.character_y_position = self.character_y_position
            elif self.map[(self.character_x_position+45)//45][(self.character_y_position+45)//45] == 0:
                self.character_x_position += self.to_x
                self.character_y_position += self.to_y
            elif self.map[self.character_x_position/45][self.character_y_position/45] == 3:
                pass
            elif self.map[self.character_x_position/45][self.character_y_position/45] == 4:
                break
            # 캐릭터 그리기
            self.screen.blit(self.CharacterImg, (self.character_x_position, self.character_y_position))
            # 게임화면 지속적으로
            pygame.display.flip()
        # pygame 종료
        pygame.quit()



if __name__ == '__main__':
    Start()