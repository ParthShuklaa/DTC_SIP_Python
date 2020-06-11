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
#rendering Font
font = pygame.font.SysFont(None,60)

#defining Score board
def text_Screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
    pass
#Defining Snake Size
Snake_x = 30
Snake_y = 40
Snake_Size = 10
exit_game = False
game_over = False
Speed = 5
#Randomly genrating food Cordinates
food_x = random.randrange(0,Screen_Width/2)
food_y = random.randrange(0,Screen_Height/2)
#Defining Velocity
velocity_x = 0
velocity_y = 0
#Score variable
Score = 0

fps = 30 #frame per second
clock = pygame.time.Clock()
SnkLength = 1
SnkList = []
#Changing Snake Length
def plot_snake(gamewindow,black1,SnkList,Snake_Size1):
    for x,y in SnkList:
        pygame.draw.rect(gameWindow,black1,[x,y,Snake_Size1,Snake_Size1])

#Game loop
while not exit_game:
    for event in pygame.event.get():
        #reading event
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
    head =[]
    head.append(Snake_x)
    head.append(Snake_y)
    SnkList.append(head)
    print(SnkList)
    if len(SnkList)>SnkLength:
        del SnkList[0]

    plot_snake(gameWindow,black,SnkList,Snake_Size)

    #pygame.draw.rect(gameWindow,red,[Snake_x,Snake_y,Snake_Size,Snake_Size])





    pygame.draw.rect(gameWindow,black,[food_x,food_y,Snake_Size,Snake_Size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

