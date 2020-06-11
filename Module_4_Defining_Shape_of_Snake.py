import pygame
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
pygame.display.update()

gameWindow.fill(white)
pygame.display.update()
#Defining Snake Size
Snake_x = 30
Snake_y = 40
Snake_Size = 10
exit_game = False
game_over = False

fps = 30 #frame per second
clock = pygame.time.Clock()

#Game loop
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have Pressed Right Arrow key... ")
                Snake_x += 5
            if event.key == pygame.K_LEFT:
                print("You have Pressed Left Arrow Key..... ")
                Snake_x -= 5

        pygame.draw.rect(gameWindow,red,[Snake_x,Snake_y,Snake_Size,Snake_Size])
        pygame.display.update()
        clock.tick(fps)


pygame.quit()
quit()

