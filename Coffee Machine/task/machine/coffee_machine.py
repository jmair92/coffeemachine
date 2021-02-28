class CoffeeMachine:
    water = 0
    milk = 0
    coffee = 0
    cups = 0
    money = 0
    action = None
    working = False

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.action = "getting action"
        self.working = True

    def get_action(self):
        if self.action == "getting action":
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")
        elif self.action == "buy":
            return input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        elif self.action == "getting water":
            return int(input("Write how many ml of water do you want to add:\n"))
        elif self.action == "getting milk":
            return int(input("Write how many ml of milk do you want to add:\n"))
        elif self.action == "getting beans":
            return int(input("Write how many grams of coffee beans do you want to add:\n"))
        elif self.action == "getting cups":
            return int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def number_of_supplies(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.coffee, " of coffee beans")
        print(self.cups, " of disposable cups")
        print(self.money, " of money")

    def buy(self, x):
        if x == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
        elif x == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
        elif x == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
        else:
            print()

    def fill(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def process(self):
        while self.working:
            self.get_action()
            if self.action == "buy":
                choice = self.get_action()
                self.buy(choice)
                self.action = "getting action"
            elif self.action == "fill":
                self.action = "getting water"
                water_income = self.get_action()
                self.action = "getting milk"
                milk_income = self.get_action()
                self.action = "getting beans"
                beans_income = self.get_action()
                self.action = "getting cups"
                cups_income = self.get_action()
                self.fill(water_income, milk_income, beans_income, cups_income)
                self.action = "getting action"
            elif self.action == "take":
                self.take()
                self.action = "getting action"
            elif self.action == "remaining":
                self.number_of_supplies()
                self.action = "getting action"
            elif self.action == "exit":
                self.action = "getting action"
                self.working = False


coffee_machine = CoffeeMachine()
coffee_machine.process()
