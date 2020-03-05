
# Japan Flag
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400))

screen.fill((255,255,255))

pygame.draw.circle(screen,[200,0,0],[300,200],100,0)

pygame.draw.circle([Surface], [color], [pos], [radius], [width])
# pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen,"Japan.jpg")
            pygame.quit()
            sys.exit()

    pygame.display.update()
