from features.player import *
from features.blocks import *
from features.powerup import *
from features.background import *
from features.sounds import *


init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)

init_audio_device()


def run_game():
    global game_won

    game_over = False
    game_won = False

    lives = 1
    score = 0
    score_timer = 0

    load_sounds()

    load_player_texture()
    load_block_texture()
    load_powerup_texture()
    load_background_texture()

    while not window_should_close() and not game_over:

        dt = get_frame_time()

        update_background_music()
        update_player(dt)
        update_blocks(dt)
        update_powerups(dt)

        if check_collision(*get_player_rect()):
            print("BOTSING! Game Over.")
            game_over = True
            play_explosion_sound()
            play_lose_sound()
            return "lose"  #  burası onemli


        if check_powerup_collision(*get_player_rect()):
            print("Power-up gepakt!")
            boost_player()
            play_powerup_sound()

        score_timer += dt
        if score_timer >= 3.0:
            score += 1
            score_timer = 0

            if score >= 3:
                print("YOU WIN!")
                game_won = True
                play_win_sound()
                return "win"  # <-- burası önemli

        begin_drawing()
        clear_background(RAYWHITE)
        draw_background()

        draw_text(f"Levens: {lives}", 10, 10, 20, RED)
        draw_text(f"Score: {score}", 10, 35, 20, RED)

        draw_player()
        draw_blocks()
        draw_powerups()

        end_drawing()


# 🟢 BAŞLANGIÇ: Sonsuz döngü içinde sürekli oyun başlat
while True:
    result = run_game()  # run_game() "win" veya "lose" döndürecek

    if result == "win":
        while not window_should_close():
            begin_drawing()
            draw_background()
            draw_player_win()
            draw_text("YOU WIN", 220, 250, 80, GREEN)
            draw_text("'ESC' om af te sluiten  \n'R' om opnieuw te beginnen", 10, 10, 20, BLACK)
            end_drawing()

            if is_key_down(KEY_ESCAPE):
                unload_sounds()
                close_audio_device()
                close_window()
                exit()

            if is_key_pressed(KEY_R):
                reset_blocks()
                reset_powerups()
                break  # 🔁 dıştaki while True'ya dönüp oyunu yeniden başlatır

    elif result == "lose":
        while not window_should_close():
            begin_drawing()
            draw_background()
            draw_player_dead()
            draw_text("GAME OVER", 160, 250, 80, RED)
            draw_text("'ESC' om af te sluiten  \n'R' om opnieuw te beginnen", 10, 10, 20, BLACK)
            end_drawing()

            if is_key_down(KEY_ESCAPE):
                unload_sounds()
                close_audio_device()
                close_window()
                exit()

            if is_key_pressed(KEY_R):
                reset_blocks()
                reset_powerups()
                break  # 🔁 dıştaki while True'ya dönüp oyunu yeniden başlatır
