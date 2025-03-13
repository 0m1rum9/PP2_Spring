import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

music_directory = '/./home/user/PP2_Spring/lab7/music'
os.chdir(music_directory)

music_files = [file for file in os.listdir() if file.endswith(".mp3")]

current_track = 0
current_track = (current_track + 1) % len(music_files)
paused = False

pygame.mixer.music.load(music_files[current_track])

font = pygame.font.Font(None, 24)

kaif = pygame.image.load("../kaif.jpg")

kaif = pygame.transform.scale(kaif, (200, 200))

running = True
while running:
    # pygame.mixer.music.load(music_files[current_track])
    # pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
    
    screen.fill((255, 255, 255))
    instructions = font.render("Spacebar: Play/Pause, Left Arrow: Previous, Right Arrow: Next", True, (0, 0, 0))
    screen.blit(instructions, (10, 10))

    screen.blit(kaif, (150, 100))

    pygame.display.flip()

pygame.quit()
