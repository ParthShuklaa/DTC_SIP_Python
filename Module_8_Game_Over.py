import pygame
import random
first_value = pygame.init()
#print(first_value)
#defining color in terns of tuple - collection
white=(255,255,255)
black = (0,0,0)
red = (255,0,0)
Screen_Width = 800
Screen_Height= 600
Screen_caption= "My first Snake game"
#creating Game Window
gameWindow = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption(Screen_caption)
gameWindow.fill(white)
pygame.display.update()
clock = pygame.time.Clock()

#rendering Font
font = pygame.font.SysFont(None,60)

#defining Score board
def text_Screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    pass
#Changing Snake Length
def plot_snake(gamewindow,black1,SnkList,Snake_Size1):
    for x,y in SnkList:
        pygame.draw.rect(gameWindow,black1,[x,y,Snake_Size1,Snake_Size1])

def gameloop():
    exit_game = False
    game_over = False
    Snake_x = 30
    Snake_y = 40
    Snake_Size = 10
    Speed = 5
    # Defining Snake Size
    # Randomly genrating food Cordinates
    food_x = random.randrange(0, Screen_Width / 2)
    food_y = random.randrange(0, Screen_Height / 2)
    # Defining Velocity
    velocity_x = 0
    velocity_y = 0
    # Score variable
    Score = 0
    SnkLength = 1
    SnkList = []
    fps = 30  # frame per second
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_Screen("GAME OVER..!!! Press ESC to Continue",red,150,150)
            for event in pygame.event.get():
            #reading event
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
            # reading event
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = Speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -Speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -Speed
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = Speed
                        velocity_x = 0
            Snake_x += velocity_x
            Snake_y += velocity_y
            if abs(Snake_x - food_x )< 10 and abs(Snake_y - food_y)<10:
                Score += 5
                print("Score is" ,Score)

                food_x = random.randrange(0,Screen_Width/2)
                food_y = random.randrange(0,Screen_Height/2)
            gameWindow.fill(white)
            text_Screen("Score "+str(Score),red,5,5)
            pygame.draw.rect(gameWindow,black,[food_x,food_y,Snake_Size,Snake_Size])

            head =[]
            head.append(Snake_x)
            head.append(Snake_y)
            SnkList.append(head)
            print(SnkList)
            if len(SnkList)>SnkLength:
                del SnkList[0]

            plot_snake(gameWindow,black,SnkList,Snake_Size)
            if head in SnkList[ : -1]:
                game_over = True
            if (Snake_x<0) or (Snake_y <0) or (Snake_x>Screen_Width) or (Snake_y>Screen_Height):
                game_over = True
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

gameloop()

