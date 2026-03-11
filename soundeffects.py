import pygame

pygame.mixer.set_num_channels(32)

def play_sound(sound):
    if sound == pew_sound:
        laser_channel = pygame.mixer.Channel(0) 
        laser_channel.play(pew_sound)
    else:
        channel = pygame.mixer.find_channel(True)
        channel.play(sound)

pew_sound = pygame.mixer.Sound("assets/audio/pew.wav")
boom_sound = pygame.mixer.Sound("assets/audio/boom.wav")
womp_womp_sound = pygame.mixer.Sound("assets/audio/wompwomp.wav")
good_job_sound = pygame.mixer.Sound("assets/audio/goodjob.wav")
warrior_sound = pygame.mixer.Sound("assets/audio/warrior.wav")
hero_sound = pygame.mixer.Sound("assets/audio/hero.wav")
champion_sound = pygame.mixer.Sound("assets/audio/champion.wav")