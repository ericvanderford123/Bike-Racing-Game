import pygame

pygame.init()

w,h =1200,750

window=pygame.display.set_mode((w,h))
pygame.display.set_caption("Bicycle Racing Game")
icon= pygame.image.load("data/bicycle racing.png")
pygame.display.set_icon(icon)
background=pygame.image.load('data/bike backdrop.png')
background = pygame.transform.scale(background, (1200, 750))
start=True

while start:
    window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            quit()
    pygame.display.update()
    
