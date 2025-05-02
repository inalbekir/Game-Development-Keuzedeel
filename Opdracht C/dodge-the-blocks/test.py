from raylibpy import *

init_window(800, 600, b"Test Sprite")
set_target_fps(60)

texture = load_texture("assets/images/test_block.png")
sprite_width = texture.width
sprite_height = texture.height

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)

    x = (get_screen_width() - sprite_width) / 2
    y = get_screen_height() * 0.8

    draw_texture(texture, int(x), int(y), WHITE)

    end_drawing()

unload_texture(texture)
close_window()