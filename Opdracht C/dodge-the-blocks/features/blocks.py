from raylibpy import *
import random

# Blokinstellingen
block_width = 40
block_height = 40
block_speed = 200
spawn_interval = 0.6

blocks = []
spawn_timer = 0
difficulty_timer = 0


def update_blocks(dt):
    """Laat blokken vallen en voeg nieuwe toe wanneer nodig."""
    global spawn_timer, difficulty_timer, block_speed, spawn_interval

    # Nieuwe blok toevoegen
    spawn_timer += dt
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        x = random.randint(0, 800 - block_width)
        blocks.append([x, -block_height])  # Start net boven het scherm

    # Moeilijkheid verhogen
    difficulty_timer += dt
    if difficulty_timer >= 3:
        difficulty_timer = 0
        block_speed += 50
        if spawn_interval < 0.4:
            spawn_interval = 0.4

    # Blokken naar beneden laten bewegen
    for block in blocks:
        block[1] += block_speed * dt


def draw_blocks():
    """Teken alle  blokken op het scherm."""
    for block in blocks:
        draw_rectangle(int(block[0]), int(block[1]), block_width, block_height, RED)


def check_collision(player_x, player_y, player_width, player_height):
    """Controleer of een blok de speler raakt."""
    for block in blocks:
        block_x = block[0]
        block_y = block[1]

        if (block_x < player_x + player_width and
            block_x + block_width > player_x and
            block_y < player_y + player_height and
            block_y + block_height > player_y):
            return True  # betekent botsin

    return False  # betekent geen botsing


def reset_blocks():
    global blocks, block_speed, spawn_timer, spawn_interval, difficulty_timer
    blocks.clear()
    block_speed = 200
    spawn_interval = 1.2
    spawn_timer = 0
    difficulty_timer = 0
