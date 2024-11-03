import pygame
import sys

class Control():
    def __init__(self):
        self.input_text = {'Moving Right':'',
                           'Moving Left' :'',
                           'Jumping' :'',
                           'Shooting' :'',
                           'Pause' :'',
                           'Restart' :''}
        # specjalne przyciski:
        self.specials_buttons = {pygame.K_SPACE: 'SPACE',
                                 pygame.K_LALT: 'L ALT',
                                 pygame.K_RALT: 'R ALT',
                                 pygame.K_LCTRL: 'L CTRL',
                                 pygame.K_RCTRL: 'R CTRL',
                                 pygame.K_LSHIFT: 'L SHIFT',
                                 pygame.K_RSHIFT: 'R SHIFT',
                                 pygame.K_CAPSLOCK: 'CAPSLOCK',
                                 pygame.K_TAB: 'TAB'}
        # aktywny przycisk
        self.active_button = None
        # Coordinate for buttons
        self.x_cord = 200
        self.y_cord = 135
        # odstęp między wierszami
        self.y_offset = 0
        # font colour nomrmal
        self.colour = (113, 4, 4)
        self.colour_active = (163, 54, 54)
        # font for categories text
        self.pl_font = pygame.font.SysFont('Sitka Small Bold', 75)
        # font for controls description
        self.ct_font = pygame.font.SysFont('Sitka Small Bold', 55)
        # Main categories of controls
        self.pl_one = self.pl_font.render('PLAYER ONE', True, self.colour)
        self.pl_two = self.pl_font.render('PLAYER TWO', True, self.colour)
        self.g_c = self.pl_font.render('GAME CONTROL', True, self.colour)
        
        # Dictionary for buttons
        self.controls = {
                'Moving Right' : (self.ct_font.render('Moving Right', True, self.colour),self.x_cord, 165),
                'Moving Left' : (self.ct_font.render('Moving Left', True, self.colour),self.x_cord, 215),
                'Jumping' : (self.ct_font.render('Jumping', True, self.colour),self.x_cord, 265),
                'Shooting' : (self.ct_font.render('Shooting', True, self.colour),self.x_cord, 315),
                'Pause' : (self.ct_font.render('Pause', True, self.colour),self.x_cord, 465),
                'Restart' : (self.ct_font.render('Restart', True, self.colour),self.x_cord, 515)
                }
    
    def tick(self, events):
        for event in events:
            if pygame.MOUSEBUTTONDOWN:
                for button_name, (text_render, x_pos, y_pos) in self.controls.items():
                    self.width = text_render.get_width()
                    self.height = text_render.get_height()
                    self.hitbox = pygame.Rect(x_pos, y_pos, self.width, self.height)
                    if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                        if pygame.mouse.get_pressed()[0]:
                            self.active_button = button_name
                            break

                    elif event.type == pygame.KEYDOWN:
                        if self.active_button is not None:
                            if event.key == pygame.K_BACKSPACE:
                                self.input_text[self.active_button] = ''
                            else: 
                                if event.key in self.specials_buttons:
                                    self.input_text[self.active_button] = self.specials_buttons[event.key]
                                elif len(self.input_text[self.active_button]) == 0:
                                    input_char = event.unicode.upper()
                                    if input_char not in self.input_text.values():
                                        self.input_text[self.active_button] += input_char
                                    else:
                                        print('Przypisany już klawisz')
                            
    def draw(self, window):
                # Button categories
        window.blit(self.pl_one, (200, 100))
        window.blit(self.g_c, (200, 400))
        # button blittin
        for button_name, (text_render, x_pos,y_pos) in self.controls.items():
            if self.active_button == button_name:
                input_text_surface = self.ct_font.render(self.input_text[button_name], True, self.colour_active)
                text_render= self.ct_font.render(button_name, True, self.colour_active)
            else:
                input_text_surface = self.ct_font.render(self.input_text[button_name], True, self.colour)
                text_render= self.ct_font.render(button_name, True, self.colour)
            
            window.blit(input_text_surface, ((x_pos + 300), (y_pos)))
            window.blit(text_render, (x_pos, y_pos))
       