from raylibpy import *


background_texture = None


def load_background_texture():
    global background_texture
    background_texture = load_texture("assets/images/background.png")


def draw_background():
    if background_texture:
        screen_width = get_screen_width()
        screen_height = get_screen_height()

        # Orijinal sprite boyutları
        texture_width = background_texture.width
        texture_height = background_texture.height

        # Kaynak dikdörtgen (orijinal resmin tamamı)
        source = Rectangle(0, 0, texture_width, texture_height)

        # Hedef dikdörtgen (ekranı tam kaplayacak)
        dest = Rectangle(0, 0, screen_width, screen_height)

        draw_texture_pro(
            background_texture,
            source,
            dest,
            Vector2(0, 0),   # Origin = köşe
            0.0,             # Rotation
            WHITE
        )