import pygame
import constants
import levels
from player import Player


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


def control_screen():

    menu = True
    selected = "play"
    background = pygame.image.load('images/preview1.jpg')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    font = "Retro.ttf"
    font1 = "Blackfat Demo.ttf"
    clock = pygame.time.Clock()
    FPS = 30
    pygame.mixer.music.load('music/Ove Melaa - Dark Loop.ogg')
    pygame.mixer.music.play(loops=-1)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "play"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "play":
                        main()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background, (0, 0))
        title = text_format("Controls: Arrow Keys = Movement", font1, 35, constants.White)
        title1 = text_format("Spacebar = Drop Down Midair", font1, 35, constants.White)
        if selected == "play":
            text_play = text_format("Play", font, 75, constants.White)
        else:
            text_play = text_format("Play", font, 75,constants.Black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, constants.White)
        else:
            text_quit = text_format("QUIT", font, 75, constants.Black)

        title_rect=title.get_rect()
        start_rect=text_play.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (constants.SCREEN_WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(title1, (constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 140))
        screen.blit(text_play, (constants.SCREEN_WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (constants.SCREEN_WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Slime Shuffle Menu")


def victory_screen():

    menu = True
    selected = "replay"
    background = pygame.image.load('images/Victory_screen.jpg')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    font = "Retro.ttf"
    font1 = "Blackfat Demo.ttf"
    clock = pygame.time.Clock()
    FPS = 30
    pygame.mixer.music.load('music/cool theme.wav')
    pygame.mixer.music.play(loops=-1)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "replay"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "replay":
                        main()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background, (0, 0))
        title = text_format("You Shuffled to Victory!", font1, 75, constants.White)
        if selected == "replay":
            text_replay = text_format("Replay", font, 75, constants.White)
        else:
            text_replay = text_format("Replay", font, 75,constants.Black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, constants.White)
        else:
            text_quit = text_format("QUIT", font, 75, constants.Black)

        title_rect=title.get_rect()
        start_rect=text_replay.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (constants.SCREEN_WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_replay, (constants.SCREEN_WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (constants.SCREEN_WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Slime Shuffle Menu")


def game_over():

    menu = True
    selected = "retry"
    background = pygame.image.load('images/background_03.png')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    font = "Retro.ttf"
    clock = pygame.time.Clock()
    FPS = 30
    pygame.mixer.music.load('music/wyver9_Boss_main(8-bit).wav')
    pygame.mixer.music.play(loops=-1)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "retry"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "retry":
                        main()
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(background, (0, 0))
        title = text_format("YOU RAN OUT OF TIME!", font, 90, constants.Red)
        if selected == "retry":
            text_start = text_format("Retry", font, 75, constants.White)
        else:
            text_start = text_format("Retry", font, 75,constants.Black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, constants.White)
        else:
            text_quit = text_format("QUIT", font, 75, constants.Black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (constants.SCREEN_WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (constants.SCREEN_WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (constants.SCREEN_WIDTH/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Slime Shuffle Menu")

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 25)
    pygame.display.set_caption("Slime Shuffle")

    # Limit to 60 frames per second
    frame_count = 0
    frame_rate = 60
    start_time = 60
    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    #level_list.append(levels.Level_04(player))
    #level_list.append(levels.Level_05(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #Plays BGM
    pygame.mixer.music.load('music/Memoraphile - Spooky Dungeon.wav')
    pygame.mixer.music.play(loops=-1)

    # -------- Main Program Loop -----------
    while not done:
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0
            game_over()


        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
        seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
        output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
        text = font.render(output_string, True, constants.White)
        screen.blit(text, [50, 50])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1

        # Limit frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.drop()
                if event.key == pygame.K_ESCAPE:
                    victory_screen()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()


        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        screen.blit(text, [50, 50])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()