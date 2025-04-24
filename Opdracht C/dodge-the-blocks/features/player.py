from raylibpy import *

# Spelerinstellingen
player_width = 50
player_height = 20
player_x = 375
player_y = 550
player_color = BLUE
player_speed = 300

boosted = False
boost_timer = 0.0


def update_player(dt):
    global player_x, boosted, boost_timer, player_speed

    if boosted:
        boost_timer += dt
        if boost_timer >= 3:
            player_speed = 300
            boosted = False
            boost_timer = 0

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


def get_player_rect():
    """Geeft de positie en grootte van de speler terug."""
    return player_x, player_y, player_width, player_height


def boost_player():
    global player_speed, boosted, boost_timer
    player_speed = 500
    boosted = True
    boost_timer = 0.0

