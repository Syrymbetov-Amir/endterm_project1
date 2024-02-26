import pygame

class Button:
    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 113, 188), [self.x, self.y, self.width, self.height])
        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 26)
        text_surface = font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.x + self.width/2, self.y+self.height/2))
        screen.blit(text_surface, text_rect)

    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                return True
        return False