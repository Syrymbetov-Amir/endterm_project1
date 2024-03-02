import pygame

from StockSimulator import StockSimulator


class Button:
    def __init__(self, x, y, width, height, text, rect: tuple[int, int] = (113, 188)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, (0, *self.rect), [self.x, self.y, self.width, self.height])
        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 26)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                return True
        return False


class NotButton:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        # pygame.draw.rect(screen, (0, 80, 188), [self.x, self.y, self.width, self.height])
        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 26)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        pass


class StockButton:
    def __init__(self, x, y, width, height, stock: StockSimulator, amount: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stock = stock
        self.text = stock.stock_name
        self.image_url = stock.image_url
        self.cost = stock.get_price()
        self.amount = amount

    def draw(self, screen):
        pygame.draw.rect(screen, (12, 35, 59), [self.x, self.y, self.width, self.height], 0, 15)
        img = pygame.image.load(self.image_url)
        img = pygame.transform.scale(img, (30, 30))
        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 26)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(self.x + 80, self.y + self.height / 2))
        cost_surf = font.render(f"{self.cost}$", True, (57, 164, 253))
        amount_surf = font.render(str(self.amount), True, (237, 237, 52))
        amount_rect = amount_surf.get_rect(midleft=(self.width / 2 + 220, self.y + self.height / 2))
        cost_rect = cost_surf.get_rect(midleft=(self.width / 2 + 80, self.y + self.height / 2))
        img_rect = img.get_rect(midleft=(self.x + 30, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)
        screen.blit(img, img_rect)
        screen.blit(cost_surf, cost_rect)
        screen.blit(amount_surf, amount_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                return True
        return False
