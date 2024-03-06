import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((230, 230))
done = False
songs = ['songs/1.mp3',
         'songs/2.mp3',
         'songs/3.mp3',]
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
bg = pygame.image.load('/Users/daniil/Desktop/cods/lab07/images/player1.jpeg')
screen.blit(bg, (0, 0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True

    pygame.display.flip()