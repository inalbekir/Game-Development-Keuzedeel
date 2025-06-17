# main.py
from features.player import *
from features.blocks import *
from features.powerup import *
from background import *
from features.sounds import *


init_window(800, 600, b"Dodge the Blocks")
set_target_fps(60)
init_audio_device()
load_background_texture()

if not show_start_screen():
    close_window()
    exit()


def run_game():
    global game_won

    game_over = False
    game_won = False

    lives = 1
    score = 0
    score_timer = 0

    # ⏳ Yeni zamanlayıcılar
    level_up_display_time = 0.0
    powerup_display_time = 0.0

    load_sounds()
    load_player_texture()
    load_block_texture()
    load_powerup_texture()

    while not window_should_close() and not game_over:

        dt = get_frame_time()

        update_background_music()
        update_player(dt)
        update_blocks(dt)
        update_powerups(dt)

        # 💣 Çarpışma kontrolü
        if check_collision(*get_player_rect()):
            print("BOTSING! Game Over.")
            game_over = True
            play_explosion_sound()
            play_lose_sound()
            return "lose"

        # 🚀 Power-Up kontrolü
        if check_powerup_collision(*get_player_rect()):
            print("Power-up gepakt!")
            boost_player()
            play_powerup_sound()
            powerup_display_time = 2.0  # 2 saniye boyunca ekranda kalacak

        # ⏳ Level Up kontrolü
        score_timer += dt
        if score_timer >= 10.0:
            score += 1
            score_timer = 0
            level_up_display_time = 2.0  # 2 saniye boyunca ekranda kalacak
            play_level_up_sound()  # Ses efekti çalınıyor

            if score >= 5:
                print("YOU WIN!")
                game_won = True
                play_win_sound()
                return "win"

        # ⏳ Sayaçları azalt
        if level_up_display_time > 0:
            level_up_display_time -= dt

        if powerup_display_time > 0:
            powerup_display_time -= dt

        begin_drawing()
        clear_background(RAYWHITE)
        draw_background()

        draw_text(f"Levens: {lives}", 10, 10, 20, RED)
        draw_text(f"Score: {score}", 10, 35, 20, RED)

        # 🎉 Level Up yazdır
        if level_up_display_time > 0:
            draw_text("LEVEL UP!", 10, 60, 20, YELLOW)

        # 🚀 Power-Up yazdır
        if powerup_display_time > 0:
            draw_text("SPEED BOOST!", 10, 90, 20, ORANGE)

        draw_player()
        draw_blocks()
        draw_powerups()

        end_drawing()


# 🟢 BAŞLANGIÇ: Sonsuz döngü içinde sürekli oyun başlat
while True:
    result = run_game()

    if result == "win":
        while not window_should_close():
            begin_drawing()
            draw_background()
            draw_logo()
            draw_player_win()
            draw_text("YOU WIN", 220, 230, 80, GREEN)
            draw_text("Druk op ESC om af te sluiten  \nDruk op R om opnieuw te beginnen", 10, 10, 20, WHITE)
            end_drawing()

            if is_key_down(KEY_ESCAPE):
                unload_sounds()
                close_audio_device()
                close_window()
                exit()

            if is_key_pressed(KEY_R):
                reset_blocks()
                reset_powerups()
                break

    elif result == "lose":
        while not window_should_close():
            begin_drawing()
            draw_background()
            draw_logo()
            draw_player_dead()
            draw_text("GAME OVER", 160, 230, 80, RED)
            draw_text("Druk op ESC om af te sluiten  \nDruk op R om opnieuw te beginnen", 10, 10, 20, WHITE)
            end_drawing()

            if is_key_down(KEY_ESCAPE):
                unload_sounds()
                close_audio_device()
                close_window()
                exit()

            if is_key_pressed(KEY_R):
                reset_blocks()
                reset_powerups()
                break