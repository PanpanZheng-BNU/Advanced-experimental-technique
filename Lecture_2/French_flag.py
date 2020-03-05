# French Flag
import pygame,sys

pygame.init()

screen = pygame.display.set_mode((600,400))

screen.fill((255,255,255))

pygame.draw.rect(screen,(0,0,255),(0,0,200,400),0)
pygame.draw.rect(screen,(255,0,0),(400,0,200,400),0)
# pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen,"France.jpg")
            pygame.quit()
            sys.exit()

    pygame.display.update()
