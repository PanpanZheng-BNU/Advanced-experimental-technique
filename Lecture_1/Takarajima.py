# Import modules
import sys,pygame

pygame.init()   # Initialize pygame
WHITE = 255,255,255   # Set variable "WHITE"
size = width, height = 620, 349   # Set variable "size"
screen = pygame.display.set_mode(size)  # Set the size of window
pygame.display.set_caption("新宝島　takarajima")    # Set title of window
bg = pygame.image.load("test.jpg") # Load picture file
pygame.mixer.music.load("01 新宝島.flac")  # Load music file
pygame.mixer.music.set_volume(1)    # Set the volume of music
pygame.mixer.music.play()   # Starting to play music

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    screen.blit(bg, (0,0))
    pygame.display.update()
