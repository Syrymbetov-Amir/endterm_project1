import pygame

# import random
# import time

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Stock Market Game')

background_color = (255,255,255)
screen.fill(background_color)

# Load font
font = pygame.font.Font(None, 16)

title_text = font.render('Welcome to My Game', True, (0, 0, 0))
title_rect = title_text.get_rect(center=screen.get_rect().center)

# Load images
butcher_icon = pygame.image.load('butcher_icon.png')
butcher_icon = pygame.transform.scale(butcher_icon, (100,100))
textile_factory_icon = pygame.image.load('textile_factory_icon.png')
textile_factory_icon = pygame.transform.scale(textile_factory_icon, (100,100))
pulp_mill_icon = pygame.image.load('pulp_mill_icon.png')
pulp_mill_icon = pygame.transform.scale(pulp_mill_icon, (120,120))
furniture_factory_icon = pygame.image.load('furniture_factory_icon.png')
furniture_factory_icon = pygame.transform.scale(furniture_factory_icon, (100,100))
oil_refinery_icon = pygame.image.load('oil_refinery_icon.png')
automobile_plant_icon = pygame.image.load('automobile_plant_icon.png')
electronic_company_icon = pygame.image.load('electronic_company_icon.png')
chemical_plant_icon = pygame.image.load('chemical_plant_icon.png')
space_corporation_icon = pygame.image.load('space_corporation_icon.png')
loan_icon = pygame.image.load('loan_icon.png')
pay_loan_icon = pygame.image.load('pay_loan_icon.png')
portfolio_icon = pygame.image.load('portfolio_icon.png')
profile_icon = pygame.image.load('profile_icon.png')

# Define stocks
stocks = {
    'Butcher\'s Shop': {'icon': butcher_icon, 'price': 1000},
    'Textile Factory': {'icon': textile_factory_icon, 'price': 5000},
    'Pulp Mill': {'icon': pulp_mill_icon, 'price': 10000},
    'Furniture Factory': {'icon': furniture_factory_icon, 'price': 200}}

# Define loans
loans = [1000, 5000, 10000]

# Define player's portfolio and balance
portfolio = {}
balance = 10000

# Define achievements
achievements = []

# Define current loans
current_loans = []

# Define virtual time
virtual_time = 0
virtual_time_increment = 10  # 1 virtual hour = 10 virtual seconds

# Define seasons
seasons = ['winter', 'spring', 'summer', 'autumn']
current_season = 0


def update_stock_prices():
    # Update stock prices based on current season
    if current_season == 1:  # Spring
        for stock in stocks.values():
            stock['price'] *= 1.02  # Increase price by 2%
    elif current_season == 2:  # Summer
        for stock in stocks.values():
            stock['price'] *= 1.05  # Increase price by 5%
    # Add more conditions for other seasons


def draw_stock_market_screen():
    # Draw stock icons
    for i, (name, stock) in enumerate(stocks.items()):
        screen.blit(stock['icon'], (100 + i * 100, 100))
        pygame.draw.rect(screen, (255, 255, 255), (100 + i * 100, 100, 100, 100), 2)
        draw_stock_price(name, stock['price'], 100 + i * 100, 200)


def draw_stock_price(name, price, x, y):
    # Draw stock price
    price_text = font.render(f"{name}: ${price}", True, (255, 255, 255))
    screen.blit(price_text, (x, y))


def draw_loan_options():
    # Draw loan options
    for i, loan in enumerate(loans):
        loan_text = font.render(f"Loan: ${loan}", True, (255, 255, 255))
        screen.blit(loan_text, (100 + i * 100, 400))
        pygame.draw.rect(screen, (255, 255, 255), (100 + i * 100, 400, 100, 100), 2)


def draw_portfolio():
    # Draw portfolio
    for i, (name, amount) in enumerate(portfolio.items()):
        portfolio_text = font.render(f"{name}: {amount}", True, (255, 255, 255))
        screen.blit(portfolio_text, (100 + i * 100, 500))


def draw_balance():
    # Draw balance
    balance_text = font.render(f"Balance: ${balance}", True, (255, 255, 255))
    screen.blit(balance_text, (100, 600))


def draw_achievements():
    # Draw achievements
    for i, achievement in enumerate(achievements):
        achievement_text = font.render(f"{achievement}", True, (255, 255, 255))
        screen.blit(achievement_text, (100 + i * 100, 200))


def draw_loan_status():
    # Draw loan status
    for i, loan in enumerate(current_loans):
        loan_text = font.render(f"Loan: ${loan}", True, (255, 255, 255))
        screen.blit(loan_text, (100 + i * 100, 300))


def update_virtual_time():
    global virtual_time
    virtual_time += virtual_time_increment


def check_achievements():
    global achievements
    # Check for achievements
    if len(portfolio) >= 5:
        achievements.append("Portfolio Master")
    if balance >= 100000:
        achievements.append("Millionaire")
    # Add more conditions for other achievements


# global virtual_time
# global current_season
# global balance

running = True
while running:

    pygame.display.update()
    # Draw stock market screen
    draw_stock_market_screen()
    draw_loan_options()
    draw_portfolio()
    draw_balance()
    draw_achievements()
    draw_loan_status()
    # Update virtual time
    update_virtual_time()

    # Update stock prices based on current season
    update_stock_prices()

    # Check for achievements
    check_achievements()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.get_pos()

            # Check for clicks on stocks
            for i, (name, stock) in enumerate(stocks.items()):
                if 100 + i * 100 <= x <= 200 + i * 100 and 100 <= y <= 200:
                    if balance >= stock['price']:
                        portfolio[name] = portfolio.get(name, 0) + 1
                        balance -= stock['price']
                        # Check for clicks on loans
                    if 100 <= x <= 200 and 400 <= y <= 500:
                        loan_amount = loans[0]
                    if 200 <= x <= 300 and 400 <= y <= 500:
                        loan_amount = loans[1]
                    if 300 <= x <= 400 and 400 <= y <= 500:
                        loan_amount = loans[2]
                    if balance < loan_amount:
                        continue
                    balance -= loan_amount
                    current_loans.append(loan_amount)

                # Check for clicks on pay loans
                # Check for clicks on pay loans
                if 100 <= x <= 200 and 600 <= y <= 700:
                    if current_loans:  # Make sure there are loans to pay
                        balance += current_loans[0]
                        current_loans.pop(0)

