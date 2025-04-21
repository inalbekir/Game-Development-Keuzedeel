from raylibpy import *

# Scherminstellingen
WIDTH = 800  # Breedte van het venster
HEIGHT = 600  # Hoogte van het venster

# Spelerinstellingen
player_width = 50 # Breedte van de speler
player_height = 20 # Hoogte van de speler

# Positie van de speler (voor elke resolutie)
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50

player_color = BLUE

# Venster openen
init_window(WIDTH, HEIGHT, b"Dodge the Blocks")
set_target_fps(60)

# Game loop instellen
while not window_should_close():
    begin_drawing()  # Begin met tekenen
    clear_background(RAYWHITE)

    # Speler tekenen
    draw_rectangle(player_x, player_y, player_width, player_height, player_color)

    end_drawing()  # Teken alles op het scherm

# Venster sluiten
close_window()