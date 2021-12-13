import pygame
import random
from random import randint

pygame.init()

w,h =1200,750

window=pygame.display.set_mode((w,h))
pygame.display.set_caption("Bicycle Racing Game")
icon= pygame.image.load("data/bicycle racing.png")
pygame.display.set_icon(icon)
background=pygame.image.load('data/bike backdrop.png')
background = pygame.transform.scale(background, (1200, 750))

bike1=pygame.image.load('data/bike2.png')
bike1 = pygame.transform.scale(bike1, (200, 150))
bike2=pygame.image.load('data/bike1.png')
bike2 = pygame.transform.scale(bike2, (200, 150))

finishingline = pygame.image.load("data/finishline.png").convert()
finishingline = finishingline.subsurface(0, 360, 800, 400)
finishingline = pygame.transform.rotate(finishingline, 90)
finishingline = pygame.transform.scale(finishingline, (500, 1000))
startingline = pygame.image.load("data/startingline.png").convert()
startingline = pygame.transform.scale(startingline, (220, 340))
#position of the first bike
b1x=0
b1y=100
b1change=0

#position of the second bike
b2x=0
b2y=400
b2change=0
x,y=1060,-50
def player(x,y):
    window.blit(bike1,(x,y))
    window.blit(bike2,(x,y))
def finish():
    window.blit(finishingline, (x,y))
def starting():
    window.blit(startingline, (0, 0))
start=True

while start:
    window.blit(background, (0,0))
    finish()
    starting()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            quit()


    move1=random.randint(0,4)
    move2 = random.randint(0, 4)
    b1change=move1
    b2change = move2
    b1x= b1x+ b1change
    b2x = b2x + b2change
    player(b1x,b1y)
    player(b2x,b2y)

    pygame.display.update()



