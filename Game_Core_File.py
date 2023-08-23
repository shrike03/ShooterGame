import sys

import pygame
from Background import Background
from Button import Button
from Player import Player
from Collision_Object import Object
from Target import Target
from Counting import Counting

# initializes Pygame library
pygame.init()
# display width
background_width = 1224
# display height
background_height = 646
# display resolution
resolution = (background_width, background_height)
# creating a game display
window = pygame.display.set_mode(resolution)

# game core


def core():

    # Method call: Background
    background = Background(resolution)
    # Method call: Player(x,y)
    player = Player(300, 486)
    # Method call: collision objects(x,y,width,height,image_name)
    structures = [
                  Object(120, 350, 200, 30, 'Static/platform'),
                  Object(800, 380, 200, 30, 'Static/platform'),
                  Object(670, 150, 120, 30, 'Static/platform'),
                  # display limits
                  Object(0, 630, 2000, 350, 'Static/platform'),
                  Object(-1, 0, 1, 646, 'Static/platform'),
                  Object(1224, 0, 1, 646, 'Static/platform')]

    # Method call: Target(x,y,width,height)
    targets = [Target(20, 20, 48, 50),
               Target(1160, 450, 48, 50)]
    # Method call: Counting
    counting = Counting()
    # controlling fps
    clock = pygame.time.Clock()
    #  value of maximum fps
    max_fps = 60
    # pause font
    p_font = pygame.font.SysFont("arial", 50)
    # pause text
    pause_txt = p_font.render('PAUSE', True, (255, 255, 255))
    # pause
    pause = False

    # main game loop
    while True:
        # limited to 60 fps
        clock.tick(max_fps) / 1000
        # quit the game, by using Escape, or closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            # restart the game by pressing 'r'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                core()
            # pause the game by pressing 'p'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                # change value pause, by pressing 'p'
                pause = not pause
                # display: pause
                window.blit(pause_txt, (550, 280))
                pygame.display.update()

        if pause:
            continue

        # check keyboard state
        key = pygame.key.get_pressed()
        # background frames change
        background.tick()
        # background draw
        background.draw(window)
        # counter draw
        counting.draw(window)
        # target drawing
        for target in targets:
            target.tick()
            target.draw(window)
        # collision objects drawing
        for structure in structures:
            structure.draw(window)

        # player drawing, and move
        player.draw(window)
        player.update(key, structures, targets, counting)
        # display refresh
        pygame.display.update()

# game menu


def menu():
    # loading buttons images
    play_button = Button(462, 124, "Images/Buttons/play_button.png")
    exit_button = Button(460, 384, "Images/Buttons/exit_button.png")
    while True:
        # quit the game, by using Escape, or closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        # go to game core
        if play_button.tick():
            core()
        # exit
        if exit_button.tick():
            sys.exit()

        # buttons drawing
        play_button.draw(window)
        exit_button.draw(window)
        # refreshing display
        pygame.display.update()


if __name__ == '__main__':
    menu()
