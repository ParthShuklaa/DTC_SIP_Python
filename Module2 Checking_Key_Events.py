import pygame
first_value = pygame.init()
#print(first_value)

#creating Game Window
gameWindow = pygame.display.set_mode((400,400))
pygame.display.set_caption("My First Game Window")
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have Pressed Right Arrow key... ")

            if event.key == pygame.K_LEFT:
                print("You have Pressed Left Arrow Key..... ")

pygame.quit()
quit()

