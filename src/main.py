#main.py is the entry point of the game, responsible for initializing and combining the various components of the code
from ShooterGame import sys,pygame,Background,Control,Button,Counting,Player,Target, Object

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
# game menu
def menu():
     # Method call: Background
    background = Background(resolution,'Background/menu')
    # loading buttons images
    play_button = Button(462, 60, "Buttons/play_button","Buttons/play_button_b")
    control_button = Button(462, 256, "Buttons/control_button", "Buttons/control_button_b")
    exit_button = Button(462, 452, "Buttons/exit_button", "Buttons/exit_button_b")
    while True:
        # quit the game, by using Escape, or closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
        # go to game core
        if play_button.tick():
            core()
        # go to control panel
        if control_button.tick():
           control_panel()
        # exit
        if exit_button.tick():
            sys.exit()

        # background draw
        background.draw(window)
        # buttons drawing
        play_button.draw(window)
        control_button.draw(window)
        exit_button.draw(window)
        # refreshing display
        pygame.display.update()

def control_panel():
    # Method call: Background
    background = Background(resolution,'Background/menu')
    # Method call: Controls
    controls = Control()
    while True:
        # quit the game, by closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # back to the main menu by using Escape 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu()
                
        # background draw
        background.draw(window)
        # controls adding text
        controls.tick()
        # controls panel draw
        controls.draw(window)
        # refreshing display
        pygame.display.update()

# game core
def core():
    # Method call: Background
    background = Background(resolution,'Background/background')
    # Method call: Player(x,y)
    player = Player(300, 486)
    # Method call: collision objects(x,y,width,height,image_name)
    structures = [
                  Object(120, 350, 200, 30,  'Static/platform'),
                  Object(800, 380, 200, 30, 'Static/platform'),
                  Object(670, 150, 120, 30, 'Static/platform'),
                  # display limits
                  Object(0, 630, 2000, 350, 'Static/platform'),
                  Object(-1, 0, 1, 646, 'Static/platform'),
                  Object(1224, 0, 1, 646, 'Static/platform')]

    #Creating list targets and Method call: Target(x,y,width,height,list)
    targets=[]
    targets.append(Target(20, 20, 48, 50,targets))
    targets.append(Target(1160, 450, 48, 50, targets))
    # Method call: Counting
    counting = Counting()
    # controlling fps
    clock = pygame.time.Clock()
    #  value of maximum fps
    max_fps = 60
    # pause font
    p_font = pygame.font.SysFont('Sitka Small Bold', 50)
    # pause text
    pause_txt = p_font.render('PAUSE', True, (255, 255, 255))
    # pause
    pause = False

    # main game loop
    while True:
        # limited to 60 fps
        clock.tick(max_fps) / 1000
        # quit the game, by closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # back to the main menu by using Escape
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu()
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


if __name__ == '__main__':
    menu()
