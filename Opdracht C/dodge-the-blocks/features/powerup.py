from raylibpy import *
import random

# Power-up instellingen
powerup_width = 40
powerup_height = 40
powerup_speed = 150
spawn_interval = 10.0

powerups = []
spawn_timer = 0
powerup_texture = None
powerup_scale = 2



def load_powerup_texture():
    global powerup_texture, powerup_width, powerup_height

    image = load_image("assets/images/Pirate Bomb/Sprites/7-Objects/12-Other Objects/Green Bottle.png")
    powerup_texture = load_texture_from_image(image)
    unload_image(image)

    powerup_width = powerup_texture.width * powerup_scale
    powerup_height = powerup_texture.height * powerup_scale


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
    for powerup in powerups:
        x = int(powerup[0])
        y = int(powerup[1])
        if powerup_texture:
            draw_texture_ex(powerup_texture, Vector2(x, y), 0.0, powerup_scale, WHITE)
        else:
            draw_rectangle(x, y, int(powerup_width), int(powerup_height), GREEN)  # Fallback


def check_powerup_collision(player_x, player_y, player_width, player_height):
    """Controleer of een power-up de speler raakt met kleinere hitbox."""
    for powerup in powerups:
        powerup_x = powerup[0]
        powerup_y = powerup[1]

        # 🔧 Hitbox marges instellen (verkleint van alle kanten)
        margin_x = powerup_width * 0.3
        margin_y = powerup_height * 0.3

        hitbox_x = powerup_x + margin_x / 2
        hitbox_y = powerup_y + margin_y / 2
        hitbox_width = powerup_width - margin_x
        hitbox_height = powerup_height - margin_y

        if (hitbox_x < player_x + player_width and
            hitbox_x + hitbox_width > player_x and
            hitbox_y < player_y + player_height and
            hitbox_y + hitbox_height > player_y):
            powerups.remove(powerup)
            return True

    return False


def reset_powerups():
    powerups.clear()
