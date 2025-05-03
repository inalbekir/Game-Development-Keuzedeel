from raylibpy import *

# Spelerinstellingen
player_x = 0
player_y = 0
player_width = 50
player_height = 20
player_speed = 300
player_scale = 1.3

boosted = False
boost_timer = 0.0
player_texture = None


def load_player_texture():
    global player_texture, player_dead_texture, player_won_texture
    global player_x, player_y, player_width, player_height

    # Normla
    image = load_image("assets/images/Pirate Bomb/Sprites/5-Enemy-Captain/1-Idle/1.png")
    player_texture = load_texture_from_image(image)
    unload_image(image)

    # Game Over sprite
    dead_image = load_image("assets/images/Pirate Bomb/Sprites/5-Enemy-Captain/11-Dead Ground/1.png")
    player_dead_texture = load_texture_from_image(dead_image)
    unload_image(dead_image)

    # Win sprite
    win_image = load_image("assets/images/Pirate Bomb/Sprites/5-Enemy-Captain/8-Scare Run/1.png")
    player_won_texture = load_texture_from_image(win_image)
    unload_image(win_image)

    player_width = player_texture.width * player_scale
    player_height = player_texture.height * player_scale

    player_x = get_screen_width() / 2 - player_width / 2
    player_y = get_screen_height() - player_height - 10


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
    if player_x > get_screen_width() - player_width:
        player_x = get_screen_width() - player_width


def draw_player():
    global player_texture
    if player_texture:
        draw_texture_ex(
            player_texture,
            Vector2(player_x, player_y),
            0.0,
            player_scale,
            WHITE
        )
    else:
        draw_text("GEEN TEXTUUR", 300, 300, 20, RED)


def get_player_rect():
    """Geeft een precieze, extra verkleinde hitbox van de speler terug."""
    hitbox_margin_horizontal = player_width * 0.6
    hitbox_margin_top = player_height * 0.25
    hitbox_margin_bottom = player_height * 0.1

    hitbox_x = player_x + (hitbox_margin_horizontal / 2)
    hitbox_y = player_y + hitbox_margin_top
    hitbox_width = player_width - hitbox_margin_horizontal
    hitbox_height = player_height - hitbox_margin_top - hitbox_margin_bottom

    return hitbox_x, hitbox_y, hitbox_width, hitbox_height


def boost_player():
    global player_speed, boosted, boost_timer
    player_speed = 500
    boosted = True
    boost_timer = 0.0


def draw_player_dead():
    if player_dead_texture:
        scale = player_scale + 2
        texture_width = player_dead_texture.width * scale
        texture_height = player_dead_texture.height * scale

        x = get_screen_width() / 2 - texture_width / 2
        y = get_screen_height() - texture_height - 10

        draw_texture_ex(
            player_dead_texture,
            Vector2(x, y),
            0.0,
            scale,
            GRAY
        )


def draw_player_win():
    if player_won_texture:
        scale = player_scale + 2
        texture_width = player_won_texture.width * scale
        texture_height = player_won_texture.height * scale

        x = get_screen_width() / 2 - texture_width / 2
        y = get_screen_height() - texture_height - 10

        draw_texture_ex(
            player_won_texture,
            Vector2(x, y),
            0.0,
            scale,
            GREEN
        )
