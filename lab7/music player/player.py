import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player with Album Art")
font = pygame.font.SysFont(None, 24)

# Playlist with corresponding images
playlist = [
    {'song': 'adore.mp3', 'image': 'adore.png'},
    {'song': '8.mp3', 'image': '8.jpg'},
    {'song': 'Eva.mp3', 'image': 'Eva.jpg'}
]

current_track = 0

# Load and play selected track and show image
def play_track(track_index):
    pygame.mixer.music.load(playlist[track_index]['song'])
    pygame.mixer.music.play()

# Function to load and display the image
def display_image(track_index):
    image = pygame.image.load(playlist[track_index]['image'])
    image = pygame.transform.scale(image, (400, 200))
    screen.blit(image, (0, 100))

play_track(current_track)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_q:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                play_track(current_track)

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                play_track(current_track)

    screen.fill((30, 30, 30))

    instructions = [
        "Space - Play/Pause",
        "Q - Stop",
        "Right Arrow - Next",
        "Left Arrow - Previous"
    ]

    for i, text in enumerate(instructions):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (20, 25 * i + 10))

    # Display song-specific image
    display_image(current_track)

    pygame.display.flip()

pygame.quit()
sys.exit()
