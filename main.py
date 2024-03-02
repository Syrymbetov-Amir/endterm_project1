from datetime import datetime

import pygame

from LiveStockGraph import LiveStockGraph
from StockSimulator import StockSimulator
from User import User
from buttons import Button, StockButton, NotButton
import sys
import time

pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Stock IDLE")
bg = (17, 50, 84)

user = User(1, "Guest", 10000)
stocks = [
    StockSimulator("Apple Inc.", 100, "images/apple_icon.png"),
    StockSimulator("Xiaomi Corp.", 100, "images/mi.png", drift=-0.1, volatility=0.9),
    StockSimulator("Samsung Group", 100, "images/samsung.png", drift=0.0001, volatility=0.15),
    StockSimulator("Volkswagen Group", 100, "images/Volkswagen.png", drift=0.1, volatility=0.4),
    StockSimulator("Toyota Motor Corp.", 100, "images/toyota.png")
]

MAX_FPS = 30
clock = pygame.time.Clock()
clock.tick(MAX_FPS)


def start_menu_scene():
    start_button = Button(250, 300, 300, 50, "Start")
    exit_button = Button(250, 370, 300, 50, "Exit")
    setting_button = Button(570, 530, 200, 50, "Settings")

    running = True

    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.handle_event(event):
                    main_menu_scene()
                elif exit_button.handle_event(event):
                    pygame.quit()
                    sys.exit()
                elif setting_button.handle_event(event):
                    settings_scene()

        start_button.draw(screen)
        exit_button.draw(screen)
        setting_button.draw(screen)

        font = pygame.font.Font("Fonts/troika.otf", 46)
        text_surface = font.render("Stock IDLE", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(w / 2, 100))
        screen.blit(text_surface, text_rect)

        font2 = pygame.font.Font("Fonts/Anta-Regular.ttf", 20)
        text_rect2 = text_surface.get_rect(center=(120, 580))
        text_surface2 = font2.render("v0.0.1 alpha", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)

        pygame.display.flip()


def main_menu_scene():
    stock_button = Button(250, 220, 300, 50, "Stocks")
    credit_button = Button(250, 290, 300, 50, "Credits")
    news_button = Button(250, 360, 300, 50, "News")
    mm_button = Button(250, 430, 300, 50, "Main Menu")
    account_button = Button(570, 530, 200, 50, user.name)

    running = True

    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mm_button.handle_event(event):
                    start_menu_scene()
                elif account_button.handle_event(event):
                    account_scene()
                elif stock_button.handle_event(event):
                    stocks_menu_scene()
                elif credit_button.handle_event(event):
                    credits_menu_scene()

        font = pygame.font.Font("Fonts/troika.otf", 30)
        font2 = pygame.font.Font("Fonts/troika.otf", 50)

        text_surface = font.render("Budget", True, (252, 209, 177))
        text_rect = text_surface.get_rect(center=(w / 2, 50))
        screen.blit(text_surface, text_rect)
        text_surface2 = font2.render(str(round(user.balance, 2)), True, (34, 181, 115))
        text_rect2 = text_surface2.get_rect(center=(w / 2, 100))
        screen.blit(text_surface2, text_rect2)

        stock_button.draw(screen)
        credit_button.draw(screen)
        news_button.draw(screen)
        mm_button.draw(screen)
        account_button.draw(screen)

        pygame.display.flip()


def account_scene():
    back_button = Button(20, 20, 150, 50, "Back")

    user_image = pygame.image.load("images/user_image.png")
    user_image = pygame.transform.scale(user_image, (200, 200))

    running = True

    while running:
        screen.fill((17, 50, 84))
        screen.blit(user_image, (50, 220))
        pygame.draw.rect(screen, (51, 158, 218), [20, 180, w - 60, 9])
        pygame.draw.rect(screen, (51, 158, 218), [20, 134, 170, 55], 0, 12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.handle_event(event):
                    main_menu_scene()

        back_button.draw(screen)

        font = pygame.font.Font("Fonts/Anta-Regular.ttf", 28)
        font2 = pygame.font.Font("Fonts/troika.otf", 36)

        text_surface = font.render("Profile", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(102, 155))
        text_surface2 = font2.render("ID:", True, (252, 209, 177))
        text_rect2 = text_surface2.get_rect(center=(280, 240))
        text_surface3 = font2.render("Name:", True, (252, 209, 177))
        text_rect3 = text_surface3.get_rect(center=(304, 290))
        text_surface4 = font2.render("Online:", True, (252, 209, 177))
        text_rect4 = text_surface4.get_rect(center=(315, 340))

        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)
        screen.blit(text_surface4, text_rect4)

        id_txt = font2.render(f"#{user.user_id}", True, (255, 255, 255))
        name_txt = font2.render(user.name, True, (255, 255, 255))
        online_txt = font2.render(f"{user.get_play_time()} minutes", True, (255, 255, 255))

        id_rect = id_txt.get_rect(center=(415, 240))
        name_rect = name_txt.get_rect(center=(454, 290))
        online_rect = online_txt.get_rect(center=(480, 340))

        screen.blit(id_txt, id_rect)
        screen.blit(name_txt, name_rect)
        screen.blit(online_txt, online_rect)

        pygame.display.flip()


def stocks_menu_scene():
    back_button = Button(20, 20, 150, 50, "Back")
    y_delta = 70

    stock_buttons = []
    for idx, stock in enumerate(stocks):
        btn = StockButton(30, 180 + y_delta * idx, w - 200, 50, stock, user.stocks_count[stock.stock_name])
        stock_buttons.append(btn)

    running = True
    while running:
        screen.fill((17, 50, 84))
        pygame.draw.rect(screen, (12, 35, 59), [w / 2 - 180, 20, 250, 50])
        pygame.draw.rect(screen, (12, 35, 59), [w / 2 + 100, 20, 250, 50])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.handle_event(event):
                    main_menu_scene()
                for btn in stock_buttons:
                    if btn.handle_event(event):
                        stock_scene(btn.stock)

        back_button.draw(screen)
        for btn in stock_buttons:
            btn.cost = btn.stock.get_price()
            btn.amount = user.stocks_count[btn.stock.stock_name]
            btn.draw(screen)

        font = pygame.font.Font("Fonts/troika.otf", 40)
        font2 = pygame.font.Font("Fonts/troika.otf", 24)
        font3 = pygame.font.Font("Fonts/troika.otf", 28)
        stock_txt = font.render("Stocks", True, (255, 255, 255))
        date_txt = font2.render(f"Date: {datetime.now().strftime('%Y-%m-%d')}", True, (255, 255, 255))
        money_txt = font2.render("Money:", True, (255, 255, 255, 255))
        balance_val = font3.render(str(round(user.balance, 2)), True, (34, 181, 115))

        stock_rect = stock_txt.get_rect(center=(w / 2, 120))
        date_rect = date_txt.get_rect(midleft=(w / 2 - 170, 43))
        money_rect = money_txt.get_rect(midleft=(w / 2 + 110, 43))
        money_val_rect = balance_val.get_rect(midright=(w / 2 + 340, 43))

        screen.blit(stock_txt, stock_rect)
        screen.blit(date_txt, date_rect)
        screen.blit(money_txt, money_rect)
        screen.blit(balance_val, money_val_rect)

        pygame.display.flip()


def settings_scene():
    running = True

    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if back_button.handle_event(event):
            #         main_menu(online)

        font = pygame.font.Font("Fonts/troika.otf", 36)
        setting_txt = font.render("Settings", True, (255, 255, 255))
        setting_rect = setting_txt.get_rect(center=(w / 2, 50))
        screen.blit(setting_txt, setting_rect)

        pygame.display.flip()


def credits_menu_scene():
    _small_credit = NotButton(50, 200, 300, 50, f"Small Credit: {user.credits['small']}")
    take_small = Button(430, 200, 130, 50, "Take", rect=(80, 188))
    repay_small = Button(580, 200, 130, 50, "Repay", rect=(80, 188))

    _medium_credit = NotButton(50, 300, 300, 50, f"Medium Credit: {user.credits['medium']}")
    take_medium = Button(430, 300, 130, 50, "Take", rect=(80, 188))
    repay_medium = Button(580, 300, 130, 50, "Repay", rect=(80, 188))

    _big_credit = NotButton(50, 400, 300, 50, f"Big Credit: {user.credits['big']}")
    take_big = Button(430, 400, 130, 50, "Take", rect=(80, 188))
    repay_big = Button(580, 400, 130, 50, "Repay", rect=(80, 188))

    back_button = Button(20, 20, 150, 50, "Back")

    objects_to_draw = [
        _small_credit, take_small, repay_small,
        _medium_credit, take_medium, repay_medium,
        _big_credit, take_big, repay_big,
        back_button
    ]

    font = pygame.font.Font("Fonts/troika.otf", 40)
    warn_text = None  # font.render("Enough money!", True, (252, 3, 3))
    warn_text_rect = None  # enough_money_warn.get_rect(center=(w / 2, 50))
    warn_time = None

    running = True
    while running:
        screen.fill((17, 50, 84))
        for obj in objects_to_draw:
            obj.draw(screen)

        if warn_text and time.time() - warn_time < 2:
            screen.blit(warn_text, warn_text_rect)
        else:
            warn_text = None
            warn_text_rect = None
            warn_time = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                res = None
                if take_small.handle_event(event):
                    res = user.take_credit('small')
                    _small_credit.text = f"Small Credit: {user.credits['small']}"
                elif repay_small.handle_event(event):
                    res = user.repay_credit('small')
                    _small_credit.text = f"Small Credit: {user.credits['small']}"
                elif take_medium.handle_event(event):
                    res = user.take_credit('medium')
                    _medium_credit.text = f"Medium Credit: {user.credits['medium']}"
                elif repay_medium.handle_event(event):
                    res = user.repay_credit('medium')
                    _medium_credit.text = f"Medium Credit: {user.credits['medium']}"
                elif take_big.handle_event(event):
                    res = user.take_credit('big')
                    _big_credit.text = f"Big Credit: {user.credits['big']}"
                elif repay_big.handle_event(event):
                    res = user.repay_credit('big')
                    _big_credit.text = f"Big Credit: {user.credits['big']}"

                if res:
                    warn_text = font.render(res, True, (252, 3, 3))
                    warn_text_rect = warn_text.get_rect(center=(w / 2, 50))
                    warn_time = time.time()
                elif back_button.handle_event(event):
                    main_menu_scene()

        pygame.display.flip()


def stock_scene(stock: StockSimulator):
    img = pygame.image.load(stock.image_url)
    img = pygame.transform.scale(img, (60, 60))
    img_rect = img.get_rect(midleft=(40, 150))

    font2 = pygame.font.Font("Fonts/Anta-Regular.ttf", 24)
    count_surface = font2.render(f"Count: {user.stocks_count[stock.stock_name]}", True, (255, 255, 255))
    count_rect = count_surface.get_rect(center=(170, 150))

    live_price_surface = font2.render(f"Live price: {stock.get_price()}$", True, (255, 255, 255))
    live_price_rect = count_surface.get_rect(center=(350, 150))

    balance_surface = font2.render(f"Balance: {round(user.balance, 2)}$", True, (255, 255, 255))
    balance_rect = count_surface.get_rect(center=(600, 150))

    buy_button = Button(w / 2 - 200, 500, 150, 50, "Buy")
    sell_button = Button(w / 2 + 90, 500, 150, 50, "Sell")

    live_stock_graph = LiveStockGraph(stock, screen, pygame.Rect(204, 219, 637 - 204, 460 - 219))

    running = True

    last_time = time.time()

    while running:
        screen.fill((17, 50, 84))

        screen.blit(img, img_rect)
        screen.blit(count_surface, count_rect)
        screen.blit(balance_surface, balance_rect)
        screen.blit(live_price_surface, live_price_rect)
        buy_button.draw(screen)
        sell_button.draw(screen)

        if (time.time() - last_time) >= 1:
            last_time = time.time()
            stock.generate_next_price()
            live_stock_graph.update()

        live_stock_graph.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button.handle_event(event):
                    if user.balance >= stock.get_price():
                        user.balance -= stock.get_price()
                        user.stocks_count[stock.stock_name] += 1
                elif sell_button.handle_event(event):
                    if user.stocks_count[stock.stock_name] > 0:
                        user.balance += stock.get_price()
                        user.stocks_count[stock.stock_name] -= 1

        font = pygame.font.Font("Fonts/troika.otf", 40)
        title = font.render(stock.stock_name, True, (255, 255, 255))
        title_rect = title.get_rect(center=(w / 2, 50))
        screen.blit(title, title_rect)

        count_surface = font2.render(f"Count: {user.stocks_count[stock.stock_name]}", True, (255, 255, 255))
        balance_surface = font2.render(f"Balance: {round(user.balance, 2)}$", True, (255, 255, 255))
        live_price_surface = font2.render(f"Live price: {stock.get_price()}$", True, (255, 255, 255))

        pygame.display.flip()


if __name__ == "__main__":
    start_menu_scene()
