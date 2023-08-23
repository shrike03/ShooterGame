import pygame
import random
from Physics import Physics
from Target import Target

# Constructor code for Shoot class
# if the shoot object hits the target, the counter increases by 1, the shoot object is removed
# inherits from Physics


class Shoot(Physics):
    def __init__(self, x_cord, y_cord, direction):
        # shoot image
        self.image = self
        # shoot image right vector, depends on Player direction
        self.right = pygame.image.load("Images/Bullet/bullet.png").convert_alpha()
        # shoot image left vector, depends on Player direction
        self.left = pygame.transform.flip(self.right, True, False)
        # shoot object dimensions
        width = self.right.get_width()
        height = self.right.get_height()
        # shoot direction
        self.direction = direction
        # Call the constructor of the parent class
        # Physics(x_cord, y_cord, width, height, gravity, acceleration, maximum velocity)
        # defines hitbox
        super().__init__(x_cord, y_cord, width, height, 0, 2, 2, 0, 0)

    def tick(self, targets, counting):
        self.physic_tick(targets)

        # move depending on direction
        if self.direction == 0:
            self.vel_hor += self.acc
            self.image = self.right
        elif self.direction == 1:
            self.vel_hor -= self.acc
            self.image = self.left

        # hitbox for shooting target
        for target in targets:
            if self.hitbox_player.colliderect(target.hitbox_ob):
                # remove the hit target
                targets.remove(target)
                # + 1 to counter
                counting.tick()
                # creating new target depend on which is hit
                if target.x_cord == 1160:
                    # increasing the speed of the new target
                    new_acc = target.acc + 1
                    # Initialize the Target class (x_cord, y_cord, width, height)
                    target = Target(1160, random.randint(60, 600), 48, 50)
                    target.acc = new_acc
                    # adding target to list
                    targets.append(target)
                if target.x_cord == 20:
                    new_acc = target.acc + 1
                    target = Target(20, random.randint(60, 600), 48, 50)
                    target.acc = new_acc
                    targets.append(target)

    def draw(self, window):
        # draw Shoot
        window.blit(self.image, (self.x_cord, self.y_cord))
