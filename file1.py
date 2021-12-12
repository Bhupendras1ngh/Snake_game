import pygame
x = pygame.init()
# Creating window
game_window  =pygame.display.set_mode((1200 ,500))
pygame.display.set_caption("First Game")
# game specific variable
exit_game = False
game_over = False
# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed right arrow key")

-
pygame.quit()
quit()


