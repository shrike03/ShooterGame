import pygame

# image width = 7344
# class defines scrolling backgrounds,
# speed background = 2 frames per second


class Background:
    def __init__(self, resolution):
        # background image load
        self.image = pygame.image.load("Images/Background/background.png").convert()
        # rect to represent the image's coordinates and size
        self.rect = self.image.get_rect()
        # coordinate using in shift image
        self.rect.x = 0
        self.rect.y = 0
        # image shift pixels
        self.speed = 1224
        # surface to draw image fragment
        self.background_surface = pygame.Surface(resolution)
        # frame counter
        self.operation_counter = 0

    def tick(self):
        # moving the image two times per second
        self.operation_counter += 1
        if self.operation_counter % 30 == 0:
            self.rect.x -= self.speed
            if self.rect.right <= 0:
                self.rect.x = 0

    def draw(self, window):
        # drawing image fragment
        self.background_surface.blit(self.image, self.rect)
        # display image fragment
        window.blit(self.background_surface, (0, 0))
