import pygame
import windows
import consts
import spriteGroups
import game_over
from itemCreator import Button
from processHelper import terminate, load_image
from cutsceneAnimator import AnimatedError


def hleb_greeting_cutscene():
    pass


def boss_greeting_cutscene():
    pass


def boss_win_cutscene():
    field = AnimatedError(load_image(fr"cutscenes\boss-win\hero-lose-boss-field-obj.png"), 2, 1,
                          windows.width // 2 - 1290 / 4,
                          windows.height // 2 - 513 / 2)
    yes_btn = Button(field.x + 645 / 2 - 92 - 20, field.y + 513 - 38 - 48, 92, 38,
                     fr"cutscenes\boss-win\default-yes-btn.png",
                     fr"cutscenes\boss-win\hover-yes-btn.png",
                     "",
                     r"data\sounds\menu-button-sound.mp3")
    no_btn = Button(field.x + 645 / 2 + 20, field.y + 513 - 38 - 48, 92, 38,
                    fr"cutscenes\boss-win\default-no-btn.png",
                    fr"cutscenes\boss-win\hover-no-btn.png",
                    "",
                    r"data\sounds\menu-button-sound.mp3")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.USEREVENT and event.button == yes_btn:
                running = False
                spriteGroups.animatedError.empty()

            if event.type == pygame.USEREVENT and event.button == no_btn:
                spriteGroups.animatedError.empty()
                game_over.game_over()

            for button in [yes_btn, no_btn]:
                button.handle_event(event, consts.volS)

        consts.backgrBossWin.draw(windows.screen)
        field.update()
        spriteGroups.animatedError.draw(windows.screen)

        for button in [yes_btn, no_btn]:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(windows.screen)

        pygame.display.flip()


def boss_lose_cutscene():
    pass
