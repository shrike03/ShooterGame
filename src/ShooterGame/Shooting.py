from ShooterGame import pygame, Physics, Path
# Constructor code for Shoot class
# if the shoot object hits the target, the counter increases by 1, the shoot object is removed
# inherits from Physics

class Shoot(Physics):
    def __init__(self, x_cord, y_cord, direction):
        # shoot image
        self.image = self
        # creating path to folder Images
        images_path = Path(__file__).parent /"Assets" / "Images"
        # shoot image right vector, depends on Player direction
        self.right = pygame.image.load(str(images_path/"Bullet/bullet.png")).convert_alpha()
        # shoot image left vector, depends on Player direction
        self.left = pygame.transform.flip(self.right, True, False)
        # shoot object dimensions
        width = self.right.get_width()
        height = self.right.get_height()
        # shoot direction
        self.direction = direction
        # checking whether the target was hit, used in counting and target
        # allows adding new reaction for hit
        self.hit = False
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
            if self.hitbox_player.colliderect(target.hitbox_ob) and not self.hit:
                self.hit=True
                # remove the hit target
                targets.remove(target)
                 # + 1 to counter
                counting.tick(self.hit)
                target.new_target(self.hit)    
        self.hit = False

    def draw(self, window):
        # draw Shoot
        window.blit(self.image, (self.x_cord, self.y_cord))
