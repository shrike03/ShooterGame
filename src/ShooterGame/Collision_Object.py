from ShooterGame import pygame,Path
# static object with hitbox
class Object:
    def __init__(self, x_cord, y_cord, width, height, img_name): 
        # location coordinate
        self.x_cord = x_cord
        self.y_cord = y_cord
        # object dimensions
        self.width = width
        self.height = height
        # hitbox object
        self.hitbox_ob = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        # creating path to folder Images
        images_path = Path(__file__).parent / "Assets" / "Images"
        # the name of the loaded image and folder f.e. static/platform
        self.img_name = img_name
        # image loading
        self.image_temp = pygame.image.load(str(images_path/f"{self.img_name}.png"))
        # change image_temp size
        self.change_size = (width, height)
        self.image = pygame.transform.scale(self.image_temp, self.change_size)

    def tick(self):
        pass

    def draw(self, window):
        # drawing an object
        window.blit(self.image, (self.x_cord, self.y_cord))
