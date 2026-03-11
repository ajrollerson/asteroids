import os

import pygame
pygame.init()
pygame.mixer.init()
from soundeffects import *
import sys

from constants import *
from player import *
from text import *
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ore import Ore


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")   

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ores = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Ore.containers = (ores, drawable, updatable)

    player = Player(x, y)
    asteroidfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    text_font = pygame.font.SysFont(None, 60, bold = True)
    score = 0
    game_over = False


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        if game_over == False:
            draw_text(score_text(score), screen, text_font, "white", 1000, 100)
            updatable.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print(final_score_text(score))
                    game_over = True
                    game_end_start = pygame.time.get_ticks()
                    if score < 1000:
                        play_sound(womp_womp_sound)
                    elif 1000 <= score < 2500:
                        play_sound(good_job_sound)
                    elif 2500 <= score < 4000:
                        play_sound(warrior_sound)
                    elif 4000 <= score < 7500:
                        play_sound(hero_sound)
                    elif score >= 7500:
                        play_sound(champion_sound)
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
                        score += 10
            for ore in ores:
                if ore.collides_with(player):
                    if ore.ore_type == "cool_crystal":
                        player.player_shoot_cooldown_base -= 0.02
                    if ore.ore_type == "lasor_crystal":
                        player.player_shoot_speed += 5
                    if ore.ore_type == "score":
                        score += 50
                    if ore.ore_type == "radioactive":
                        score += 100
                    ore.kill()
                for shot in shots:
                    if ore.collides_with(shot):
                        if ore.ore_type == "cool_crystal":
                            player.player_shoot_cooldown_base -= 0.02
                        if ore.ore_type == "lasor_crystal":
                            player.player_shoot_speed += 5
                        if ore.ore_type == "score":
                            score += 50
                        if ore.ore_type == "radioactive":
                            score += 100
                        ore.kill()
            for object in drawable:
                object.draw(screen)
        else:
            draw_text(final_score_text(score), screen, text_font, "white", 350, 320) 
            if pygame.time.get_ticks() - game_end_start > 15000:
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
