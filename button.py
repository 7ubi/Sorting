import pygame

pygame.init()

myfont = pygame.font.SysFont('Arial', 22)

class Button:
    def __init__(self, x, y, text, screen):
        self.x = x
        self.y = y
        self.w = 100
        self.h = 50
        self.text = text
        self.screen = screen
    
    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (self.x, self.y, self.w, self.h))
        textsurface = myfont.render(self.text, False, (255, 255, 255))
        self.screen.blit(textsurface, (self.x + 5, self.y + 12))
    