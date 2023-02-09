import pygame
import random
import os

pygame.init()
pygame.mixer.init()


#color intialization


white = (255,255,255)
red =   (255,0,0)
black = (0,0,0)
blue = (0,0,255)


screen_width = 900
screen_height = 600


game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")
pygame.display.update()


font = pygame.font.SysFont(None,55)


bgimg = pygame.image.load('snks.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()



gmover = pygame.image.load('gameover.jpg')
gmover = pygame.transform.scale(gmover, (screen_width,screen_height)).convert_alpha()


def plot_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color, [x,y, snake_size, snake_size])


def text_score(text,color,x,y):
    screen_text= font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

#game variable

exit_game = False
exit_over = False
snake_x = 45
snake_y = 55
snake_size = 10
velocity_x = 0
velocity_y = 0
food_x = random.randint(0,screen_width/1.5)
food_y = random.randint(0,screen_height/1.5)
score = 0
snake_list=[]
snake_lenght=1
clock = pygame.time.Clock()
fps = 60
a=[0,0]
b=[0,600]


def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((250,245,225))
        game_window.blit(bgimg, (0, 0))
        text_score("Welcome to Snakes game",black,260,250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('baground.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(60)

#code

def game_loop():
    init_velocity = 2
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width / 2)
    food_y = random.randint(0, screen_height /2 )
    score = 0
    snake_list = []
    snake_lenght = 1
    clock = pygame.time.Clock()
    fps = 60
    a = [0, 0]
    b = [0, 600]
    if not os.path.exists("higscore.txt"):
        with open("higscore.txt","w") as f:
            f.write("0")
    with open("higscore.txt", "r") as f:
        Highscore = f.read()
    while not exit_game:
        if game_over:
            with open("higscore.txt", "w") as f:
                f.write(str(Highscore))
            game_window.fill(white)
            game_window.blit(gmover,(0,0))
            #text_score("Game over: Press enter to continue",red,108,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

            snake_x = velocity_x + snake_x
            snake_y = velocity_y + snake_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                pygame.mixer.music.load('Beep.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randint(0, screen_width / 1.5)
                food_y = random.randint(0, screen_height / 1.5)
                snake_lenght += 5
                if score>int(Highscore):
                    Highscore=score


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_lenght:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load('Explosion.mp3')
                pygame.mixer.music.play()
                game_over = True
            if snake_x < 10 or snake_x > 890 or snake_y < 10 or snake_y > 590:
                pygame.mixer.music.load('Explosion.mp3')
                pygame.mixer.music.play()
                game_over = True


            game_window.fill(white)

            text_score("Score:" + str(score) , red, 5, 5)
            text_score( "Higscore is " + str(Highscore), red, 5, 50)
            plot_snake(game_window, black, snake_list, snake_size)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(game_window, black, a, b, 10)
            pygame.draw.line(game_window, black, a, [900, 0], 10)
            pygame.draw.line(game_window, black, [0, 600], [900, 600], 10)
            pygame.draw.line(game_window, black, [900, 0], [900, 600], 10)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
