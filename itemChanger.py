import pygame
import windows
import consts
import starsRecorder
import fileManager
import spriteGroups
from processHelper import load_image
from itemAnimator import AnimatedHero, AnimatedHealthBar, AnimatedHeroHealth
from itemCreator import Object, Button


def heroHeartsChanger():
    spriteGroups.hero_health.empty()
    if not windows.fullscreen:
        img_tmp = load_image(r"objects\animated\hearts-obj.png")
        tr_tmp = pygame.transform.scale(img_tmp,
                                        (img_tmp.get_width() * 2, img_tmp.get_height() * 2))
        heroHealth = AnimatedHeroHealth(tr_tmp, 5, 1,
                                        12, 18)
    else:
        img_tmp = load_image(r"objects\animated\hearts-obj.png")
        tr_tmp = pygame.transform.scale(img_tmp,
                                        (img_tmp.get_width() * 4, img_tmp.get_height() * 4))
        heroHealth = AnimatedHeroHealth(tr_tmp, 5, 1,
                                        windows.otstupx + 12, 18)
    return heroHealth


def healthBossBarChanger():
    spriteGroups.health_bar.empty()
    if not windows.fullscreen:
        img_tmp = load_image(r"objects\animated\boss-health-bar-obj.png")
        tr_tmp = pygame.transform.scale(img_tmp,
                                        (img_tmp.get_width() * 1.68, img_tmp.get_height() * 1.68))
        healthBossBar = AnimatedHealthBar(tr_tmp, 41, 1,
                                          windows.width // 2 - 14760 * 1.68 / 41 / 2, 12)
    else:
        img_tmp = load_image(r"objects\animated\boss-health-bar-obj.png")
        tr_tmp = pygame.transform.scale(img_tmp,
                                        (img_tmp.get_width() * 2, img_tmp.get_height() * 2))
        healthBossBar = AnimatedHealthBar(tr_tmp, 41, 1,
                                          windows.width // 2 - 14760 * 2 / 41 / 2, 12)
    return healthBossBar


def heroOnScreenChanger(hero, title, hero_field):
    current_hero = None
    if hero == 1:
        spriteGroups.animatedHero.empty()
        heroWai = AnimatedHero(load_image(r"objects\animated\hero-wai-obj.png"), 1, 8,
                               hero_field.x + hero_field.width // 2 - 116 // 2,
                               title.y + 188)
        current_hero = heroWai
    elif hero == 2:
        spriteGroups.animatedHero.empty()
        heroTheStrongest = AnimatedHero(load_image(r"objects\animated\hero-the-strongest-obj.png"), 1, 8,
                                        hero_field.x + hero_field.width // 2 - 104 // 2,
                                        title.y + 188)
        current_hero = heroTheStrongest
    return current_hero


def pauseButtonChanger():
    if not windows.fullscreen:
        pause_btn = Button(windows.width - 60, 6, 52, 54,
                           fr"buttons\without text\default-pause-btn.png",
                           fr"buttons\without text\hover-pause-btn.png",
                           "", r"data\sounds\menu-button-sound.mp3")
    else:
        pause_btn = Button(windows.width - windows.otstupx - 90,
                           6, 78, 81,
                           fr"buttons\without text\default-pause-btn.png",
                           fr"buttons\without text\hover-pause-btn.png",
                           "", r"data\sounds\menu-button-sound.mp3")
    return pause_btn


def fullscreenChanger(fullscreen, ft=False):
    fileManager.fullscreenExport(windows.fullscreen)
    if fullscreen:
        if not ft:
            windows.width, windows.height = windows.fullsize
            windows.screen = pygame.display.set_mode(windows.fullsize, pygame.FULLSCREEN)
        consts.menu_bg = pygame.transform.scale(consts.img_fs, (consts.img_fs.get_width(), consts.img_fs.get_height()))
        consts.pause_field = Object(windows.otstupx + 8, 8, windows.width - windows.otstupx * 2 - 16, 1064,
                                    r"objects\without text\pause-window-obj.png")
        consts.game_state_field = Object(windows.otstupx + 8, windows.height - 1072,
                                         windows.width - windows.otstupx * 2 - 16, 1064,
                                         r"objects\without text\games-window-obj.png")
    else:
        if not ft:
            windows.width, windows.height = windows.size
            windows.screen = pygame.display.set_mode(windows.size)
        consts.menu_bg = pygame.transform.scale(consts.img, (consts.img.get_width() * 2, consts.img.get_height() * 2))
        consts.pause_field = Object(windows.width - 1016, windows.height - 696, 1008, 688,
                                    r"objects\without text\pause-window-obj.png")
        consts.game_state_field = Object(windows.width - 1016, windows.height - 696, 1008, 688,
                                         r"objects\without text\games-window-obj.png")


def volumeChanger(event, music_slider_btn, music_slider_obj, sound_slider_btn, sound_slider_obj):
    if consts.isSliderMusic:
        xM = music_slider_btn.rect[0]
        if (music_slider_obj.x + music_slider_obj.width / 30.2 < event.pos[0] < music_slider_obj.x +
                music_slider_obj.width - (music_slider_obj.width / 30.2)):
            x_cube_M = event.pos[0] - xM
        else:
            x_cube_M = music_slider_btn.width // 2
        music_slider_btn.rect = music_slider_btn.rect.move(x_cube_M - music_slider_btn.width // 2, 0)
        consts.wM = round((music_slider_btn.rect[0] - music_slider_obj.x) / music_slider_obj.width, 3)
        if consts.wM < 0.0:
            consts.wM = 0.0
        pygame.mixer.music.set_volume(consts.wM)
    elif consts.isSliderSound:
        xS = sound_slider_btn.rect[0]
        if (sound_slider_obj.x + sound_slider_obj.width / 30.2 < event.pos[0] < sound_slider_obj.x
                + sound_slider_obj.width - (sound_slider_obj.width / 30.2)):
            x_cube_S = event.pos[0] - xS
        else:
            x_cube_S = sound_slider_btn.width // 2
        sound_slider_btn.rect = sound_slider_btn.rect.move(x_cube_S - sound_slider_btn.width // 2, 0)
        consts.wS = round((sound_slider_btn.rect[0] - sound_slider_obj.x) / sound_slider_obj.width, 3)
        if consts.wS < 0.0:
            consts.wS = 0.0
        consts.volS = consts.wS
    fileManager.volumeExport(consts.wM, consts.wS)


def starsChanger(whatLevel, time):
    if whatLevel == 1:
        if 0 < time <= 35:
            return 3
        elif 35 < time <= 40:
            return 2
        elif 40 < time <= 60:
            return 1
        elif time > 60:
            return 0
    if whatLevel == 2:
        if 0 < time <= 65:
            return 3
        elif 65 < time <= 70:
            return 2
        elif 70 < time <= 90:
            return 1
        elif time > 90:
            return 0
    if whatLevel == 3:
        if 0 < time <= 125:
            return 3
        elif 125 < time <= 130:
            return 2
        elif 130 < time <= 150:
            return 1
        elif time > 150:
            return 0


def timeChanger(whatLevel, ButtonsFont, w, h, screen):
    time = starsRecorder.get_seconds(whatLevel)
    time_sorted = f"{time // 60:02}:{time % 60:02}"
    if whatLevel == 1:
        levelTime = ButtonsFont.render(time_sorted, True, "#ffffff")
        levelTimeRect = levelTime.get_rect(center=(w + 186 // 2, h + 80))
        return screen.blit(levelTime, levelTimeRect)
    if whatLevel == 2:
        levelTime = ButtonsFont.render(time_sorted, True, "#ffffff")
        levelTimeRect = levelTime.get_rect(center=(w + 186 // 2, h + 80))
        return screen.blit(levelTime, levelTimeRect)
    if whatLevel == 3:
        levelTime = ButtonsFont.render(time_sorted, True, "#ffffff")
        levelTimeRect = levelTime.get_rect(center=(w + 186 // 2, h + 80))
        return screen.blit(levelTime, levelTimeRect)
