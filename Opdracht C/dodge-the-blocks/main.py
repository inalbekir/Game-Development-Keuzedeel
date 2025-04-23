from raylibpy import *
from features.player import *
from features.blocks import *

lives = 1

init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)

while not window_should_close():
    dt = get_frame_time()

    update_player(dt)
    update_blocks(dt)

    if check_collision(*get_player_rect()):
        print("BOTSING! Game Over.")
        break

    begin_drawing()
    clear_background(RAYWHITE)
    draw_player()
    draw_blocks()

    end_drawing()


close_window()