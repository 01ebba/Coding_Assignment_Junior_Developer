from entities import Portfolio
from entities import Instrument
from entities import Trade

# testdata
sweden = Portfolio("Sweden", "SEK")
volvo = Instrument("Volvo", "Stock")

portfolios = [sweden]
instruments = [volvo]
trades = [Trade(volvo, sweden, 10, 100, "BUY"),
          Trade(volvo, sweden, 5, 120, "SELL")]


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


# print trades
def print_trade(t):
    print(f"{t.instrument.name} | {t.portfolio.name} | {t.quantity} | {t.price} | {t.direction} | {t.timestamp} ")


# List all trades, with optional filtering by portfolio or instrument
def list_trades():
    print("""
        1. Show all trades
        2. Filter by portfolio
        3. Filter by instrument
    """)
    choice = input("Choose: ")

    if choice == "1":
        for t in trades:
            print_trade(t)

    elif choice == "2":
        port_choice = input("Portfolio: ")
        for t in trades:
            if t.portfolio.name.lower() == port_choice.lower():
                print_trade(t)

    elif choice == "3":
        inst_choice = input("Instrument: ")
        for t in trades:
            if t.instrument.name.lower() == inst_choice.lower():
                print_trade(t)


# Calculate the profit and loss (P&L) for a given portfolio based on recorded trades
def calculate_pnl():
    portfolio_name = input("Portfolio: ")

    pnl = 0
    found = False

    for t in trades:
        if t.portfolio.name.lower() == portfolio_name.lower():
            found = True
            trade_value = t.quantity * t.price

            if t.direction == "BUY":
                pnl -= trade_value
            elif t.direction == "SELL":
                pnl += trade_value

    if found:
        print(f"P&L for {portfolio_name}: {pnl}")
    else:
        print("No trades found for this portfolio")


# calculate the net position value based on trade history
def calculate_net_position_value():
    portfolio_name = input("Portfolio: ")

    positions = {}
    found = False
    for t in trades:
        if t.portfolio.name.lower() == portfolio_name.lower():
            found = True

            # if instrument not in positions, add to dictionary 
            instrument_name = t.instrument.name
            if instrument_name not in positions:
                positions[instrument_name] = {"quantity": 0, "latest_price": 0}

            if t.direction == "BUY":
                positions[instrument_name]["quantity"] += t.quantity
            elif t.direction == "SELL":
                positions[instrument_name]["quantity"] -= t.quantity

            # Save price from latest trade
            positions[instrument_name]["latest_price"] = t.price

    if not found: 
        print("No trades found for this portfolio")
        return

    total_value = 0

    for instrument_name, position in positions.items():
        value = position["quantity"] * position["latest_price"]
        total_value += value

        print(f"{instrument_name}: {position["quantity"]} * {position["latest_price"]} = {value}")

    print(f"Net position value for {portfolio_name}: {total_value}")
