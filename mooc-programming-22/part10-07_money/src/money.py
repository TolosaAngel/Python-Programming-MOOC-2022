class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, another):
        return self.__euros==another.__euros and self.__cents==another.__cents
    
    def __ne__(self, another):
        return self.__euros!=another.__euros or self.__cents!=another.__cents

    def __gt__(self, another):
        if self.__eq__(another):
            return False
        elif self.__euros>another.__euros:
            return True
        elif self.__euros<another.__euros:
            return False
        elif self.__cents>another.__cents:
            return True
        else:
            return False
        
    def __lt__(self, another):
        if self.__eq__(another):
            return False
        else:
            return not self.__gt__(another)
    
    def __add__(self, another):
        money = Money(self.__euros+another.__euros, self.__cents+another.__cents)

        if money.__cents>=100:
            money.__euros += 1
            money.__cents -= 100

        return money
    
    def __sub__(self, another):
        euros = self.__euros-another.__euros
        cents = self.__cents-another.__cents
        
        if cents<0:
            euros -= 1
            cents += 100

        if euros<0 or cents<0:
            raise ValueError("a negative result is not allowed")
        else:
            return Money(euros, cents)
        
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    print(e1)
    e1.euros = 1000
    print(e1)