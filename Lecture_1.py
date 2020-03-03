# filename is: firstblood_2.py

# import zone
import pygame

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode([800, 600])

# loop: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
pygame.quit()



####

# filename is: firstblood_2.py

# import zone
import pygame

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode([800, 600])

screen.fill([255,255,255])

jpgFileName = "pho.jpg"
imgRect = pygame.image.load(jpgFileName)
screen.blit(imgRect,[0,0])

pygame.display.flip()
# loop: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
pygame.quit()
