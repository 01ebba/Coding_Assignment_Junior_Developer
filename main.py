from functions import create_portfolio, list_portfolios, create_instrument, list_instruments

running = True

while running:
    print("""
        1. Create portfolio
        2. List portfolios
        3. Create instrument
        4. List instruments
        x. Quit
    """)


    choice = input("Choose: ")

    if choice == "1":
        create_portfolio()
    elif choice == "2":
        list_portfolios()
    elif choice == "3":
        create_instrument()
    elif choice == "4":
        list_instruments()
    elif choice == "x":
        running = False
