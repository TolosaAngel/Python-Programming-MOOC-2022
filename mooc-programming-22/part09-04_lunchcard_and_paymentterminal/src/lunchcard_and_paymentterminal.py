class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance>=amount:
            self.balance -= amount
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
        self.regular_price = 2.50
        self.special_price = 4.30

    def eat_lunch(self, payment: float):
        if payment>=self.regular_price:
            self.funds += self.regular_price
            self.lunches += 1
            return payment-self.regular_price
        else:
            return payment

    def eat_special(self, payment: float):        
        if payment>=self.special_price:
            self.funds += self.special_price
            self.specials += 1
            return payment-self.special_price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance>=self.regular_price:
            card.subtract_from_balance(self.regular_price)
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance>=self.special_price:
            card.subtract_from_balance(self.special_price)
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount
        
if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)