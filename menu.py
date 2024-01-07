import pygame
import sys
from load_image import load_image
from buttons import Button
from transition import transition
from const import *

pygame.init()

size = WIDTH, HEIGHT = 1024, 704
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sensei Rescuing')
clock = pygame.time.Clock()

imgSI = load_image(bg1)
bgSI = pygame.transform.scale(imgSI, (imgSI.get_width() * 2, imgSI.get_height() * 2))

cross_btn = Button(WIDTH - 40, 10, 32, 32, "buttons\cross.png", "",
                   "data\sounds\menu-button-sound.mp3")

cursor = load_image('cursor.png')
pygame.mouse.set_visible(False)


def main_menu():
    # pygame.mixer.music.load("data\sounds\menu-sound.mp3")
    # pygame.mixer.music.play(-1)

    img = load_image('backgrounds\main-menu-bg.png')
    bg = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))

    start_btn = Button(WIDTH - 265, 168, 190, 80, "buttons\start-btn.png", "buttons\hover-start-btn.png",
                       "data\sounds\menu-button-sound.mp3")
    settings_btn = Button(WIDTH - 265, 248, 190, 80, "buttons\settings-btn.png", "buttons\hover-settings-btn.png",
                          "data\sounds\menu-button-sound.mp3")
    info_btn = Button(WIDTH - 265, 328, 190, 80, "buttons\info-btn.png", "buttons\hover-info-btn.png",
                      "data\sounds\menu-button-sound.mp3")
    exit_btn = Button(WIDTH - 265, 408, 190, 80, "buttons\exit-btn.png", "buttons\hover-exit-btn.png",
                      "data\sounds\menu-button-sound.mp3")

    buttons = [start_btn, settings_btn, info_btn, exit_btn]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.USEREVENT and event.button == exit_btn):
                print('game quit | exit-btn tapped')
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_btn:
                print('start-btn tapped')
                transition()
                levels_menu()

            if event.type == pygame.USEREVENT and event.button == settings_btn:
                print('settings-btn tapped')
                transition()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == info_btn:
                print('info-btn tapped')
                transition()
                info_menu()

            for button in buttons:
                button.handle_event(event)

        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def settings_menu():

    imgSet = load_image('backgrounds\settings-bg.png')
    bgSet = pygame.transform.scale(imgSet, (imgSet.get_width() * 2, imgSet.get_height() * 2))

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bgSet, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('game quit')
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                print('cross-btn tapped from settings')
                transition()
                running = False

            cross_btn.handle_event(event)

        cross_btn.check_hover(pygame.mouse.get_pos())
        cross_btn.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def levels_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bgSI, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('game quit')
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                print('cross-btn tapped from levels')
                transition()
                running = False

            cross_btn.handle_event(event)

        cross_btn.check_hover(pygame.mouse.get_pos())
        cross_btn.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def info_menu():

    imgInf = load_image(backgrounds['info-bg'])
    bgInf = pygame.transform.scale(imgInf, (imgInf.get_width() * 2, imgInf.get_height() * 2))

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bgInf, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('game quit')
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                print('cross-btn tapped from info')
                transition()
                running = False

            cross_btn.handle_event(event)

        cross_btn.check_hover(pygame.mouse.get_pos())
        cross_btn.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


main_menu()
