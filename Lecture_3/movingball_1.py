import pygame,sys

pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
WHITE = 255,255,255
ball_x = 100
ball_y = 100
ball_speed_x = 2
ball_speed_y = 2

screen.fill(WHITE)

gifFileName = 'intro_ball.gif'
ballRect = pygame.image.load(gifFileName)
screen.blit(ballRect,(ball_x,ball_y))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(20)

    # eraze the last the image
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,111,111],0)

    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
    if ball_x < 0 or ball_x > width-111:
        ball_speed_x = -ball_speed_x
    if ball_y < 0 or ball_y > height-111:
        ball_speed_y = -ball_speed_y

    screen.blit(ballRect,[ball_x,ball_y])
    pygame.display.update()
