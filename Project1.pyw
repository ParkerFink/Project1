import pygame


pygame.init()

windowWidth = 400
windowHeight = 400
screen = pygame.display.set_mode([windowHeight,windowHeight])


playerX = 200
playerY = 200
character = pygame.image.load("Textures/temp_character.png")
def player(x,y):
    screen.blit(character, (x, y))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(playerX, playerY)
    pygame.display.update()
