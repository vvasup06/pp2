import pygame
import time
import random
 
pygame.init()
 
# ЦВЕТА
yellow = (255, 255, 102)
red = (213, 50, 80)
blue = (0, 0, 255)
green = (0,255,0)
white = (255, 255, 255)
black = (0, 0, 0)

# РАЗМЕР ПОЛОТНА
dis_width = 600
dis_height = 400


FPS = 60
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
#РАЗМЕР ЗМЕЙКИ 
snake_block = 10
snake_speed = 15
 
# ТЕКСТ
font_style = pygame.font.SysFont("freesansbold.ttf", 40)
score_font = pygame.font.SysFont("freesansbold.ttf", 15)
level_font = pygame.font.SysFont("freesansbold.ttf", 15)

# ФУНКЦИЯ УРОВНЯ
def lever_score(level):
    value = score_font.render("Your level: " + str(level), True, black)
    screen.blit(value, [10, 25])
 
# ФУНКЦИЯ ОЧКОВ
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [10, 10])
 
 
# GRAPH SNAKE
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])
 
# MESSAGE
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [30, 200])
 
# THE MAIN FUNCTION OF GAME
def gameLoop():
    game_over = False
    game_exit = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    level = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    # УПРАВЛЕНИЕ ПАУЗЫ
    while not game_over:
        # ОСНОВНОЕ НАЧАЛО
        while game_exit == True:
            global snake_speed
            screen.fill(white)
            message("Game Over! Press S-Play Again or Q-Exit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            # команды перезапуска игры или выхода
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_exit = False
                    if event.key == pygame.K_s:
                        snake_speed = 10
                        gameLoop()

        # УПРАВЛЕНИЕ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0
        # СТОЛКНОВЕНИЕ С СТЕНОЙ
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_exit = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(white)
        # РИСОВАНИЕ ЯБЛОКА
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        # ДОБАВЛЕНИЕ НОВЫХ ЧАСТЕЙ
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        # УДАЛЕНИЕ СТАРЫХ
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_exit = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        lever_score(level)
        if Length_of_snake >= 11:
            level = 2
            snake_speed = 25
        

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - 100) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 100) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()