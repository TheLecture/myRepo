import pygame
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()  # Initialize Pygame mixer

# Set up the display window
window_width = 1280
window_height = 720
windowGame = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shooter')

# Load and set the icon
icon_image = pygame.image.load("Assets/icon.jpeg")
pygame.display.set_icon(icon_image)

# Load the music file
music_file = os.path.abspath("Assets/battle_music.ogg")
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play(-1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
