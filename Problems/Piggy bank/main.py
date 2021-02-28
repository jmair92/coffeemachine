class PiggyBank:
    # create __init__ and add_money methods

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents


    def add_money(self, deposit_dollars, deposit_cents):
        var = self.cents + deposit_cents
        if var > 99:
            self.dollars = self.dollars + deposit_dollars + var // 100
            self.cents = var % 100
        else:
            self.cents += deposit_cents
            self.dollars += deposit_dollars
