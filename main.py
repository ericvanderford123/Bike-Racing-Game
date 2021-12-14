import random

import pygame

import time



pygame.init()

w,h =1200,750
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bw,bh=1200,750
bsx,bsy=200,150

window=pygame.display.set_mode((w,h))
pygame.display.set_caption("Bicycle Racing Game")
icon= pygame.image.load("data/bicycle racing.png")
pygame.display.set_icon(icon)
background=pygame.image.load('data/bike backdrop.png')
background = pygame.transform.scale(background, (bw, bh))
clock = pygame.time.Clock()

bike1=pygame.image.load('data/bike2.png')
bike1 = pygame.transform.scale(bike1, (bsx, bsy))
bike2=pygame.image.load('data/bike1.png')
bike2 = pygame.transform.scale(bike2, (bsx, bsy))

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
x,y=1040,-50

def player(x,y):
    window.blit(bike1,(x,y))
    window.blit(bike2,(x,y))
def finish():
    window.blit(finishingline, (x,y))
def starting():
    window.blit(startingline, (0, 0))
gamestate='Running'
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((w/2),(h/2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(4)
def win1():
    message_display('Player 1 Wins')
def win2():
    message_display('Player 2 Wins')


while (gamestate == 'Running' ) or (gamestate == 'notrunning1')or (gamestate == 'notrunning2'):
    window.blit(background, (0,0))
    finish()
    starting()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('gamesate quit')
            gamestate = 'quit'
            pygame.quit()
            quit()


    if gamestate == 'Running':
        move1=random.randint(0,4)
        move2 = random.randint(0, 4)
        b1x= b1x+ move1
        b2x = b2x + move2
        player(b1x,b1y)
        player(b2x,b2y)

        if b1x >=850:
            print('gamestate notrunning1')
            gamestate='notrunning1'
        if b2x >= 850:
            print('gamestate notrunning2')
            gamestate = 'notrunning2'
    if gamestate =='notrunning1':
        win1()
    if gamestate =='notrunning2':
        win2()

    clock.tick(60)
    pygame.display.update()



