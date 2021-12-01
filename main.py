import pygame

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
finishingline=pygame.image.load('data/finishline.png')
finishingline = pygame.transform.rotate(finishingline, 90)
finishingline = pygame.transform.scale(finishingline, (600, 1000))

#position of the first bike
b1x=0
b1y=100

#position of the second bike
b2x=0
b2y=400
x,y=900,-50
def player(x,y):
    window.blit(bike1,(x,y))
    window.blit(bike2,(x,y))
def finish():
    window.blit(finishingline, (x,y))
start=True

while start:
    window.blit(background, (0,0))
    finish()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            quit()


    player(b1x,b1y)
    player(b2x,b2y)
    pygame.display.update()
    
