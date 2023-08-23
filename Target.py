import pygame
from Collision_Object import Object

# Target class create moving targets,
# Player have to shoot targets,
# from Object, takes hitbox and drawing,


class Target(Object):
    def __init__(self, x_cord, y_cord, width, height):
        # method call: Object
        super().__init__(x_cord, y_cord, width, height, 'Target/target')
        # target acceleration
        self.acc = 2
        # maximum acceleration
        self.max_acc = 20
        # target move direction, 0 = down, 1 = up
        self.direction = 0

    def tick(self):
        # check if acceleration is bigger or equal to max acceleration
        # if is then target speed won't increase
        if self.acc >= self.max_acc:
            self.acc = self.max_acc

        # change move direction of target, by checking 'y' coordinate
        if self.direction == 0:
            self.y_cord += self.acc
            # checking if target is on bottom edge of the screen
            if self.y_cord >= 450:
                # then change direction and move up
                self.direction = 1
        elif self.direction == 1:
            self.y_cord -= self.acc
            #  checking if target is on upper edge of the screen
            if self.y_cord <= 60:
                #  then change direction and move down
                self.direction = 0

        # refreshing the hitbox
        self.hitbox_ob = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window):
        # drawing target
        Object.draw(self, window)
