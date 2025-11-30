import pygame  # Import the pygame library, which can handle sounds, music, and more

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pygame

# Initialize the mixer module in pygame (used for playing sounds)
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("tmp.mp3")

# Start playing the loaded music
pygame.mixer.music.play()

# Keep the program running until the music finishes
while pygame.mixer.music.get_busy():  # get_busy() returns True while the music is playing
    pygame.time.Clock().tick(10)      # Pause briefly to avoid using too much CPU