from raylibpy import *


background_texture = None
logo_texture = None


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



def show_start_screen():

    while not window_should_close():
        begin_drawing()
        clear_background(RAYWHITE)
        draw_background()
        draw_logo()

        draw_text("DODGE THE BLOCKS", 185, 250, 40, RED)
        draw_text("Druk op ENTER om te beginnen", 10, 10, 20, WHITE)

        end_drawing()

        if is_key_pressed(KEY_ENTER):
            return True
        if is_key_pressed(KEY_ESCAPE):
            return False





def draw_logo():
    global logo_texture
    if not logo_texture:
        logo_texture = load_texture("assets/images/logo.png")

    # Logoyu çiz
    draw_texture_ex(logo_texture, Vector2(515, 180), 0.0, 3, WHITE)

    # Yanına yazı çiz (slogan gibi)
    draw_text("BEST EDUCATION", 220, 190, 30, DARKBLUE)
    draw_text("Wij lanceren je de toekomst in!", 170, 320, 30, GOLD)
