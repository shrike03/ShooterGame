from ShooterGame import pygame, Path
#class defines button
#hitbox detection on mouse click
class Button:
    def __init__(self, x_cord, y_cord, graphic,graphic_b):
        #location coordinate
        self.x_cord = x_cord
        self.y_cord = y_cord
        # creating path to folder Images
        images_path = Path(__file__).parent /"Assets" / "Images"
        #loading button image
        self.graphic = pygame.image.load(str(images_path/f'{graphic}.png'))
        #loading brighter button image
        self.graphic_b = pygame.image.load(str(images_path/f'{graphic_b}.png'))
        self.height = self.graphic.get_height()
        self.width = self.graphic.get_width()
        self.hover = False
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)


    def tick(self):
        # left mouse button click hitbox
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.hover=True
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.hover=False

    def draw(self, window):
        window.blit(self.graphic, (self.x_cord, self.y_cord))
        
        if self.hover==True:
            window.blit(self.graphic_b, (self.x_cord, self.y_cord))