from entities import Portfolio
from entities import Instrument
from entities import Trade

portfolios = []
instruments = []
trades = []


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
def record_trade():
    search_portfolio = input("Portfolio: ")
    found_portfolio = None

    for p in portfolios:
        if search_portfolio == p.name:
            found_portfolio = p

    search_instrument = input("Instrument: ")
    found_instrument = None

    for i in instruments:
        if search_instrument == i.name:
            found_instrument = i

    if found_portfolio is not None and found_instrument is not None:
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        direction = input("Direction: ").upper()

        trade = Trade(found_instrument, found_portfolio, quantity, price, direction)
        trades.append(trade)
        print("Trade recorded")
    else: 
        print("Portfolio or Instrument not found")

# List all trades, with optional filtering by portfolio or instrument