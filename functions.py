from entities import Portfolio
from entities import Instrument
from entities import Trade


portfolios = []
instruments = []
trades = []

# testdata
#sweden = Portfolio("Sweden", "SEK")
#volvo = Instrument("Volvo", "Stock")

#portfolios = [sweden]
#instruments = [volvo]
#trades = [Trade(volvo, sweden, 10, 100, "BUY"),
#         Trade(volvo, sweden, 5, 120, "SELL")]


# Create portfolios
def create_portfolio():
    name = input("Name: ").strip()
    currency = input("Currency: ").strip()

    if name == "" or currency == "":
        print("Name and currency can't be empty")
        return

    portfolio = Portfolio(name, currency)
    portfolios.append(portfolio)

    print("Portfolio created")


# List portfolios
def list_portfolios():
    for portfolio in portfolios:
        print(f"{portfolio.name} - {portfolio.currency}")


# Create instrument
def create_instrument():
    name = input("Name: ").strip()
    instrument_type = input("Instrument type: ").strip()

    if name == "" or instrument_type == "":
        print("Name and instrument type can't be empty")
        return

    instrument = Instrument(name, instrument_type)
    instruments.append(instrument)

    print("Instrument created")


# List instruments
def list_instruments():
    for instrument in instruments:
        print(f"{instrument.name} - {instrument.instrument_type}")


# Record a trade (buy or sell) for a given instrument and portfolio
def record_trade():
    search_portfolio = input("Portfolio: ").strip()
    found_portfolio = None

    # Find the selected portfolio
    for p in portfolios:
        if search_portfolio.lower() == p.name.lower():
            found_portfolio = p
            break

    search_instrument = input("Instrument: ").strip()
    found_instrument = None

    # Find the selected instrument
    for i in instruments:
        if search_instrument.lower() == i.name.lower():
            found_instrument = i
            break

    # Stop if portfolio or instrument does not exist
    if found_portfolio is None or found_instrument is None:
        print("Portfolip or instrument not found")
        return

    # Validate input
    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
    except ValueError:
        print("Quantity must be an integer and Price must be a number")
        return

    # Quantity and price must be greater than 0
    if quantity <= 0:
        print("Quantity must be greater than 0")
        return
    if price <= 0:
        print("Price must be greater than 0")
        return
    
    direction = input("Direction: ").strip().upper()

    # Only BUY and SELL are accepted
    if direction not in ["BUY", "SELL"]:
        print("Direction must be BUY or SELL")
        return

    # Create and store trade
    trade = Trade(found_instrument, found_portfolio, quantity, price, direction)
    trades.append(trade)

    print("Trade recorded")


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
    else:
        print("Invalid choice")


# Calculate simplified P&L (profit and loss) as net cash flow from trades
def calculate_pnl():
    portfolio_name = input("Portfolio: ")

    pnl = 0
    found = False

    # Go through all trades in the selected portfolio
    for t in trades:
        if t.portfolio.name.lower() == portfolio_name.lower():
            found = True
            trade_value = t.quantity * t.price

            # BUY = money out and SELL = money in
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

    # Stores net quantity and latest trade price for each instrument
    positions = {}

    found = False

    # Create current position for each instrument
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

    # Calculate total value using the latest recorded trade price
    total_value = 0

    for instrument_name, position in positions.items():
        value = position["quantity"] * position["latest_price"]
        total_value += value

        print(f"{instrument_name}: {position["quantity"]} * {position["latest_price"]} = {value}")

    print(f"Net position value for {portfolio_name}: {total_value}")
