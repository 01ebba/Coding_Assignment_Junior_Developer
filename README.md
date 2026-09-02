# Coding_Assignment_Junior_Developer

# Features

The application allows users to:
- Create and list portfolios
- Create and list instruments
- Record BUY and SELL trades
- List all recorded trades
- Filter trades by portfolio or instrument
- Calculate simplified P&L for a portfolio 
- Calculate net position value for at portfolio

## Requirements

- Python 3.x

No external libraries are required

## How to run

Clone or download the repository and open a terminal in the project folder.

Run:

```bash
python main.py
```

Depending on the system, you may need to use:

```bash
python3 main.py
```

The application will display a menu where the user can select different operations.


## Project structure

The project is divided in three main files:

### `entities.py`

Contains the data models:

- `Portfolio`
- `Instrument`
- `Trade`

### `functions.py`

Contains the logic and the functions for creating portfolios, instruments, trades and calculations.

### `main.py`

Contains the menu and calls the functions from `functions.py`

## Assumptions

### P&L
Since no external market prices are provided, P&L is implemented using a simplified cash flow model based on recorded trades.

- BUY represents money going out
- SELL represents money coming in

For example:

BUY 10 Volvo @ 100 = -1000
SELL 5 Volvo @ 120 = +600

P&L = -400


### Net Position Value

The net position is calculated by adding quantities from BUY trades and subtracting quantities from SELL trades.

Since no external market prices are available, the latest recorded trade price for each instrument is used as a simplified current price.

For example:

BUY 10 Volvo @ 100
SELL 5 Volvo @ 120

Net quantity = 10 - 5 = 5
Latest price = 120

Net position value = 5 * 120 = 600

If a portfolio contains multiple instruments, the position values of all instruments are added together.

## Input Validation

The application includes basic input validation:

- Portfolio and instrument must exist before a trade can be recorded
- Quantity must be an integer
- Price must be a number
- Quantity and price must be greater than zero
- Direction must be BUY or SELL
- Required fields cannot be empty
- Invalid menu choices display an error message

## Data Storage

Data is currently stored in memory while the application is running.

This means that portfolios, instruments, and trades created by the user are not saved after the application is closed.

## Possible Improvements

Given more time, possible improvements include:

- Unit tests
- Persistent data storage
- More advanced P&L calculations
- External market price data
- Additional input validation