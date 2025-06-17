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
block_texture = None
block_scale = 1


def load_block_texture():
    global block_texture, block_width, block_scale, block_height
    image = load_image("assets/images/Pirate Bomb/Sprites/7-Objects/1-BOMB/1-Bomb Off/1.png")
    block_texture = load_texture_from_image(image)
    unload_image(image)

    block_width = block_texture.width * block_scale
    block_height = block_texture.height * block_scale


def update_blocks(dt):
    """Laat blokken vallen en voeg nieuwe toe wanneer nodig."""
    global spawn_timer, difficulty_timer, block_speed, spawn_interval

    # Nieuwe blok toevoegen
    spawn_timer += dt
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        x = random.randint(0, int(get_screen_width() - block_width))
        blocks.append([x, -block_height])  # Start net boven het scherm

    # Moeilijkheid verhogen
    difficulty_timer += dt
    if difficulty_timer >= 10:
        difficulty_timer = 0
        block_speed += 100
        if spawn_interval < 0.4:
            spawn_interval = 0.4

    # Blokken naar beneden laten bewegen
    for block in blocks:
        block[1] += block_speed * dt


def draw_blocks():
    for block in blocks:
        x = int(block[0])
        y = int(block[1])
        if block_texture:
            draw_texture_ex(
                block_texture,
                Vector2(x, y),
                0.0,
                block_scale,
                WHITE
            )
        else:
            draw_rectangle(x, y, block_width, block_height, RED)  # fallback


def check_collision(player_x, player_y, player_width, player_height):
    """Controleer of een blok de speler raakt met verkleinde hitbox."""
    for block in blocks:
        block_x = block[0]
        block_y = block[1]

        # 🔽 Hitbox marges (ayarlar)
        margin_x = block_width * 0.7    # %20 sağ/sol kenar boşluğu
        margin_y = block_height * 0.2   # %20 üst/alt boşluk

        # 🔽 Daraltılmış blok hitbox koordinatları
        hitbox_x = block_x + margin_x / 2
        hitbox_y = block_y + margin_y / 2
        hitbox_width = block_width - margin_x
        hitbox_height = block_height - margin_y

        if (hitbox_x < player_x + player_width and
            hitbox_x + hitbox_width > player_x and
            hitbox_y < player_y + player_height and
            hitbox_y + hitbox_height > player_y):
            return True

    return False


def reset_blocks():
    global blocks, block_speed, spawn_timer, spawn_interval, difficulty_timer
    blocks.clear()
    block_speed = 200
    spawn_interval = 1.2
    spawn_timer = 0
    difficulty_timer = 0
