from entities import Portfolio
from entities import Instrument
from entities import Trade

portfolios = []
instruments = []


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


# Create instrument
def create_instrument():
    name = input("Name: ")
    instrument_type = input("Instrument type: ")

    instrument = Instrument(name, instrument_type)
    instruments.append(instrument)

    print("Instrument created")


# List instruments
def list_instruments():
    for instrument in instruments:
        print(f"{instrument.name} - {instrument.instrument_type}")

# Record a trade (buy or sell) for a given instrument and portfolio
# List all trades, with optional filtering by portfolio or instrument