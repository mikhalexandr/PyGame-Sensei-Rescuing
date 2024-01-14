import pygame
import sys
import webbrowser
from load_image import load_image
from buttons import Button
from objects import Object
from transition import transition
from consts import *

pygame.init()

size = WIDTH, HEIGHT = 1024, 704
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sensei Rescuing')
clock = pygame.time.Clock()

imgSI = load_image(bg1)
bgSI = pygame.transform.scale(imgSI, (imgSI.get_width() * 2, imgSI.get_height() * 2))

cursor = load_image(r'objects\cursor-obj.png')
pygame.mouse.set_visible(False)

img = load_image(r'backgrounds\main-menu-bg.png')
bg = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))

checkPassing2 = True
checkPassingBoss = False


def main_menu():
    # pygame.mixer.music.load("data\sounds\menu-sound.mp3")
    # pygame.mixer.music.play(-1)

    title = Object(WIDTH // 2 - 886 // 2, 49, 886, 80, r"objects\menu-title-obj.png")

    start_btn = Button(WIDTH // 2 - 240 // 2, 186, 240, 100, r"buttons\start-btn.png",
                       r"buttons\hover-start-btn.png", r"data\sounds\menu-button-sound.mp3")
    settings_btn = Button(WIDTH // 2 - 240 // 2, 284, 240, 100, r"buttons\settings-btn.png",
                          r"buttons\hover-settings-btn.png", r"data\sounds\menu-button-sound.mp3")
    info_btn = Button(WIDTH // 2 - 240 // 2, 382, 240, 100, r"buttons\info-btn.png",
                      r"buttons\hover-info-btn.png", r"data\sounds\menu-button-sound.mp3")
    exit_btn = Button(WIDTH // 2 - 240 // 2, 480, 240, 100, r"buttons\exit-btn.png",
                      r"buttons\hover-exit-btn.png", r"data\sounds\menu-button-sound.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.USEREVENT and event.button == exit_btn):
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_btn:
                transition()
                levels_menu()

            if event.type == pygame.USEREVENT and event.button == settings_btn:
                transition()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == info_btn:
                transition()
                info_menu()

            for button in [start_btn, settings_btn, info_btn, exit_btn]:
                button.handle_event(event)

            title.handle_event(event)

        for button in [start_btn, settings_btn, info_btn, exit_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        title.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def settings_menu():
    title = Object(WIDTH // 2 - 626 // 2 - 50, 85, 626, 82, r"objects\settings-title-obj.png")
    field_audio = Object(WIDTH // 2 - 450, 200, 420, 430, r"objects\audio-field-obj.png")
    field_video = Object(WIDTH // 2 + 30, 200, 420, 430, r"objects\video-field-obj.png")
    fs_name = Object(WIDTH // 2 + 478 // 2 - 332 // 2, 330, 332, 75, r"objects\fullscreen-obj.png")
    sound_name = Object(WIDTH // 2 - 450 // 2 - 332 // 2 - 18, 470, 332, 35, r"objects\sound-obj.png")
    music_name = Object(WIDTH // 2 - 450 // 2 - 332 // 2 - 18, 334, 332, 35, r"objects\music-obj.png")

    cross_btn = Button(WIDTH - 229, 93, 67, 72, r"buttons\cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"data\sounds\menu-button-sound.mp3")
    fs_btn = Button(WIDTH // 2 + 478 // 2 - 136 // 2, 420, 136, 62, r"buttons\no-fullscreen-btn.png", r"buttons\fullscreen-btn.png",
                    r"data\sounds\menu-button-sound.mp3")
    music_slider_btn = Object(WIDTH // 2 - 450 // 2 - 385 // 2 - 18, 378, 385, 14, r"buttons\slider-btn.png")
    sound_slider_btn = Object(WIDTH // 2 - 450 // 2 - 385 // 2 - 18, 514, 385, 14, r"buttons\slider-btn.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                running = False

            for obj in [title, field_audio, field_video, fs_name, sound_name, music_name, music_slider_btn, sound_slider_btn]:
                obj.handle_event(event)

            cross_btn.handle_event(event)
            fs_btn.handle_event(event)

        for obj in [title, field_audio, field_video, fs_name, sound_name, music_name, music_slider_btn, sound_slider_btn]:
            obj.draw(screen)

        fs_btn.check_hover(pygame.mouse.get_pos())
        fs_btn.draw(screen)
        cross_btn.check_hover(pygame.mouse.get_pos())
        cross_btn.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def levels_menu():
    global checkPassing2, checkPassingBoss
    cross_btn = Button(WIDTH - 192, 93, 67, 72, r"buttons\cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"data\sounds\menu-button-sound.mp3")
    level1Button = Button(64, HEIGHT // 2 - 189 // 2 + 43, 144, 155, r"buttons\first-btn.png",
                          r"buttons\hover-first-btn.png", r"data\sounds\menu-button-sound.mp3")
    level2Button = Button(WIDTH // 2 - 73, HEIGHT // 2 - 189 // 2 + 43, 144, 155, r"buttons\second-btn.png",
                          r"buttons\hover-second-btn.png", r"data\sounds\menu-button-sound.mp3")
    levelBossButton = Button(WIDTH // 2 + 300, HEIGHT // 2 - 189 // 2 + 43, 144, 155, r"buttons\boss-btn.png",
                             r"buttons\hover-boss-btn.png", r"data\sounds\menu-button-sound.mp3")

    title = Object(WIDTH // 2 - 700 // 2 - 49, 85, 700, 82, r"objects\level-menu-title-obj.png")
    level1Field = Object(43, HEIGHT // 2 - 189 // 2 + 25, 186, 189, r"objects\start-level-field-obj.png")
    level2Field = Object(WIDTH // 2 - 269, HEIGHT // 2 - 189 // 2 + 25, 360, 189, r"objects\level-field-obj.png",
                         r"objects\hover-level-field-obj.png")
    levelBossField = Object(WIDTH // 2 + 104, HEIGHT // 2 - 189 // 2 + 25, 360, 189,
                            r"objects\level-field-obj.png", r"objects\hover-level-field-obj.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                running = False

            for obj in [title, level1Field, level2Field, levelBossField]:
                obj.handle_event(event)

            for button in [cross_btn, level1Button, level2Button, levelBossButton]:
                button.handle_event(event)

        for obj in [title, level1Field]:
            obj.draw(screen)

        level2Field.check_passing(checkPassing2)
        level2Field.draw(screen)

        levelBossField.check_passing(checkPassingBoss)
        levelBossField.draw(screen)

        for button in [cross_btn, level1Button, level2Button, levelBossButton]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def info_menu():
    cross_btn = Button(WIDTH - 218, 93, 67, 72, r"buttons\cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"data\sounds\menu-button-sound.mp3")
    github_left_btn = Button(WIDTH // 2 - 345, HEIGHT - 170, 67, 72, r"buttons\github-btn.png",
                             r"buttons\hover-github-btn.png",
                             r"data\sounds\menu-button-sound.mp3")
    github_right_btn = Button(WIDTH // 2 + 100, HEIGHT - 170, 67, 72, r"buttons\github-btn.png",
                              r"buttons\hover-github-btn.png",
                              r"data\sounds\menu-button-sound.mp3")

    title = Object(WIDTH // 2 - 640 // 2 - 46, 85, 640, 82, r"objects\info-title-obj.png")
    field = Object(WIDTH // 2 - 450, 200, 900, 430, r"objects\info-field-obj.png")
    alexandr = Object(WIDTH // 2 - 265, HEIGHT - 157, 269, 46, r"objects\alexandr-obj.png")
    igor = Object(WIDTH // 2 + 180, HEIGHT - 157, 142, 45, r"objects\igor-obj.png")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                running = False

            if event.type == pygame.USEREVENT and event.button == github_left_btn:
                webbrowser.open('https://github.com/mikhalexandr')

            if event.type == pygame.USEREVENT and event.button == github_right_btn:
                webbrowser.open('https://github.com/WaizorSote')

            for obj in [title, field, alexandr, igor]:
                obj.handle_event(event)

            for button in [github_left_btn, github_right_btn, cross_btn]:
                button.handle_event(event)

        for obj in [title, field, alexandr, igor]:
            obj.draw(screen)

        for button in [github_left_btn, github_right_btn, cross_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


main_menu()
