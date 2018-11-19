import pygame
import os
import constants
from platform_scroller import *


# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText



# Game Fonts
font = "Retro.ttf"
font1 = "Blackfat Demo.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():

    menu = True
    selected = "start"
    background = pygame.image.load('images/preview.jpg')
    pygame.mixer.music.load('music/Intro Theme.wav')
    pygame.mixer.music.play(loops=-1)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    selected = "start"
                if event.key == pygame.K_LEFT:
                    selected = "control"
                if event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        main()
                    elif selected == "control":
                        control_screen()
                    elif selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background, (0, 0))
        title = text_format("SLIME SHUFFLE", font1, 90, constants.Orange)
        if selected == "start":
            text_start = text_format("START", font, 75, constants.White)
        else:
            text_start = text_format("START", font, 75,constants.Black)
        if selected == "control":
            text_control = text_format("Controls", font, 75, constants.White)
        else:
            text_control = text_format("Controls", font, 75,constants.Black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, constants.White)
        else:
            text_quit = text_format("QUIT", font, 75, constants.Black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        control_rect = text_control.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (constants.SCREEN_WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (constants.SCREEN_WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_control, (constants.SCREEN_HEIGHT / 4 - (control_rect[2] / 2), 300))
        screen.blit(text_quit, (constants.SCREEN_WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Slime Shuffle Menu")

#Initialize the Game
main_menu()
pygame.quit()
quit()