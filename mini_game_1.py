# import relational modules
import sys,pygame

pygame.init()   # Initialize pygame
size = width, height = 600, 400 # set variable "size"
speed = [1,1]   # Set variable "speed", the first element is the horizontal speed (left --> right), the secend elements is the longitudinal speed (top --> bottom)
BLACK = (0,0,0) # Set variable "BLACK"
screen = pygame.display.set_mode(size)  # Set the size of window as variable "size"
pygame.display.set_caption("Pygame Mini Game 1")    # Set the title of window
ball = pygame.image.load("intro_ball.gif")  # load the picture
ballrect = ball.get_rect()  # Using ".get_rect()" to get the rect object of the picture
# Properties of "rect":
    # Get the position of pictures' 4 boundaries: top, bottom, left, right.
    # Get the size of pictures: width, height.
fps = 300
fclock = pygame.time.Clock()    # Creating a "Clock" object
# Properties of Clock:
    # tick: Seting the ratio of refresh: Hz


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1]) # Moving the rect
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(BLACK)  # Fill the background as Black
    screen.blit(ball, ballrect) # Drawing the "ball" (picture) in the "ballrect" (object)
    pygame.display.update()
    fclock.tick(fps)
