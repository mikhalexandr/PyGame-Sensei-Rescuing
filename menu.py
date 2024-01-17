import pygame
import sys
import webbrowser
from load_image import load_image
from itemCreator import Object, Button, Stars
from transition import transition
from consts import *
from windows import fullscreen, k

# сначала в меню, инфо и сеттингс пересчитать x и Y относительно title, потом сделать fs

pygame.init()

size = WIDTH, HEIGHT = 1024, 704
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sensei Rescuing')
clock = pygame.time.Clock()
fps = 60

cursor = load_image(r'objects\cursor-obj.png')
pygame.mouse.set_visible(False)

img = load_image(r'backgrounds\main-menu-bg.png')
bg = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))

checkIsActive2 = False
checkIsActiveBoss = False
checkF11 = False
isSliderMusic = False
isSliderSound = False

checkIsPassing1 = True
checkIsPassing2 = False
checkIsPassingBoss = False

record1 = 0
record2 = 0
record3 = 0

a = open(r"data\settings.txt", "r", encoding="utf-8")
checkActDet = list(map(lambda x: float(x.rstrip('\n')), a))
wM = checkActDet[0]
wS = checkActDet[1]
volS = wS

ft = True


def main_menu():
    global checkActDet, wM, wS, checkF11, ft
    if ft:
        pygame.mixer.music.load(r"data\sounds\menu-sound.wav")
        pygame.mixer.music.play(-1)
        ft = False
    pygame.mixer.music.set_volume(wM)

    title = Object(WIDTH // 2 - 886 // 2, 49, 886, 80, r"objects\menu-title-obj.png")

    start_btn = Button(WIDTH // 2 - 240 // 2, 186, 240, 100, r"buttons\default-start-btn.png",
                       r"buttons\hover-start-btn.png", r"buttons\press-start-btn.png",
                       r"data\sounds\menu-button-sound.mp3")
    settings_btn = Button(WIDTH // 2 - 240 // 2, 284, 240, 100, r"buttons\default-settings-btn.png",
                          r"buttons\hover-settings-btn.png", r"buttons\press-settings-btn.png",
                          r"data\sounds\menu-button-sound.mp3")
    info_btn = Button(WIDTH // 2 - 240 // 2, 382, 240, 100, r"buttons\default-info-btn.png",
                      r"buttons\hover-info-btn.png", r"buttons\press-info-btn.png",
                      r"data\sounds\menu-button-sound.mp3")
    exit_btn = Button(WIDTH // 2 - 240 // 2, 480, 240, 100, r"buttons\default-exit-btn.png",
                      r"buttons\hover-exit-btn.png", r"buttons\press-exit-btn.png",
                      r"data\sounds\menu-button-sound.mp3")

    running = True
    while running:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.USEREVENT and event.button == exit_btn):
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

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                if checkF11:
                    checkF11 = False
                    print('f11 off')
                else:
                    checkF11 = True
                    print('f11 on')

            for button in [start_btn, settings_btn, info_btn, exit_btn]:
                button.handle_event(event, volS)

        for button in [start_btn, settings_btn, info_btn, exit_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        title.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if not checkF11:
            if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
                screen.blit(cursor, (x_c, y_c))
        else:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def levels_menu():
    global checkF11

    if not checkF11:
        all_w, all_h = WIDTH // 2 - 399, HEIGHT - 619
    else:
        all_w, all_h = WIDTH // 2 - 399, HEIGHT - 770
    title = Object(all_w, all_h, 700, 82, r"objects\level-menu-title-obj.png")
    cross_btn = Button(all_w + title.width + 18, all_h + 8, 67, 72, r"buttons\default-cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"buttons\press-cross-btn.png", r"data\sounds\menu-button-sound.mp3")
    level1Button = Button(all_w - 49, all_h + 215.5, 144, 155, r"buttons\default-first-btn.png",
                          r"buttons\hover-first-btn.png", r"buttons\press-first-btn.png",
                          r"data\sounds\menu-button-sound.mp3")
    level2Button = Button(all_w + 326, all_h + 215.5, 144, 155, r"buttons\default-second-btn.png",
                          r"buttons\hover-second-btn.png", r"buttons\press-second-btn.png",
                          r"data\sounds\menu-button-sound.mp3", r"buttons\no-active-second-btn.png")
    levelBossButton = Button(all_w + 699, all_h + 215.5, 144, 155, r"buttons\default-boss-btn.png",
                             r"buttons\hover-boss-btn.png", r"buttons\press-boss-btn.png",
                             r"data\sounds\menu-button-sound.mp3", r"buttons\no-active-boss-btn.png")
    info_btn = Button(all_w + 857, all_h + 178, 18, 18, r"buttons\default-level-info-btn.png",
                      r"buttons\hover-level-info-btn.png")

    field = Object(all_w - 91, all_h + 166, 980, 305, r"objects\level-menu-field-obj.png")
    level1Field = Object(all_w - 70, all_h + 197.5, 186, 189, r"objects\start-level-field-obj.png")
    level2Field = Object(all_w + 130, all_h + 197.5, 360, 189, r"objects\level-field-obj.png",
                         r"objects\hover-level-field-obj.png")
    levelBossField = Object(all_w + 503, all_h + 197.5, 360, 189,
                            r"objects\level-field-obj.png", r"objects\hover-level-field-obj.png")

    zeroStars, oneStar, twoStars, threeStars = (r"objects\stars-zero-obj.png", r"objects\stars-one-obj.png",
                                                r"objects\stars-two-obj.png", r"objects\stars-three-obj.png")
    level1Stars = Stars(all_w - 103, all_h + 395.5, 252, 44, zeroStars, oneStar, twoStars, threeStars)
    level2Stars = Stars(all_w + 273, all_h + 395.5, 252, 44, zeroStars, oneStar, twoStars,
                        threeStars)
    levelBossStars = Stars(all_w + 647, all_h + 395.5, 252, 44, zeroStars, oneStar, twoStars,
                           threeStars)

    running = True
    while running:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                main_menu()

            if event.type == pygame.USEREVENT and event.button == level1Button:
                print(' -> Level 1')
                transition()

            if event.type == pygame.USEREVENT and event.button == level2Button and checkIsActive2:
                print(' -> Level 2')
                transition()

            if event.type == pygame.USEREVENT and event.button == levelBossButton and checkIsActiveBoss:
                print(' -> Level 3 (Boss)')
                transition()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                if checkF11:
                    checkF11 = False
                    print('f11 off')
                    change_fullScreen(1024, 704)
                    levels_menu()
                else:
                    checkF11 = True
                    print('f11 on')
                    change_fullScreen(1920, 1080, pygame.FULLSCREEN)
                    levels_menu()

            for button in [cross_btn, level1Button, level2Button, levelBossButton]:
                button.handle_event(event, volS)

        for obj in [title, field, level1Field]:
            obj.draw(screen)

        level2Field.check_passing(checkIsActive2)
        level2Field.draw(screen)
        levelBossField.check_passing(checkIsActiveBoss)
        levelBossField.draw(screen)

        for button in [cross_btn, level1Button, level2Button, levelBossButton]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        info_btn.check_hover(pygame.mouse.get_pos())
        if info_btn.rect.collidepoint(pygame.mouse.get_pos()):
            field_d = Object(all_w + 357, all_h - 40, 498, 218, r"objects\level-info-field-obj.png")
            field_d.draw(screen)
        info_btn.draw(screen)

        level2Button.check_passing(checkIsActive2)
        levelBossButton.check_passing(checkIsActiveBoss)

        if checkIsPassing1:
            level1Stars.draw(screen, record1)
        if checkIsPassing2:
            level2Stars.draw(screen, record2)
        if checkIsPassingBoss:
            levelBossStars.draw(screen, record3)

        x_c, y_c = pygame.mouse.get_pos()
        if not checkF11:
            if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
                screen.blit(cursor, (x_c, y_c))
        else:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def settings_menu():
    global checkF11, isSliderMusic, isSliderSound, sl, sd, tmp, volS, wM, wS, checkActDet
    title = Object(WIDTH // 2 - 626 // 2 - 50, 85, 626, 82, r"objects\settings-title-obj.png")
    field_audio = Object(WIDTH // 2 - 450, 200, 420, 430, r"objects\audio-field-obj.png")
    field_video = Object(WIDTH // 2 + 30, 200, 420, 430, r"objects\video-field-obj.png")
    fs_name = Object(WIDTH // 2 + 478 // 2 - 332 // 2, 330, 332, 75, r"objects\fullscreen-obj.png")
    sound_name = Object(WIDTH // 2 - 450 // 2 - 332 // 2 - 18, 470, 332, 35, r"objects\sound-obj.png")
    music_name = Object(WIDTH // 2 - 450 // 2 - 332 // 2 - 18, 334, 332, 35, r"objects\music-obj.png")

    cross_btn = Button(WIDTH - 229, 93, 67, 72, r"buttons\default-cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"buttons\press-cross-btn.png", r"data\sounds\menu-button-sound.mp3")
    fs_btn = Button(WIDTH // 2 + 478 // 2 - 136 // 2, 420, 136, 62, r"buttons\fullscreen-off-btn.png", "",
                    r"buttons\fullscreen-on-btn.png", r"data\sounds\menu-button-sound.mp3")

    sl = 106 + 300 * wM
    music_slider_btn = Button(sl, 387, 26, 28,
                              r"buttons\default-slider-btn.png", r"buttons\hover-slider-btn.png",
                              r"buttons\press-slider-btn.png")

    sd = 106 + 300 * wS
    sound_slider_btn = Button(sd, 523, 26, 28,
                              r"buttons\default-slider-btn.png", r"buttons\hover-slider-btn.png",
                              r"buttons\press-slider-btn.png")

    music_slider_obj = Object(WIDTH // 2 - 450 // 2 - 302 // 2 - 18, 393, 302, 16, r"objects\slider-obj.png")
    sound_slider_obj = Object(WIDTH // 2 - 450 // 2 - 302 // 2 - 18, 529, 302, 16, r"objects\slider-obj.png")
    running = True
    while running:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    transition()
                    running = False

            if event.type == pygame.USEREVENT and event.button == cross_btn:
                transition()
                running = False

            if ((event.type == pygame.USEREVENT and event.button == fs_btn) or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_F11)):
                if checkF11:
                    checkF11 = False
                    print('f11 off')
                    change_fullScreen(1024, 704)
                else:
                    checkF11 = True
                    print('f11 on')
                    change_fullScreen(1920, 1080, pygame.FULLSCREEN)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == music_slider_btn:
                isSliderMusic = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == music_slider_btn:
                isSliderMusic = False

            elif event.type == pygame.MOUSEMOTION:
                if isSliderMusic or isSliderSound:
                    checkActDet = open(r"data\settings.txt", "w")
                    if isSliderMusic:
                        xM = music_slider_btn.rect[0]
                        if 118 < event.pos[0] < 420:
                            x_cube_M = event.pos[0] - xM
                        else:
                            x_cube_M = 13
                        music_slider_btn.rect = music_slider_btn.rect.move(x_cube_M - 13, 0)
                        sl = music_slider_btn.rect[0]
                        wM = (music_slider_btn.rect[0] - 106) / 300
                        pygame.mixer.music.set_volume(wM)

                    elif isSliderSound:
                        xS = sound_slider_btn.rect[0]
                        if 118 < event.pos[0] < 420:
                            x_cube_S = event.pos[0] - xS
                        else:
                            x_cube_S = 13
                        sound_slider_btn.rect = sound_slider_btn.rect.move(x_cube_S - 13, 0)
                        sd = sound_slider_btn.rect[0]
                        wS = (sound_slider_btn.rect[0] - 106) / 300
                        volS = wS
                    checkActDet.writelines([str(wM) + '\n', str(wS)])

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == sound_slider_btn:
                isSliderSound = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == sound_slider_btn:
                isSliderSound = False

            for button in [cross_btn, fs_btn]:
                button.handle_event(event, volS)

            for slider_button in [music_slider_btn, sound_slider_btn]:
                slider_button.handle_event_slider(event)

        for obj in [title, field_audio, field_video, fs_name, sound_name, music_name, music_slider_obj,
                    sound_slider_obj]:
            obj.draw(screen)

        for slider_button in [cross_btn, music_slider_btn, sound_slider_btn]:
            slider_button.check_hover(pygame.mouse.get_pos())
            slider_button.draw(screen)

        fs_btn.check_hover(pygame.mouse.get_pos())
        fs_btn.draw_f11(screen, checkF11)

        x_c, y_c = pygame.mouse.get_pos()
        if not checkF11:
            if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
                screen.blit(cursor, (x_c, y_c))
        else:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def info_menu():
    global checkF11
    cross_btn = Button(WIDTH - 218, 93, 67, 72, r"buttons\default-cross-btn.png", r"buttons\hover-cross-btn.png",
                       r"buttons\press-cross-btn.png", r"data\sounds\menu-button-sound.mp3")
    github_left_btn = Button(WIDTH // 2 - 345, HEIGHT - 170, 67, 72, r"buttons\default-github-btn.png",
                             r"buttons\hover-github-btn.png", r"buttons\press-github-btn.png",
                             r"data\sounds\menu-button-sound.mp3")
    github_right_btn = Button(WIDTH // 2 + 100, HEIGHT - 170, 67, 72, r"buttons\default-github-btn.png",
                              r"buttons\hover-github-btn.png", r"buttons\press-github-btn.png",
                              r"data\sounds\menu-button-sound.mp3")

    title = Object(WIDTH // 2 - 640 // 2 - 46, 85, 640, 82, r"objects\info-title-obj.png")
    field = Object(WIDTH // 2 - 450, 200, 900, 430, r"objects\info-field-obj.png")
    alexandr = Object(WIDTH // 2 - 265, HEIGHT - 157, 269, 46, r"objects\alexandr-obj.png")
    igor = Object(WIDTH // 2 + 180, HEIGHT - 157, 142, 45, r"objects\igor-obj.png")

    running = True
    while running:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                if checkF11:
                    checkF11 = False
                    print('f11 off')
                else:
                    checkF11 = True
                    print('f11 on')

            for button in [github_left_btn, github_right_btn, cross_btn]:
                button.handle_event(event, volS)

        for obj in [title, field, alexandr, igor]:
            obj.draw(screen)

        for button in [github_left_btn, github_right_btn, cross_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)

        x_c, y_c = pygame.mouse.get_pos()
        if not checkF11:
            if 1 <= x_c <= 1022 and 1 <= y_c <= 702:
                screen.blit(cursor, (x_c, y_c))
        else:
            screen.blit(cursor, (x_c, y_c))

        pygame.display.flip()


def change_fullScreen(width, height, fullScreen=1):
    global WIDTH, HEIGHT, screen, img, bg
    WIDTH, HEIGHT = width, height
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullScreen)
    if checkF11:
        tmp = load_image(r"backgrounds\main-menu-fullScreen-bg.png")
        bg = pygame.transform.scale(tmp, (tmp.get_width(), tmp.get_height()))
    else:
        bg = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))


# main_menu()
