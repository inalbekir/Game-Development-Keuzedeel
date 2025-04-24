from raylibpy import *
from features.player import *
from features.blocks import *

game_over = False
lives = 1

init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)

while not window_should_close() and not game_over:

    dt = get_frame_time()

    update_player(dt)
    update_blocks(dt)

    if check_collision(*get_player_rect()):
        print("BOTSING! Game Over.")
        game_over = True

    begin_drawing()
    clear_background(RAYWHITE)
    draw_text(f"Levens: {lives}", 10, 10, 20, DARKGRAY)
    draw_player()
    draw_blocks()

    end_drawing()

# Game over scherm
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_text("GAME OVER", 290, 250, 40, RED)
    draw_text("Druk op ESC om af te sluiten", 260, 310, 20, WHITE)
    end_drawing()

    if is_key_down(KEY_ESCAPE):  # beter dan key_pressed
        break


close_window()