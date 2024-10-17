import pygame

# class counts how many target Player shoot


class Counting:
    def __init__(self):
        # location coordinate
        self.x_cord = 50
        self.y_cord = 40
        self.width = 80
        self.height = 20
        # initial number of hits
        self.count = 0
        # font
        self.font_count = pygame.font.SysFont('arial', 20)
        # counter
        self.count_txt = self.font_count.render(f'Amount: {self.count}', True, (255, 255, 255))

    def tick(self,hit):
         if hit==True:
        # increasing counter
            self.count += 1

    def draw(self, window):
        # drawing counter
        self.count_txt = self.font_count.render(f'Amount: {self.count}', True, (255, 255, 255))
        window.blit(self.count_txt, (50, 50))
