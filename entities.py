import datetime

class Portfolio:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency

class Instrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

class Trade:
    def __init__(self, instrument, portfolio, quantity, price, direction):
        self.instrument = instrument
        self.portfolio = portfolio
        self.quantity = quantity
        self.price = price
        self.timestamp = datetime.datetime.now()
        self.direction = direction

