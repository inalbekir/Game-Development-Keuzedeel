from features.player import *
from features.blocks import *
from features.powerup import *
from features.background import *


init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)


def run_game():
    global player_texture
    global block_texture

    game_over = False
    lives = 1
    score = 0
    score_timer = 0

    load_player_texture()
    load_block_texture()
    load_powerup_texture()
    load_background_texture()

    while not window_should_close() and not game_over:

        dt = get_frame_time()


        update_player(dt)
        update_blocks(dt)
        update_powerups(dt)

        if check_collision(*get_player_rect()):
            print("BOTSING! Game Over.")
            game_over = True

        if check_powerup_collision(*get_player_rect()):
            print("Power-up gepakt!")
            boost_player()


        score_timer += dt
        if score_timer >= 3.0:
            score += 1
            score_timer = 0


        begin_drawing()
        clear_background(RAYWHITE)
        draw_background()

        draw_text(f"Levens: {lives}", 10, 10, 20, RED)
        draw_text(f"Score: {score}", 10, 35, 20, RED)

        draw_player()
        draw_blocks()
        draw_powerups()

        end_drawing()


run_game()
# Game over scherm
while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text("GAME OVER", 290, 250, 40, RED)
    draw_text("Druk op ESC om af te sluiten", 260, 310, 20, BLACK)
    draw_text("OF", 400, 345, 15, BLACK)
    draw_text("Druk op R om opnieuw te beginnen", 250, 370, 20, BLACK)
    end_drawing()

    if is_key_down(KEY_ESCAPE):
        break

    if is_key_pressed(KEY_R):
        reset_blocks()
        reset_powerups()
        run_game()

close_window()
