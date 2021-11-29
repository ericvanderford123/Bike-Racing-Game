import pygame

pygame.init()

w,h =1500,750

window=pygame.display.set_mode((w,h))

start=True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start=False
            pygame.quit()
            quit()
