import pygame

import constants
import platforms


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()

        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()


    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.Blue)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)


    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x




# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/cave bg2.png").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.STONE_LEFT, 500, 500],
                 [platforms.STONE_MIDDLE, 570, 500],
                 [platforms.STONE_RIGHT, 640, 500],
                 [platforms.STONE_LEFT, 800, 400],
                 [platforms.STONE_MIDDLE, 870, 400],
                 [platforms.STONE_RIGHT, 940, 400],
                 [platforms.STONE_PLATFORM_LEFT, 1000, 500],
                 [platforms.STONE_PLATFORM_MIDDLE, 1070, 500],
                 [platforms.STONE_PLATFORM_RIGHT, 1140, 500],
                 [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                 [platforms.INVIS_BLOCK, 50, 0],
                 [platforms.INVIS_BLOCK, 50, 70],
                 [platforms.INVIS_BLOCK, 50, 140],
                 [platforms.INVIS_BLOCK, 50, 210],
                 [platforms.INVIS_BLOCK, 50, 280],
                 [platforms.INVIS_BLOCK, 50, 350],
                 [platforms.INVIS_BLOCK, 50, 420],
                 [platforms.INVIS_BLOCK, 50, 490],
                 [platforms.INVIS_BLOCK, 50, 560],
                 [platforms.INVIS_BLOCK, 50, 630],
                 [platforms.INVIS_BLOCK, 50, 700],
                 [platforms.INVIS_BLOCK, 50, 770],
                 [platforms.STONE_BLOCK, 2700, 0],
                 [platforms.STONE_BLOCK, 2700, 70],
                 [platforms.STONE_BLOCK, 2700, 350],
                 [platforms.STONE_BLOCK, 2700, 420],
                 [platforms.STONE_BLOCK, 2700, 490],
                 [platforms.STONE_BLOCK, 2700, 560],
                 [platforms.STONE_BLOCK, 2700, 630],
                 [platforms.STONE_BLOCK, 2700, 700],
                 [platforms.STONE_BLOCK, 2700, 770],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Adds custom moving platforms
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1600
        block.rect.y = 280
        block.boundary_left = 1600
        block.boundary_right = 2000
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2000
        block.rect.y = 280
        block.boundary_left = 2000
        block.boundary_right = 2399
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/rock.png").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -1700

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.STONE_PLATFORM_LEFT, 500, 550],
                 [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                 [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                 [platforms.INVIS_BLOCK, 50, 0],
                 [platforms.INVIS_BLOCK, 50, 70],
                 [platforms.INVIS_BLOCK, 50, 140],
                 [platforms.INVIS_BLOCK, 50, 210],
                 [platforms.INVIS_BLOCK, 50, 280],
                 [platforms.INVIS_BLOCK, 50, 350],
                 [platforms.INVIS_BLOCK, 50, 420],
                 [platforms.INVIS_BLOCK, 50, 490],
                 [platforms.INVIS_BLOCK, 50, 560],
                 [platforms.INVIS_BLOCK, 50, 630],
                 [platforms.INVIS_BLOCK, 50, 700],
                 [platforms.INVIS_BLOCK, 50, 770],
                 [platforms.STONE_PLATFORM_LEFT, 700, 450],
                 [platforms.STONE_PLATFORM_MIDDLE, 770, 450],
                 [platforms.STONE_PLATFORM_MIDDLE, 600, 350],
                 [platforms.STONE_PLATFORM_MIDDLE, 450, 250],
                 [platforms.STONE_PLATFORM_RIGHT, 500, 250],
                 [platforms.STONE_PLATFORM_LEFT, 500, 750],
                 [platforms.STONE_PLATFORM_MIDDLE, 570, 750],
                 [platforms.STONE_BLOCK, 400, 0],
                 [platforms.STONE_BLOCK, 400, 70],
                 [platforms.STONE_BLOCK, 400, 140],
                 [platforms.STONE_BLOCK, 400, 210],
                 [platforms.STONE_BLOCK, 400, 280],
                 [platforms.STONE_BLOCK, 400, 350],
                 [platforms.STONE_BLOCK, 800, 140],
                 [platforms.STONE_BLOCK, 800, 210],
                 [platforms.STONE_BLOCK, 800, 280],
                 [platforms.STONE_BLOCK, 800, 350],
                 [platforms.STONE_BLOCK, 800, 420],
                 [platforms.STONE_BLOCK, 800, 490],
                 [platforms.STONE_BLOCK, 800, 560],
                 [platforms.STONE_BLOCK, 800, 630],
                 [platforms.STONE_BLOCK, 800, 700],
                 [platforms.STONE_BLOCK, 800, 770],
                 [platforms.STONE_BLOCK, 950, 0],
                 [platforms.STONE_BLOCK, 950, 70],
                 [platforms.STONE_BLOCK, 950, 140],
                 [platforms.STONE_BLOCK, 950, 210],
                 [platforms.STONE_BLOCK, 950, 280],
                 [platforms.STONE_BLOCK, 950, 350],
                 [platforms.STONE_BLOCK, 950, 420],
                 [platforms.STONE_BLOCK, 950, 630],
                 [platforms.STONE_BLOCK, 950, 700],
                 [platforms.STONE_BLOCK, 950, 770],
                 [platforms.STONE_BLOCK, 1700, 210],
                 [platforms.STONE_BLOCK, 1700, 280],
                 [platforms.STONE_BLOCK, 1700, 350],
                 [platforms.STONE_BLOCK, 1700, 420],
                 [platforms.STONE_BLOCK, 1700, 490],
                 [platforms.STONE_BLOCK, 1700, 560],
                 [platforms.STONE_BLOCK, 1700, 630],
                 [platforms.STONE_BLOCK, 1700, 700],
                 [platforms.STONE_BLOCK, 1700, 770],
                 [platforms.STONE_BLOCK, 1900, 0],
                 [platforms.STONE_BLOCK, 1900, 70],
                 [platforms.STONE_BLOCK, 1900, 140],
                 [platforms.STONE_BLOCK, 1900, 210],
                 [platforms.STONE_BLOCK, 1900, 280],
                 [platforms.STONE_BLOCK, 1900, 350],
                 [platforms.STONE_BLOCK, 1900, 420],
                 [platforms.STONE_BLOCK, 1900, 630],
                 [platforms.STONE_BLOCK, 1900, 700],
                 [platforms.STONE_BLOCK, 1900, 770],

                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1200
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)



class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/Scene.jpg").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_LEFT, 500, 450],
                 [platforms.GRASS_MIDDLE, 570, 450],
                 [platforms.GRASS_RIGHT, 640, 450],
                 [platforms.INVIS_BLOCK, 50, 0],
                 [platforms.INVIS_BLOCK, 50, 70],
                 [platforms.INVIS_BLOCK, 50, 140],
                 [platforms.INVIS_BLOCK, 50, 210],
                 [platforms.INVIS_BLOCK, 50, 280],
                 [platforms.INVIS_BLOCK, 50, 350],
                 [platforms.INVIS_BLOCK, 50, 420],
                 [platforms.INVIS_BLOCK, 50, 490],
                 [platforms.INVIS_BLOCK, 50, 560],
                 [platforms.INVIS_BLOCK, 50, 630],
                 [platforms.INVIS_BLOCK, 50, 700],
                 [platforms.INVIS_BLOCK, 50, 770],
                 [platforms.STONE_BLOCK, 1800, 0],
                 [platforms.STONE_BLOCK, 1800, 70],
                 [platforms.STONE_BLOCK, 1800, 350],
                 [platforms.STONE_BLOCK, 1800, 420],
                 [platforms.STONE_BLOCK, 1800, 490],
                 [platforms.STONE_BLOCK, 1800, 560],
                 [platforms.STONE_BLOCK, 1800, 630],
                 [platforms.STONE_BLOCK, 1800, 700],
                 [platforms.STONE_BLOCK, 1800, 770],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 0
        block.rect.y = 300
        block.boundary_left = 0
        block.boundary_right = 1800
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_BLOCK)
        block.rect.x = 1400
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_BLOCK)
        block.rect.x = 900
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_BLOCK)
        block.rect.x = 1200
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_BLOCK)
        block.rect.x = 1320
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_BLOCK)
        block.rect.x = 700
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 570
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_04(Level):
    """ Definition for level 4. """

    def __init__(self, player):
        """ Create level 4. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/Dungeon_background.png").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                 [platforms.INVIS_BLOCK, 50, 0],
                 [platforms.INVIS_BLOCK, 50, 70],
                 [platforms.INVIS_BLOCK, 50, 140],
                 [platforms.INVIS_BLOCK, 50, 210],
                 [platforms.INVIS_BLOCK, 50, 280],
                 [platforms.INVIS_BLOCK, 50, 350],
                 [platforms.INVIS_BLOCK, 50, 420],
                 [platforms.INVIS_BLOCK, 50, 490],
                 [platforms.INVIS_BLOCK, 50, 560],
                 [platforms.INVIS_BLOCK, 50, 630],
                 [platforms.INVIS_BLOCK, 50, 700],
                 [platforms.INVIS_BLOCK, 50, 770],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_05(Level):
    """ Definition for level 5. """

    def __init__(self, player):
        """ Create level 5. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/Dungeon_background.png").convert()
        self.background.set_colorkey(constants.White)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_LEFT, 500, 500],
                 [platforms.GRASS_MIDDLE, 570, 500],
                 [platforms.GRASS_RIGHT, 640, 500],
                 [platforms.GRASS_LEFT, 800, 400],
                 [platforms.GRASS_MIDDLE, 870, 400],
                 [platforms.GRASS_RIGHT, 940, 400],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1070, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                 [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                 [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                 [platforms.INVIS_BLOCK, 50, 0],
                 [platforms.INVIS_BLOCK, 50, 70],
                 [platforms.INVIS_BLOCK, 50, 140],
                 [platforms.INVIS_BLOCK, 50, 210],
                 [platforms.INVIS_BLOCK, 50, 280],
                 [platforms.INVIS_BLOCK, 50, 350],
                 [platforms.INVIS_BLOCK, 50, 420],
                 [platforms.INVIS_BLOCK, 50, 490],
                 [platforms.INVIS_BLOCK, 50, 560],
                 [platforms.INVIS_BLOCK, 50, 630],
                 [platforms.INVIS_BLOCK, 50, 700],
                 [platforms.INVIS_BLOCK, 50, 770],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)