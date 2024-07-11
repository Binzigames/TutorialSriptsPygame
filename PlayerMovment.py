import pygame
import sys

WindowX = 400
WindowY = 400

screen = pygame.display.set_mode((WindowX,WindowY))
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


player_size = 30
player_pos = [WindowX // 2, WindowY // 2]
player_speed = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed


    screen.fill(WHITE)


    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))


    pygame.display.flip()


    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()