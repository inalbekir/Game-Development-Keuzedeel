# features/sounds.py
from raylibpy import *

# Sound variables
background_music = None
sound_powerup = None
sound_explosion = None
sound_win = None
sound_lose = None
sound_level_up = None


def load_sounds():
    global background_music, sound_powerup, sound_explosion, sound_win, sound_lose, sound_level_up

    background_music = load_music_stream("assets/sounds/background.wav")
    play_music_stream(background_music)

    sound_powerup = load_sound("assets/sounds/powerup.wav")
    sound_explosion = load_sound("assets/sounds/explosion.wav")
    sound_win = load_sound("assets/sounds/won.mp3")
    sound_lose = load_sound("assets/sounds/lost.mp3")
    sound_level_up = load_sound("assets/sounds/levelup.wav")


def update_background_music():
    if background_music:
        update_music_stream(background_music)


def play_powerup_sound():

    if sound_powerup:
        play_sound(sound_powerup)


def play_explosion_sound():

    if sound_explosion:
        play_sound(sound_explosion)


def play_win_sound():

    if sound_win:
        play_sound(sound_win)


def play_lose_sound():
    if sound_lose:
        play_sound(sound_lose)


def play_level_up_sound():
    """Level up olduğunda çalan ses."""
    if sound_level_up:
        play_sound(sound_level_up)



def unload_sounds():
    global background_music, sound_powerup, sound_explosion, sound_win, sound_lose, sound_level_up

    unload_music_stream(background_music)
    unload_sound(sound_powerup)
    unload_sound(sound_explosion)
    unload_sound(sound_win)
    unload_sound(sound_lose)
    unload_sound(sound_level_up)
