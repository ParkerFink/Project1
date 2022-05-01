import pygame


pygame.init()

windowWidth = 800
windowHeight = 500
screen = pygame.display.set_mode([windowHeight,windowHeight])


playerX = 100
playerY = 100

character = pygame.image.load('Textures/temp_character.png')
def player():
    screen.blit(character, (playerX, playerY))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()
