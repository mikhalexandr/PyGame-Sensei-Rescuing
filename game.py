import pygame.surface
import boss
import fileManager
import lvl_gen
import game_over
import game_complete
import pause
import consts
import windows
import starsRecorder
from hero import Hero
from processHelper import terminate
from itemCreator import Object
from itemChanger import starsChanger


def game_def(lvl):
    pygame.mixer.music.load(r"data\sounds\game-theme-sound.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(consts.wM)
    start_coords = lvl_gen.generate_level(lvl)
    character = fileManager.heroImport()[0]
    if not windows.fullscreen:
        pause_btn = Object(windows.width - windows.width + 8, windows.height - windows.height + 6, 108, 54,
                           r"objects\without text\pause-button-obj.png")
    else:
        pause_btn = Object(windows.otstupx + 8, windows.height - windows.height + 6, 144, 72,
                           r"objects\without text\pause-button-obj.png")
    lvl_gen.updater()
    consts.hero = Hero(*start_coords, windows.k ** windows.fullscreen, character)
    running = True
    lvl_gen.characters.draw(windows.screen)
    thing = ''
    cheatPanel = False  # cheats
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    started = True
    current_seconds = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == timer_event and started:
                current_seconds += 1
                # print(current_seconds)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    consts.xspeed = consts.hero.xs
                    if not consts.jumping:
                        consts.hero.change_hero('r', consts.hero.get_coords())
                    else:
                        if not consts.falling:
                            consts.hero.change_hero('jumpr', consts.hero.get_coords())
                        else:
                            consts.hero.change_hero('fallr', consts.hero.get_coords())
                    consts.lookingright = 1
                    consts.runright = True
                    consts.runleft = False
                elif event.key == pygame.K_s:
                    consts. sitting = True
                elif event.key == pygame.K_a:
                    consts.xspeed = consts.hero.xs
                    if not consts.jumping:
                        consts.hero.change_hero('l', consts.hero.get_coords())
                    else:
                        if not consts.falling:
                            consts.hero.change_hero('jumpl', consts.hero.get_coords())
                        else:
                            consts.hero.change_hero('falll', consts.hero.get_coords())
                    consts.lookingright = 0
                    consts.runleft = True
                    consts.runright = False
                elif event.key == pygame.K_SPACE:
                    if consts.sitting:
                        consts.yspeed = 7
                    else:
                        if (not (consts.jumping or consts.falling or consts.sitting)) or cheatPanel:
                            consts.jumping = True
                            consts.yspeed = -9 - 2 * cheatPanel
                            if consts.lookingright:
                                consts.hero.change_hero('jumpr', consts.hero.get_coords())
                            else:
                                consts.hero.change_hero('jumpl', consts.hero.get_coords())
                elif event.key == pygame.K_w:
                    if pygame.sprite.spritecollide(consts.hero, lvl_gen.finale, False):
                        thing = ''
                        consts.hero.end()
                        lvl_gen.updater()
                        started = False
                        record = starsChanger(lvl, current_seconds)
                        if current_seconds < starsRecorder.get_seconds(lvl) or starsRecorder.get_seconds(lvl) == 0:
                            starsRecorder.push_record(lvl, 1, record, current_seconds)
                        starsRecorder.push_lastRecord(lvl, record, current_seconds)
                        game_complete.game_complete()
                    else:
                        if consts.lookingright:
                            consts.shooting = consts.hero.projectile_speed * windows.k ** windows.fullscreen
                        else:
                            consts.shooting = -consts.hero.projectile_speed * windows.k ** windows.fullscreen
                        consts.hero.shoot(consts.shooting)
                elif event.key == pygame.K_ESCAPE:
                    consts.xspeed = 0
                    predpause = consts.hero.get_coords()
                    consts.hero.end()
                    started = False
                    pause.pause(current_seconds, len(list(lvl_gen.sloniks)))
                    started = True
                    consts.hero = Hero(*predpause, windows.k ** windows.fullscreen, character)
                    if consts.lookingright:
                        consts.hero.change_hero('sr', predpause)
                    else:
                        consts.hero.change_hero('sl', predpause)
                    lvl_gen.rescreen()
                    lvl_gen.updater()
            elif event.type == pygame.WINDOWEXPOSED:
                if consts.lookingright:
                    consts.hero.change_hero('sr', consts.hero.get_coords())
                else:
                    consts.hero.change_hero('sl', consts.hero.get_coords())
                lvl_gen.rescreen()
                lvl_gen.updater()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    consts.runright = False
                elif event.key == pygame.K_s:
                    consts.sitting = False
                elif event.key == pygame.K_a:
                    consts.runleft = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:  # cheats
                    cheatPanel = not cheatPanel
                    consts.hero.xs = 3 * 5 ** cheatPanel
                    consts.hero.projectile_speed = 8 * 2 ** cheatPanel

        pause_btn.draw(windows.screen)
        if pygame.sprite.spritecollide(consts.hero, lvl_gen.changegroup, False):
            lvl_gen.projectilesgroup.empty()
            lvl_gen.nmeprojectilesgroup.empty()
            lvl_gen.projectilespeed = []
            boss.boss_projectile_group.empty()
            boss.b_projectile_speed = []
            if thing == '':
                thing = 1
            else:
                thing += 1
            consts.hero.set_coords(*lvl_gen.generate_level(lvl + thing / 10))
            consts.hero.projectilespeed = []
            windows.screen.fill('#000000')
            lvl_gen.updater()
        lvl_gen.get_shadow(*consts.hero.get_coords(), *consts.hero.get_size())
        lvl_gen.shadowgroup.draw(windows.screen)

        if lvl_gen.projectilesgroup:
            for sprite in range(len(lvl_gen.projectilesgroup)):
                pygame.draw.rect(windows.screen, (36, 34, 52), list(lvl_gen.projectilesgroup)[sprite].rect)
                list(lvl_gen.projectilesgroup)[sprite].rect = list(lvl_gen.projectilesgroup)[sprite].rect.move(
                    consts.hero.projectilespeed[sprite], 0)
                if pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite], lvl_gen.sloniks, False):
                    if (pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite],
                                                    lvl_gen.sloniks, False)[0].get_hit(consts.hero.get_coords()[0]) == 0
                            or cheatPanel):
                        lvl_gen.remover(lvl_gen.board.get_cell(list(
                            pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite], lvl_gen.sloniks, True))[
                                                                   0].rect[:2]))
                    consts.hero.projectilespeed.pop(sprite)
                    list(lvl_gen.projectilesgroup)[sprite].kill()
                    break

                if pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite], boss.boss_group, False):
                    if (pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite],
                                                    boss.boss_group, False)[0].get_hit() == 0):
                        boss.boss_group.empty()
                    consts.hero.projectilespeed.pop(sprite)
                    list(lvl_gen.projectilesgroup)[sprite].kill()
                    break

                if (pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite], lvl_gen.toches, False)
                        or pygame.sprite.spritecollide(list(lvl_gen.projectilesgroup)[sprite],
                                                       lvl_gen.anothertoches, False)):
                    consts.hero.projectilespeed.pop(sprite)
                    list(lvl_gen.projectilesgroup)[sprite].kill()
                    break
            lvl_gen.projectilesgroup.draw(windows.screen)

        if lvl_gen.nmeprojectilesgroup:
            for sprite in range(len(lvl_gen.nmeprojectilesgroup)):
                pygame.draw.rect(windows.screen, (36, 34, 52), list(lvl_gen.nmeprojectilesgroup)[sprite].rect)
                list(lvl_gen.nmeprojectilesgroup)[sprite].rect = list(lvl_gen.nmeprojectilesgroup)[sprite].rect.move(
                    lvl_gen.projectilespeed[sprite][0], 0)
                if pygame.sprite.spritecollide(list(lvl_gen.nmeprojectilesgroup)[sprite], lvl_gen.characters,
                                               False) and not cheatPanel:
                    thing = ''
                    consts.hero.end()
                    lvl_gen.projectilespeed = []
                    lvl_gen.nmeprojectilesgroup.empty()
                    lvl_gen.updater()
                    boss.boss_projectile_group.empty()
                    boss.b_projectile_speed = []
                    started = False
                    game_over.game_over()
                if (pygame.sprite.spritecollide(list(lvl_gen.nmeprojectilesgroup)[sprite], lvl_gen.toches, False)
                        or pygame.sprite.spritecollide(list(lvl_gen.nmeprojectilesgroup)[sprite],
                                                       lvl_gen.anothertoches, False)):
                    lvl_gen.projectilespeed.pop(sprite)
                    list(lvl_gen.nmeprojectilesgroup)[sprite].kill()
                    break
            lvl_gen.nmeprojectilesgroup.draw(windows.screen)

        if boss.boss_projectile_group:
            for sprite in range(len(boss.boss_projectile_group)):
                list(boss.boss_projectile_group)[sprite].rect = list(boss.boss_projectile_group)[sprite].rect.move(
                    boss.b_projectile_speed[sprite][0], 0)
                if pygame.sprite.spritecollide(list(boss.boss_projectile_group)[sprite], lvl_gen.characters,
                                               False) and not cheatPanel:
                    thing = ''
                    consts.hero.end()
                    lvl_gen.projectilespeed = []
                    lvl_gen.nmeprojectilesgroup.empty()
                    boss.boss_projectile_group.empty()
                    boss.b_projectile_speed = []
                    lvl_gen.updater()
                    started = False
                    game_over.game_over()
                elif (pygame.sprite.spritecollide(list(boss.boss_projectile_group)[sprite], lvl_gen.toches, False)
                      or pygame.sprite.spritecollide(list(boss.boss_projectile_group)[sprite],
                                                     lvl_gen.anothertoches, False)):
                    list(boss.boss_projectile_group)[sprite].rect = list(boss.boss_projectile_group)[
                        sprite].rect.move(
                        -boss.b_projectile_speed[sprite][0], 0)
                    if boss.b_projectile_speed[sprite][1] == 2:
                        pygame.draw.rect(windows.screen, (36, 34, 52), (
                            list(boss.boss_projectile_group)[sprite].rect))
                        list(boss.boss_projectile_group)[sprite].kill()
                        boss.b_projectile_speed.pop(sprite)
                        break
                    else:
                        pygame.draw.rect(windows.screen, (36, 34, 52), (
                            list(boss.boss_projectile_group)[sprite].rect))
                        boss.b_projectile_speed[sprite] = (-boss.b_projectile_speed[sprite][0],
                                                           boss.b_projectile_speed[sprite][1] + 1)
                else:
                    pygame.draw.rect(windows.screen, (36, 34, 52), (
                        list(boss.boss_projectile_group)[sprite].rect[0] - boss.b_projectile_speed[sprite][0],
                        *list(boss.boss_projectile_group)[sprite].rect[1:4]))
                list(boss.boss_projectile_group)[sprite].update()
            lvl_gen.boss.boss_projectile_group.draw(windows.screen)

        if not cheatPanel:
            if (pygame.sprite.spritecollide(consts.hero, lvl_gen.thorngroup, False)
                    or pygame.sprite.spritecollide(consts.hero, lvl_gen.sloniks, False)
                    or pygame.sprite.spritecollide(consts.hero, boss.boss_group, False)):
                thing = ''
                consts.hero.end()
                lvl_gen.projectilespeed = []
                lvl_gen.nmeprojectilesgroup.empty()
                lvl_gen.updater()
                started = False
                game_over.game_over()
        if pygame.sprite.spritecollide(consts.hero, lvl_gen.triggergroup, False):
            if lvl == 2 and thing == 1:
                # lvl_gen.remover(lvl_gen.board.get_cell(consts.hero.get_coords()))
                # consts.hero.set_coords(consts.hero.get_coords()[0], consts.hero.get_coords()[1]
                # - lvl_gen.board.get_size())
                # lvl_gen.remover((8, 5), '=')
                # lvl_gen.remover((9, 5), '=')
                # lvl_gen.remover((10, 5), '=')
                # lvl_gen.remover((11, 5), '=')
                # lvl_gen.remover((12, 5), '=')
                # lvl_gen.remover((13, 5), '=')
                # lvl_gen.remover((14, 5), '=')
                # lvl_gen.remover((7, 4), 'F')
                pass
            elif lvl == 3:
                lvl_gen.remover(lvl_gen.board.get_cell(
                    list(pygame.sprite.spritecollide(consts.hero, lvl_gen.triggergroup, True))[0].rect[:2]))
                lvl_gen.toches.remove(lvl_gen.get_key(lvl_gen.toches.spritedict,
                                                      pygame.rect.Rect(int(lvl_gen.board.rev_get_cell((11, 10))[0]),
                                                                       int(lvl_gen.board.rev_get_cell((11, 10))[1]),
                                                                       lvl_gen.board.get_size(),
                                                                       lvl_gen.board.get_size())))
                lvl_gen.remover((11, 10))

        if not lvl_gen.sloniks:
            if lvl == 2 and thing == '':
                lvl_gen.remover((2, 7), 'C')
            elif lvl == 2 and thing == 1:
                lvl_gen.remover((8, 4), 'F')
            elif lvl == 3 and thing == 1:
                lvl_gen.remover((7, 4), 'S')
            elif lvl == 3 and thing == 2:
                consts.hero.end()
                thing = ''
                lvl_gen.updater()
                started = False
                record = starsChanger(lvl, current_seconds)
                if current_seconds < starsRecorder.get_seconds(lvl) or starsRecorder.get_seconds(lvl) == 0:
                    starsRecorder.push_record(lvl, 1, record, current_seconds)
                starsRecorder.push_lastRecord(lvl, record, current_seconds)
                game_complete.game_complete()

        if consts.runright or consts.runleft:
            if consts.runright:
                consts.hero.move(consts.xspeed * windows.k ** windows.fullscreen, 0)
            if consts.runleft:
                consts.hero.move(-consts.xspeed * windows.k ** windows.fullscreen, 0)
        else:
            consts.xspeed = 0
        consts.hero.update()
        lvl_gen.breakgroup.draw(windows.screen)
        lvl_gen.characters.draw(windows.screen)
        lvl_gen.sloniks.update()
        boss.boss_group.update()
        lvl_gen.sloniks.draw(windows.screen)
        lvl_gen.triggergroup.draw(windows.screen)
        lvl_gen.finale.draw(windows.screen)
        lvl_gen.untouches.draw(windows.screen)
        boss.boss_group.draw(windows.screen)
        pygame.draw.rect(windows.screen, '#000000',
                         (0, 0, windows.otstupx ** windows.fullscreen, windows.fullsize[1] ** windows.fullscreen))
        pygame.draw.rect(windows.screen, '#000000',
                         (windows.fullsize[0] - windows.otstupx, 0, windows.fullsize[0] ** windows.fullscreen,
                          windows.fullsize[1] ** windows.fullscreen))
        consts.clock.tick(consts.fps)
        pygame.display.flip()
