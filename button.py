import pygame

pygame.font.init()


FONT1 = pygame.font.SysFont("comicsans", 48)

RED = (255, 0, 0)

class Button:
    def __init__(self, x, y, text):
        self.text = FONT1.render(text, 1, RED)
        self.rect = pygame.Rect(x, y, self.text.get_width(), self.text.get_height())

    def draw(self, win, middle = True, width = 750, height = 750):
        if middle:
            win.blit(self.text, (width //2 - self.text.get_width() /2, height //2 - self.text.get_height()/2))
            return
        win.blit(self.text, (self.rect.x, self.rect.y))

    def click(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            return True
        return  False