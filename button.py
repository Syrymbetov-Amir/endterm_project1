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

class StockButton:
    def __init__(self,x,y,width,height,text, image_url, cost, exist):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image_url = image_url
        self.cost = cost
        self.exist = exist

    def draw2(self, screen):
        pygame.draw.rect(screen, (12, 35, 59), [self.x, self.y, self.width, self.height], 0, 15)
        img = pygame.image.load(self.image_url)
        img = pygame.transform.scale(img, (30,30))
        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 26)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(self.x+80, self.y + self.height / 2))
        cost_surf = font.render(f"{self.cost}$", True, (57,164,253))
        cost_rect = cost_surf.get_rect(midleft=(self.width/2+80,self.y + self.height/2))
        exist_surf = font.render(self.exist, True, (245,149,37))
        exist_rect = exist_surf.get_rect(midright=(self.width-30, self.y + self.height/2))
        img_rect = img.get_rect(midleft=(self.x+30, self.y + self.height/2))
        screen.blit(text_surface, text_rect)
        screen.blit(img, img_rect)
        screen.blit(cost_surf, cost_rect)
        screen.blit(exist_surf, exist_rect)

    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                return True
        return False