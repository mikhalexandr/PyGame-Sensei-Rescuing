import pygame
import menu
import game
import windows
import lvl_gen
import fileManager
from processHelper import terminate
from itemCreator import Object, Button

languageNow = fileManager.languageImport()


def pause(super_pause):
    field = Object(8, 8, 1008, 688, rf"objects\without text\pause-window-obj.png")
    title = Object(windows.width // 2 - 150, windows.height // 2 - 224, 300, 100,
                   fr"objects\{languageNow}\pause-title-obj.png")

    sound_name = Object(windows.width // 2 + 28, windows.height // 2 + 124, 434, 50,
                        fr"objects\{languageNow}\sound-obj.png")
    music_name = Object(windows.width // 2 - 28 - 434, windows.height // 2 + 124, 434, 50,
                        fr"objects\{languageNow}\music-obj.png")
    music_slider_obj = Object(music_name.x + 434 // 2 - 422 // 2, windows.height // 2 + 200, 422, 16,
                              r"objects\without text\slider-obj.png")
    sound_slider_obj = Object(sound_name.x + 434 // 2 - 422 // 2, windows.height // 2 + 200, 422, 16,
                              r"objects\without text\slider-obj.png")
    sound_field = Object(sound_name.x + 434 // 2 - 470 // 2, windows.height // 2 + 110, 470, 128,
                         fr"objects\without text\volume-field-obj.png")
    music_field = Object(music_name.x + 434 // 2 - 470 // 2, windows.height // 2 + 110, 470, 128,
                         fr"objects\without text\volume-field-obj.png")
    music_slider_btn = Button(music_slider_obj.x + 422 - 15, music_slider_obj.y - 6, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")
    sound_slider_btn = Button(sound_slider_obj.x + 422 - 15, sound_slider_obj.y - 6, 26, 28,
                              r"buttons\without text\default-slider-btn.png",
                              r"buttons\without text\hover-slider-btn.png",
                              r"buttons\without text\press-slider-btn.png")

    repeat_btn = Button(windows.width // 2 - 150 + 102, windows.height // 2 - 112, 94, 104,
                        r"buttons\without text\default-repeat-btn.png",
                        r"buttons\without text\hover-repeat-btn.png",
                        r"buttons\without text\press-repeat-btn.png", r"data\sounds\menu-button-sound.mp3")
    to_lvlmenu_btn = Button(windows.width // 2 - 150 + 212, windows.height // 2 - 112, 94, 104,
                            r"buttons\without text\default-tolvlmenu-btn.png",
                            r"buttons\without text\hover-tolvlmenu-btn.png",
                            r"buttons\without text\press-tolvlmenu-btn.png", r"data\sounds\menu-button-sound.mp3")
    play_btn = Button(windows.width // 2 - 150 - 7, windows.height // 2 - 112, 94, 104,
                      r"buttons\without text\default-play-btn.png",
                      r"buttons\without text\hover-play-btn.png",
                      r"buttons\without text\press-play-btn.png", r"data\sounds\menu-button-sound.mp3")

    control_btn = Button(windows.width // 2 - 150, windows.height // 2 + 2, 300, 80,
                         fr"buttons\{languageNow}\default-controls-btn.png",
                         fr"buttons\{languageNow}\hover-controls-btn.png")  # 266
    pause_field = Object(windows.width // 2 - 430 // 2, windows.height // 2 - 246, 430, 342,
                         fr"objects\without text\pause-field-obj.png")
    left_field = Object(music_name.x + 434 // 2 - 470 // 2, windows.height // 2 - 246, 252, 342,
                        fr"objects\without text\left-field-obj.png")
    right_field = Object(sound_name.x + 434 // 2 - 470 // 2 + 470 - 252, windows.height // 2 - 246, 252, 342,
                        fr"objects\without text\right-field-obj.png")
    control_field = Object(windows.width // 2 - 250, windows.height // 2 - 170, 504, 252,
                           fr"objects\{languageNow}\controls-field-obj.png")

    while super_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate(windows.fullscreen)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                if windows.fullscreen:
                    windows.fullscreen = 0
                else:
                    windows.fullscreen = 1

            if event.type == pygame.USEREVENT and event.button == to_lvlmenu_btn:
                menu.levels_menu()

            if event.type == pygame.USEREVENT and event.button == repeat_btn:
                game.game_def(menu.lvlNow)

            if event.type == pygame.USEREVENT and event.button == play_btn:
                super_pause = False

            for button in [repeat_btn, to_lvlmenu_btn, play_btn]:
                button.handle_event(event, menu.volS)

        for obj in [field, left_field, pause_field, right_field, sound_field, music_field, title,
                    sound_slider_obj,
                    music_slider_obj, music_slider_btn, sound_slider_btn, sound_name, music_name]:
            obj.draw(lvl_gen.screen)

        for button in [repeat_btn, to_lvlmenu_btn, play_btn, control_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(lvl_gen.screen)

        # if control_btn.rect.collidepoint(pygame.mouse.get_pos()):
        #     control_field.draw(lvl_gen.screen)

        pygame.display.flip()
