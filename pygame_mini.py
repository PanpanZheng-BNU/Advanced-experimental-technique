import sys,pygame   # Import the modules

pygame.init()       # Initialize the window of pygame
screen = pygame.display.set_mode((600,400)) # Setting the width and height of the window
pygame.display.set_caption("Pygame 最小开发框架") # Setting the title as "Pygame 最小开发框架"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
