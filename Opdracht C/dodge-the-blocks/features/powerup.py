from raylibpy import *
import random

# Power-up instellingen
powerup_width = 40
powerup_height = 40
powerup_speed = 150
spawn_interval = 10.0

powerups = []
spawn_timer = 0


def update_powerups(dt):
    """Laat power-ups vallen en voeg nieuwe toe wanneer nodig."""
    global spawn_timer

    spawn_timer += dt
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        x = random.randint(0, 800 - powerup_width)
        powerups.append([x, -powerup_height])  # bovenaan starten

    for powerup in powerups:
        powerup[1] += powerup_speed * dt


def draw_powerups():
    """Teken alle power-ups op het scherm."""
    for powerup in powerups:
        draw_rectangle(int(powerup[0]), int(powerup[1]), powerup_width, powerup_height, GREEN)


def check_powerup_collision(player_x, player_y, player_width, player_height):
    """Controleer of een power-up de speler raakt."""
    for powerup in powerups:
        powerup_x = powerup[0]
        powerup_y = powerup[1]

        if (powerup_x < player_x + player_width and
            powerup_x + powerup_width > player_x and
            powerup_y < player_y + player_height and
            powerup_y + powerup_height > player_y):
            powerups.remove(powerup)
            return True

    return False


def reset_powerups():
    powerups.clear()
