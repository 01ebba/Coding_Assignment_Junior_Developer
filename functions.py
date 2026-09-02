from entities import Portfolio
from entities import Instrument
from entities import Trade

portfolios = []


# Create portfolios
def create_portfolio():
    name = input("Name: ")
    currency = input("Currency: ")

    portfolio = Portfolio(name, currency)
    portfolios.append(portfolio)

    print("Portfolio created")


# List portfolios
def list_portfolios():
    for portfolio in portfolios:
        print(f"{portfolio.name} - {portfolio.currency}")

# Create and list instruments


# Record a trade (buy or sell) for a given instrument and portfolio
# List all trades, with optional filtering by portfolio or instrument