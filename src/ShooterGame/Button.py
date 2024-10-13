import pygame
#class defines button
#hitbox detection on mouse click
class Button:
    def __init__(self, x_cord, y_cord, grafika):
        #location coordinate
        self.x_cord = x_cord
        self.y_cord = y_cord
        #button image load
        self.grafika = pygame.image.load(grafika)
        self.height = self.grafika.get_height()
        self.width = self.grafika.get_width()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        # left mouse button click hitbox
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        window.blit(self.grafika, (self.x_cord, self.y_cord))