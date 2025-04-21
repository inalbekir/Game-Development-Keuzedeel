from raylibpy import *

# Spelerinstellingen
player_width = 50
player_height = 20
player_x = 375
player_y = 550
player_color = BLUE
player_speed = 300

def update_player(dt):
    global player_x
    if is_key_down(KEY_LEFT):
        player_x -= player_speed * dt
    if is_key_down(KEY_RIGHT):
        player_x += player_speed * dt

    # Speler binnen scherm houden
    if player_x < 0:
        player_x = 0
    if player_x > 800 - player_width:
        player_x = 800 - player_width

def draw_player():
    draw_rectangle(player_x, player_y, player_width, player_height, player_color)