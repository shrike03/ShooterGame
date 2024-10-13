import pygame
from Physics import Physics
from math import floor
from Shooting import Shoot


# Constructor code for Player class
# running animation
# inherits from Physics

class Player(Physics):
    def __init__(self, x_cord, y_cord):
        # Player coordinates
        self.x_cord = x_cord
        self.y_cord = y_cord
        # load player image, motionless, facing right side
        self.player_idle_d_R = pygame.image.load("Images/Player/player_1.png").convert_alpha()
        # load player image, motionless, facing left side
        self.player_idle_d_L = pygame.transform.flip(self.player_idle_d_R, True, False)
        # load player image, jumping, facing right side
        self.player_jump_d_R = pygame.image.load("Images/Player/player_6.png").convert_alpha()
        # load player image, jumping, facing left side
        self.player_jump_d_L = pygame.transform.flip(self.player_jump_d_R, True, False)
        # list of player images, running, facing right side, 'x' is frame number
        self.player_run_d_R = [(pygame.image.load(
            f"Images/Player/player_{x}.png").convert_alpha()) for x in range(3, 8)]
        # list of player images, running, facing left side, 'x' is frame number
        self.player_run_d_L = [(pygame.transform.flip(pygame.image.load(
            f"Images/Player/player_{x}.png"), True, False).convert_alpha()) for x in range(3, 8)]
        # Player dimensions used in Parent class: Physics
        width = self.player_idle_d_R.get_width()
        height = self.player_idle_d_R.get_height()
        # frame number used in run animation
        self.frame = 0
        # character vector, which defines Player image loading, 0 = right, 1 = left
        self.direction = 0
        # Call the constructor of the parent class
        # Physics(x_cord, y_cord, width, height, gravity, acceleration, maximum velocity,w,h )
        # defines hitbox with static structures
        # defines movement mechanics
        Physics.__init__(self, x_cord, y_cord, width, height, 0.8, 0.5, 7, -90, 0)

        # Initialize the Shoot class and create a list to store the player's shoots
        self.shoot = Shoot(self.x_cord, self.y_cord, self.direction)
        self.shoots = []
        # checking if mouse button is press
        self.press = False
        # improvement coordinates for shoots
        self.cord = 150

    # defines Player hitbox with structures
    # shooting
    # counting targets shoots
    # movement of the Player with use of keys
    def update(self, key, structures, targets, counting):

        self.physic_tick(structures)
        # improvement coordinates for shoots depending on Player direction
        if self.direction == 0:
            self.cord = 150
        else:
            self.cord = (-25)

        # One shoot per one mouse press
        if pygame.mouse.get_pressed()[0] and self.press is False:
            # creates shoot object, depending on Player coordinate
            self.shoot = Shoot(self.x_cord + self.cord, self.y_cord + 35, self.direction)
            # add shoot to the list
            self.shoots.append(self.shoot)
            self.press = True

        # shoot hitbox and counting targets hits
        for shoot in self.shoots:
            shoot.tick(targets,counting)                       
        if not pygame.mouse.get_pressed()[0]:
            self.press = False

        # if shoot object is beyond game window is removed from the list
        for shoot in self.shoots:
            if 0 >= shoot.x_cord or shoot.x_cord >= 1228:
                self.shoots.remove(shoot)

        # Player control
        # character move to the right after pressing 'a'
        if key[pygame.K_a] and self.vel_hor > self.max_vel * -1:
            self.vel_hor -= self.acc
            self.direction = 1

        # character move to the left after pressing 'd'
        if key[pygame.K_d] and self.vel_hor < self.max_vel:
            self.vel_hor += self.acc
            self.direction = 0

        # character jumps after pressing 'w'
        if key[pygame.K_w] and not self.jumping and self.vel_ver == 0:
            self.vel_ver += 20
            self.jumping = True

        # slowing down the Player if button 'a' or 'd' isn't pressed
        # rounded the speed so that the running animation wasn't infinite if acc is too small
        if not (key[pygame.K_a] or key[pygame.K_d]):
            if self.vel_hor > 0:
                self.vel_hor -= self.acc
                self.vel_hor = round(self.vel_hor, 1)
            if self.vel_hor < 0:
                self.vel_hor += self.acc
                self.vel_hor = round(self.vel_hor, 1)

    # drawing Player and shoot object
    def draw(self, window):

        # draw Player jumping
        if self.jumping:
            if self.direction == 0:
                window.blit(self.player_jump_d_R, (self.x_cord, self.y_cord))
            if self.direction == 1:
                window.blit(self.player_jump_d_L, (self.x_cord, self.y_cord))
        # draw Player running, floor return integer frame so animation is smooth
        # running animation use 5 frame which is determined in loop
        elif self.vel_hor != 0:
            if self.direction == 0:
                window.blit(self.player_run_d_R[floor(self.frame)], (self.x_cord, self.y_cord))
                self.frame += 0.15
                if self.frame >= 5:
                    self.frame = 0
            elif self.direction == 1:
                window.blit(self.player_run_d_L[floor(self.frame)], (self.x_cord, self.y_cord))
                self.frame += 0.15
                if self.frame >= 5:
                    self.frame = 0
        # draw Player in idle stance
        else:
            if self.direction == 0:
                window.blit(self.player_idle_d_R, (self.x_cord, self.y_cord))
            elif self.direction == 1:
                window.blit(self.player_idle_d_L, (self.x_cord, self.y_cord))

        # draw shoots
        for shoot in self.shoots:
            shoot.draw(window)
