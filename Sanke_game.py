import pygame
import random
import os




pygame.init()

#colors
white = (255 ,255 ,255)
red = (255 ,0 ,0)
black = (0 ,0 ,0)
pink  = (255 ,20 ,147)
magneta = (255 ,0 ,255)
blue = (0 ,0 ,255)

#creating window size
width = 900
height = 600
game_window = pygame.display.set_mode((width ,height))

# creating walpaper Image
bgimage  =pygame.image.load("wallpaper2.jpg")
bgimage  = pygame.transform.scale(bgimage ,(width , height)).convert_alpha()


bgimage2  =pygame.image.load("start_wallpaper.jpg")
bgimage2  = pygame.transform.scale(bgimage2 ,(width , height)).convert_alpha()

#title
pygame.display.set_caption("Snake_Game_Bhupendra")
pygame.display.update()




#timer
clock = pygame.time.Clock()

#for showing score on the screem
font = pygame.font.SysFont(None ,55)
def screen_score(text ,color  ,x ,y):
    screen_text =font.render(text ,True ,color)
    game_window.blit(screen_text , [x,y])


def  plot_snake(game_window  , color ,snake_list,snake_size):
    for x ,y in snake_list:
        pygame.draw.rect(game_window  ,color ,[x ,y , snake_size , snake_size])

# Game start Interface

def welcome():
    exit_game = False

    pygame.mixer.init()
    pygame.mixer.music.load('g_start.wav')
    pygame.mixer.music.play()
    while not exit_game:
        game_window.fill((220 ,240 ,220))
        game_window.blit(bgimage2, (0, 0))
        screen_score("Welcome to Bhupendra's Snake Game "  ,pink , 110 ,20)
        screen_score("Press Space Bar To Play ", red, 200, 370)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.init()
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(60)


#game loop
def game_loop():
    # game specific varible
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    init_velocity = 3
    food_x = random.randint(20, width / 2)
    food_y = random.randint(20, height / 2)
    score = 0
    snake_size = 10
    fps = 60  # frame Per Second


    # check if high score  file exist
    if( not os.path.exists("high_score.txt.html")):
        with open("high_score.txt.html" ,"w") as f:
            f.write("0")

    with open("high_score.txt.html", "r") as f:
        high_score = f.read()

    pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

    while not exit_game:
        if game_over:
            with open("high_score.txt.html", "w") as f:
                f.write(str(high_score))

            game_window.fill(white)
            screen_score("Game Over ! Press Enter to Continue" , red ,130 ,200)
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y =0

                    if event.key == pygame.K_LEFT:
                        velocity_x =-init_velocity
                        velocity_y =0
                    if event.key == pygame.K_UP:
                        velocity_y =-init_velocity
                        velocity_x =0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x= 0

                    if event.key == pygame.K_q:
                        score += 5


            snake_x = snake_x + velocity_x
            snake_y =snake_y + velocity_y

            # snake Eat food and score increment and generating the new value of food
            if abs(snake_x -food_x) <6 and abs(snake_y -food_y):
                score =score+10
                #print("Score"  ,score*10)


                food_x = random.randint(20, width / 2)
                food_y = random.randint(20, height / 2)
                snake_length += 5
                if score >int(high_score):
                    high_score = score
            # here we color our snake game background by white color
            game_window.fill(white)
            game_window.blit(bgimage , (0 ,0))
            # score showing on  snake game scree
            screen_score("Score: " + str(score) +"                                      High_score: " +str(high_score), red, 5, 5)




            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) >snake_length:
                del snake_list[0]

            # if the coordinates of head is equals to any cordinates of snakes list then Print GAme Over
            if head in snake_list[:-1]:
                game_over = True

                pygame.mixer.init()
                pygame.mixer.music.load('gover.wav')
                pygame.mixer.music.play()
            if snake_x <0 or snake_x > width  or snake_y <0 or snake_y >height:
                game_over = True

                pygame.mixer.init()
                pygame.mixer.music.load('gover.wav')
                pygame.mixer.music.play()
                #print("Game_Over")

            #snake food color

            plot_snake(game_window, magneta, snake_list, snake_size)
            pygame.draw.rect(game_window, blue, [food_x, food_y, snake_size, snake_size])

            # now we define the head of snake by black color and its position on x and y axis
            #pygame.draw.rect(game_window  ,black ,[snake_x ,snake_y , snake_size , snake_size])

        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome()
