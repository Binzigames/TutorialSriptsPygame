import pygame
import sys

ScreenX = 500
ScreenY = 500


Screen = pygame.display.set_mode ((ScreenX , ScreenY))
pygame.display.set_caption("Моє Перше Вікно!")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()