import screeninfo
import pygame
import fileManager

size = (1024, 704)
fullsize = tuple(map(int, '='.join(
    (str(screeninfo.get_monitors()).lstrip('[Monitor(').rstrip(')]').split(', '))[2: 4]).split('=')[1::2]))
fullsize = (1920, 1080)

k = 1.5
otstupx = (1920 - 1024 * k) // 2
otstupy = (1080 - 704 * k) * k // 2

fullscreen = fileManager.fullscreenImport()

if fullscreen:
    width, height = fullsize
    screen = pygame.display.set_mode(fullsize, pygame.FULLSCREEN)
else:
    width, height = size
    screen = pygame.display.set_mode(size)
