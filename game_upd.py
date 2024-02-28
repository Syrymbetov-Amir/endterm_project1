import pygame
from button import Button, StockButton
import sys
import time

pygame.init()




start_time = time.time()
last_update = start_time
online = 0
balance = 0
credits = [0, 0, 0]
avai = 0

w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Stock IDLE")
bg = (17, 50, 84)

MAX_FPS = 60
clock = pygame.time.Clock()

id = 1
username = f"Guest{id}"

if time.time() - last_update >= 60:
    online += 1
    last_update = time.time()

def start_menu(online, balance, credits):
    global last_update

    start_button = Button(250, 300, 300, 50, "Start", None)
    exit_button = Button(250, 370, 300, 50, "Exit", None)
    setting_button = Button(570, 530, 200, 50, "Settings", None)

    running = True
    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.handle_event(event):
                    main_menu(online, balance, credits)
                elif exit_button.handle_event(event):
                    running = False
                    pygame.quit()
                    sys.exit()
                elif setting_button.handle_event(event):
                    settings(online)

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

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


def main_menu(online, balance, credits):
    global last_update
    stock_button = Button(250, 220, 300, 50, "Stocks", None)
    credit_button = Button(250, 290, 300, 50, "Credits", None)
    news_button = Button(250, 360, 300, 50, "News", None)
    mm_button = Button(250, 430, 300, 50, "Main Menu", None)
    account_button = Button(570, 530, 200, 50, username, None)
    running = True
    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mm_button.handle_event(event):
                    start_menu(online, balance, credits)
                elif account_button.handle_event(event):
                    account(online)
                elif stock_button.handle_event(event):
                    stocks_menu(online, balance, avai)
                elif credit_button.handle_event(event):
                    credits_menu(online, balance, credits)

        font = pygame.font.Font("Fonts/troika.otf", 30)
        font2 = pygame.font.Font("Fonts/troika.otf", 50)
        text_surface = font.render("Budget", True, (252, 209, 177))
        text_rect = text_surface.get_rect(center=(w / 2, 50))
        screen.blit(text_surface, text_rect)
        text_surface2 = font2.render(str(balance), True, (34, 181, 115))
        text_rect2 = text_surface2.get_rect(center=(w / 2, 100))
        screen.blit(text_surface2, text_rect2)
        stock_button.draw(screen)
        credit_button.draw(screen)
        news_button.draw(screen)
        mm_button.draw(screen)
        account_button.draw(screen)

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


def account(online):
    global last_update
    back_button = Button(20, 20, 150, 50, "Back", None)

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
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.handle_event(event):
                    main_menu(online, balance, credits)

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

        id_txt = font2.render(f"#{id}", True, (255, 255, 255))
        name_txt = font2.render(username, True, (255, 255, 255))
        online_txt = font2.render(f"{online} minutes", True, (255, 255, 255))

        id_rect = id_txt.get_rect(center=(415, 240))
        name_rect = name_txt.get_rect(center=(454, 290))
        online_rect = online_txt.get_rect(center=(480, 340))

        screen.blit(id_txt, id_rect)
        screen.blit(name_txt, name_rect)
        screen.blit(online_txt, online_rect)

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


def stocks_menu(online, balance, avai):
    global last_update

    cost = 100


    back_button = Button(20, 20, 150, 50, "Back")

    apple = StockButton(30, 200, w-200, 50, "Apple Inc.", "images/apple_icon.png", str(cost), str(avai))
    xiaomi = StockButton(30, 270, w-200, 50, "Xiaomi Corp.", "images/mi.png", str(cost), str(avai))
    samsung = StockButton(30, 340, w-200, 50, "Samsung Group", "images/samsung.png", str(cost), str(avai))
    volkswagen = StockButton(30, 410, w-200, 50, "Volkswagen Group", "images/Volkswagen.png", str(cost), str(avai))
    toyota = StockButton(30, 480, w-200, 50, "Toyota Motor Corp.", "images/toyota.png", str(cost), str(avai))


    running = True
    while running:
        screen.fill((17, 50, 84))
        pygame.draw.rect(screen, (12, 35, 59), [w/2-180, 20, 250, 50])
        pygame.draw.rect(screen, (12, 35, 59), [w/2+100, 20, 250, 50])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.handle_event(event):
                    main_menu(online, balance, credits)
                elif apple.handle_event(event):
                    apple_stock(online, balance)

        back_button.draw(screen)
        apple.draw2(screen)
        xiaomi.draw2(screen)
        samsung.draw2(screen)
        volkswagen.draw2(screen)
        toyota.draw2(screen)

        font = pygame.font.Font("Fonts/troika.otf", 40)
        font2 = pygame.font.Font("Fonts/troika.otf", 24)
        font3 = pygame.font.Font("Fonts/troika.otf", 28)
        stock_txt = font.render("Stocks", True, (255, 255, 255))
        date_txt = font2.render("Date:", True, (255, 255, 255))
        money_txt = font2.render("Money:", True, (255,255,255,255))
        # date_val = font2.render(time.time(), True, (255,255,255,255))
        money_val = font3.render(str(balance), True, (34, 181, 115))

        stock_rect = stock_txt.get_rect(center=(w / 2, 120))
        date_rect = date_txt.get_rect(midleft=(w/2-170, 43))
        money_rect = money_txt.get_rect(midleft = (w/2+110,43))
        # date_val_rect = date_val.get_rect(midright=(w / 2 - 170, 43))
        money_val_rect = money_val.get_rect(midright=(w / 2 + 340, 43))


        screen.blit(stock_txt, stock_rect)
        screen.blit(date_txt, date_rect)
        screen.blit(money_txt, money_rect)
        screen.blit(money_val, money_val_rect)

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


def settings(online):
    global w, h
    global last_update

    running = True
    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


def credits_menu(online, balance, credits):
    global last_update

    small_credit = Button(100, 200, 300, 50, "Small Credit", None)
    repay_small = Button(400, 200, 300, 50, "Repay", None)
    medium_credit = Button(100, 300, 300, 50, "Medium Credit", None)
    repay_medium = Button(400, 300, 300, 50, "Repay", None)
    big_credit = Button(100, 400, 300, 50, "Big Credit", None)
    repay_big = Button(400, 400, 300, 50, "Repay", None)
    back_button = Button(20, 20, 150, 50, "Back", None)

    sum_credits = credits[0] * 10000 + credits[1] * 50000 + credits[2] * 100000

    font = pygame.font.Font("Fonts/troika.otf", 50)
    enough_money_warn = font.render("Enough money!", True, (252, 3, 3))
    enough_money_warn_rect = enough_money_warn.get_rect(center=(w / 2, 50))
    limit_warn = font.render("You have reached\nthe limit", True, (252, 3, 3))
    limit_warn_rect = limit_warn.get_rect(center=(w / 2, 100))

    enough_money_warn_time = 0
    limit_warn_time = 0

    running = True
    while running:
        screen.fill((17, 50, 84))
        small_credit.draw(screen)
        repay_small.draw(screen)
        medium_credit.draw(screen)
        repay_medium.draw(screen)
        big_credit.draw(screen)
        repay_big.draw(screen)
        back_button.draw(screen)

        if time.time() - enough_money_warn_time < 2:
            screen.blit(enough_money_warn, enough_money_warn_rect)

        if time.time() - limit_warn_time < 2:
            screen.blit(limit_warn, limit_warn_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if small_credit.handle_event(event):
                    if sum_credits < 200000:
                        balance += 10000
                        credits[0] += 1
                        main_menu(online, balance, credits)
                    else:
                        limit_warn_time = time.time()
                elif repay_small.handle_event(event):
                    if balance >= 10000:
                        balance -= 10000
                        sum_credits -= 10000
                        credits[0] -= 1
                    else:
                        enough_money_warn_time = time.time()

                elif medium_credit.handle_event(event):
                    if sum_credits < 200000:
                        balance += 50000
                        credits[1] += 1
                        main_menu(online, balance, credits)
                    else:
                        limit_warn_time = time.time()
                elif repay_medium.handle_event(event):
                    if balance >= 50000:
                        balance -= 50000
                        sum_credits -= 50000
                        credits[1] -= 1
                    else:
                        enough_money_warn_time = time.time()
                elif big_credit.handle_event(event):
                    if sum_credits < 200000:
                        balance += 100000
                        credits[2] += 1
                        main_menu(online, balance, credits)
                    else:
                        limit_warn_time = time.time()

                elif repay_big.handle_event(event):
                    if balance >= 100000:
                        balance -= 100000
                        sum_credits -= 100000
                        credits[2] -= 1
                    else:
                        enough_money_warn_time = time.time()
                elif back_button.handle_event(event):
                    main_menu(online, balance, credits)

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()

def apple_stock(online, balance):
    global last_update

    running = True
    while running:
        screen.fill((17, 50, 84))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if back_button.handle_event(event):
            #         main_menu(online)

        if time.time() - last_update >= 60:
            online += 1
            last_update = time.time()

        pygame.display.flip()


if __name__ == "__main__":
    stocks_menu(online, balance, avai)
