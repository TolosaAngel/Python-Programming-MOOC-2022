class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        format_balance = round(float(f"{self.balance:02}"), 1)
        return f"The balance is {format_balance} euros"

    def eat_lunch(self):
        if self.balance>=2.60: 
            self.balance -= 2.60

    def eat_special(self):
        if self.balance>=4.60:    
            self.balance -= 4.60

    def deposit_money(self, money: int):
        if money>=0:
            self.balance += money
        else:
            raise ValueError("You cannot deposit an amount of money less than zero")

peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.deposit_money(20)
graces_card.eat_special()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")
    