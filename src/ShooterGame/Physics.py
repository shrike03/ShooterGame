import pygame

# class defines Physics
# defines movemant mechanics (moving in Cartesian coordinates, acceleration, velocity)
# defines hitbox
# defines gravity

class Physics:
    def __init__(self, x_cord, y_cord, width, height, grav, acc, max_vel, w, h):
        # coordinates
        self.x_cord = x_cord
        self.y_cord = y_cord
        # dimensions
        self.width = width
        self.height = height
        # a value that changes the width of the hitbox
        self.w = w
        # a value that changes the height of the hitbox
        self.h = h
        # defines hitbox rect
        self.hitbox_play = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        # resize hitbox rectangle
        self.hitbox_player = self.hitbox_play.inflate(self.w, self.h)
        # maximum velocity
        self.max_vel = max_vel
        # initial vertical velocity value
        self.vel_ver = 0
        # initial vertical horizontal value
        self.vel_hor = 0
        # acceleration
        self.acc = acc
        # gravity
        self.grav = grav
        # precious coordinate
        self.previous_x = x_cord
        self.previous_y = y_cord
        # maximum jumping height
        self.max_jumping = 20
        # boolean variable
        self.jumping = False

    # defines movement
    # defines hitbox
    def physic_tick(self, structures):
        # movement horizontal
        self.x_cord += self.vel_hor
        # movement vertical
        self.y_cord -= self.vel_ver
        # gravity mechanism
        self.vel_ver -= self.grav
        # refreshing the hitbox
        self.hitbox_play = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.hitbox_player = self.hitbox_play.inflate(self.w, self.h)

        # hitbox with structure
        for structure in structures:
            if structure.hitbox_ob.colliderect(self.hitbox_player):
                # hitbox to the right
                if self.x_cord + self.width >= structure.x_cord + 51 > self.previous_x + self.width:
                    self.x_cord = self.previous_x
                    self.vel_hor = 0
                # hitbox to the left
                if self.x_cord <= structure.x_cord + structure.width - 51 < self.previous_x:
                    self.x_cord = self.previous_x
                    self.vel_hor = 0
                # hitbox from the bottom
                if self.y_cord + self.height >= structure.y_cord + 1 > self.previous_y + self.height:
                    self.y_cord = self.previous_y
                    self.vel_ver = 0
                    # if character stands then can jump
                    self.jumping = False
                # hitbox from above
                if self.y_cord <= structure.y_cord + structure.height - 1 < self.previous_y:
                    self.y_cord = self.previous_y
                    self.vel_ver = 0
        # returning the previous coordinates
        self.previous_x = self.x_cord
        self.previous_y = self.y_cord
