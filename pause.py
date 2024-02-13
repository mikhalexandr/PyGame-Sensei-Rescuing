import pygame
import consts
import levels_menu
import game
import windows
import fileManager
from processHelper import terminate, transition
from itemCreator import Object, Button


def pause(time, sloniks):
    title = Object(windows.width // 2 - 176, windows.height // 2 - 190, 352, 116,
                   fr"objects\{consts.languageNow}\pause-title-obj.png")

    sound_name = Object(windows.width // 2 + 28, windows.height // 2 + 124, 434, 50,
                        fr"objects\{consts.languageNow}\sound-obj.png")
    music_name = Object(windows.width // 2 - 28 - 434, windows.height // 2 + 124, 434, 50,
                        fr"objects\{consts.languageNow}\music-obj.png")
    music_slider_obj = Object(music_name.x + 434 // 2 - 422 // 2, windows.height // 2 + 200, 422, 16,
                              r"objects\without text\slider-obj.png")
    sound_slider_obj = Object(sound_name.x + 434 // 2 - 422 // 2, windows.height // 2 + 200, 422, 16,
                              r"objects\without text\slider-obj.png")
    sound_field = Object(sound_name.x + 434 // 2 - 470 // 2, windows.height // 2 + 110, 470, 128,
                         fr"objects\without text\volume-field-obj.png")
    music_field = Object(music_name.x + 434 // 2 - 470 // 2, windows.height // 2 + 110, 470, 128,
                         fr"objects\without text\volume-field-obj.png")
    if not windows.fullscreen:
        sl = music_slider_obj.x + music_slider_obj.width * consts.wM
    else:
        sl = (music_slider_obj.x + music_slider_obj.width) + music_slider_obj.width * consts.wM
    music_slider_btn = Button(sl, music_slider_obj.y - 6, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")
    if not windows.fullscreen:
        sd = sound_slider_obj.x + sound_slider_obj.width * consts.wS
    else:
        sd = (sound_slider_obj.x + sound_slider_obj.width) + sound_slider_obj.width * consts.wS
    sound_slider_btn = Button(sd, sound_slider_obj.y - 6, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")

    repeat_btn = Button(title.x + title.width // 2 - 94 // 2, title.y + title.height + 18, 94, 104,
                        r"buttons\without text\default-repeat-btn.png",
                        r"buttons\without text\hover-repeat-btn.png",
                        r"buttons\without text\press-repeat-btn.png", r"data\sounds\menu-button-sound.mp3")
    to_lvlmenu_btn = Button(title.x + title.width - 94 - 15, title.y + title.height + 18, 94, 104,
                            r"buttons\without text\default-tolvlmenu-btn.png",
                            r"buttons\without text\hover-tolvlmenu-btn.png",
                            r"buttons\without text\press-tolvlmenu-btn.png", r"data\sounds\menu-button-sound.mp3")
    play_btn = Button(title.x + 15, title.y + title.height + 18, 94, 104,
                      r"buttons\without text\default-play-btn.png",
                      r"buttons\without text\hover-play-btn.png",
                      r"buttons\without text\press-play-btn.png", r"data\sounds\menu-button-sound.mp3")

    pause_field = Object(windows.width // 2 - 430 // 2, windows.height // 2 - 246, 430, 342,
                         fr"objects\without text\pause-field-obj.png")
    left_field = Object(music_name.x + 434 // 2 - 470 // 2, windows.height // 2 - 246, 252, 342,
                        fr"objects\without text\left-field-obj.png")
    time_title = Object(left_field.x + left_field.width // 2 - 196 // 2, windows.height // 2 - 185, 196, 34,
                        fr"objects\{consts.languageNow}\pause-time-obj.png")
    sloniks_title = Object(left_field.x + left_field.width // 2 - 234 // 2, windows.height // 2 - 50, 234, 37,
                           fr"objects\{consts.languageNow}\pause-sloniks-obj.png")
    right_field = Object(sound_name.x + 434 // 2 - 470 // 2 + 470 - 252, windows.height // 2 - 246, 252, 342,
                         fr"objects\{consts.languageNow}\right-field-obj.png")

    TimeFont = pygame.font.Font(r"data\fonts\PixelNumbers.ttf", 50)
    time_sorted = f"{time // 60:02}:{time % 60:02}"
    levelTime = TimeFont.render(time_sorted, True, "#ffffff")
    levelTimeRect = levelTime.get_rect(
        center=(time_title.x + time_title.width // 2, time_title.y + time_title.height + 40))

    SloniksFont = pygame.font.Font(r"data\fonts\PixelNumbers.ttf", 50)
    levelSloniks = SloniksFont.render(str(sloniks), True, "#ffffff")
    levelSloniksRect = levelSloniks.get_rect(
        center=(sloniks_title.x + sloniks_title.width // 2, sloniks_title.y + sloniks_title.height + 40))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.USEREVENT and event.button == to_lvlmenu_btn:
                transition()
                levels_menu.levels_menu()

            if event.type == pygame.USEREVENT and event.button == repeat_btn:
                transition()
                game.game_def(consts.lvlNow)

            if event.type == pygame.USEREVENT and event.button == play_btn:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == music_slider_btn:
                consts.isPauseSliderMusic = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == music_slider_btn:
                consts.isPauseSliderMusic = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == sound_slider_btn:
                consts.isPauseSliderSound = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == sound_slider_btn:
                consts.isPauseSliderSound = False

            elif event.type == pygame.MOUSEMOTION:
                if consts.isPauseSliderMusic or consts.isPauseSliderSound:
                    if consts.isPauseSliderMusic:
                        xM = music_slider_btn.rect[0]
                        if music_slider_obj.x < event.pos[0] < music_slider_obj.x + music_slider_obj.width:
                            x_cube_M = event.pos[0] - xM
                        else:
                            x_cube_M = 13
                        music_slider_btn.rect = music_slider_btn.rect.move(x_cube_M - 13, 0)
                        if not windows.fullscreen:
                            consts.wM = (music_slider_btn.rect[0] - music_slider_obj.x) / music_slider_obj.width
                            if consts.wM < 0:
                                consts.wM = 0
                            if consts.wM > 1:
                                consts.wM = 1
                        else:
                            consts.wM = ((music_slider_btn.rect[0] - (music_slider_obj.x + music_slider_obj.width))
                                         / music_slider_obj.width)
                            if consts.wM < 0:
                                consts.wM = 0
                            if consts.wM > 1:
                                consts.wM = 1
                        pygame.mixer.music.set_volume(consts.wM)

                    elif consts.isPauseSliderSound:
                        xS = sound_slider_btn.rect[0]
                        if sound_slider_obj.x < event.pos[0] < sound_slider_obj.x + sound_slider_obj.width:
                            x_cube_S = event.pos[0] - xS
                        else:
                            x_cube_S = 13
                        sound_slider_btn.rect = sound_slider_btn.rect.move(x_cube_S - 13, 0)
                        if not windows.fullscreen:
                            consts.wS = (sound_slider_btn.rect[0] - sound_slider_obj.x) / sound_slider_obj.width
                            if consts.wS < 0:
                                consts.wS = 0
                            if consts.wS > 1:
                                consts.wS = 1
                            consts.volS = consts.wS
                        else:
                            consts.wS = ((sound_slider_btn.rect[0] - (sound_slider_obj.x + sound_slider_obj.width))
                                         / sound_slider_obj.width)
                            if consts.wS < 0:
                                consts.wS = 0
                            if consts.wS > 1:
                                consts.wS = 1
                            consts.volS = consts.wS
                    fileManager.volumeExport(consts.wM, consts.wS)

            for button in [repeat_btn, to_lvlmenu_btn, play_btn]:
                button.handle_event(event, consts.volS)

            for slider_button in [music_slider_btn, sound_slider_btn]:
                slider_button.handle_event_slider(event)

        for obj in [consts.pause_field, left_field, time_title, sloniks_title, pause_field, right_field, sound_field,
                    music_field,
                    title, sound_slider_obj, music_slider_obj, music_slider_btn, sound_slider_btn, sound_name,
                    music_name]:
            obj.draw(windows.screen)

        for button in [repeat_btn, to_lvlmenu_btn, play_btn, music_slider_btn, sound_slider_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(windows.screen)

        windows.screen.blit(levelTime, levelTimeRect)
        windows.screen.blit(levelSloniks, levelSloniksRect)

        pygame.display.flip()
