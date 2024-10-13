from ShooterGame import pygame, random, Object
# Target class create moving targets,
# Player have to shoot targets,
# from Object, takes hitbox and drawing,

class Target(Object):
    def __init__(self, x_cord, y_cord, width, height, targets):
        # method call: Object
        super().__init__(x_cord, y_cord, width, height, 'Target/target')
        # target acceleration
        self.acc = 2
        # maximum acceleration
        self.max_acc = 20
        # target move direction, 0 = down, 1 = up
        self.direction = 0
        self.targets = targets

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
    #Definition responsible for creating new object
    def new_target(self,hit):
        #checking if target is hit, atribute took from Shooting Class
        if hit==True:
                # creating new target depend on which is hit
            if self.x_cord == 1160:
                # increasing the speed of the new target
                new_acc = self.acc + 1
                # Initialize the Target class (x_cord, y_cord, width, height)
                new_target = Target(1160, random.randint(60, 600), 48, 50,self.targets)
                new_target.acc = new_acc
                # adding target to list
                self.targets.append(new_target)
            if self.x_cord == 20:
                new_acc = self.acc + 1
                new_target = Target(20, random.randint(60, 600), 48, 50, self.targets)
                new_target.acc = new_acc
                self.targets.append(new_target)      

    def draw(self, window):
        # drawing target
        Object.draw(self, window)
