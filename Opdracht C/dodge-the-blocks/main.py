from raylibpy import *
from features.player import *

init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)

while not window_should_close():
    dt = get_frame_time()

    update_player(dt)

    begin_drawing()
    clear_background(RAYWHITE)
    draw_player()
    end_drawing()

close_window()