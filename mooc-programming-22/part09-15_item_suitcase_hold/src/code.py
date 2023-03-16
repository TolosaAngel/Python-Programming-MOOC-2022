class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: "Item"):
        if self.__max_weight>=item.weight():
            self.__max_weight -= item.weight()
            self.__items.append(item)

    def __str__(self):
        if len(self.__items)==1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"
    
    def print_items(self):
        for item in self.__items:
            print(item)
    
    def weight(self):
        weight = 0

        for item in self.__items:
            weight += item.weight()

        return weight
    
    def heaviest_item(self):
        max_item_weight = 0
        heaviest = None

        for item in self.__items:
            print(item.weight())
            if int(item.weight())>=max_item_weight:
                max_item_weight = item.weight()
                heaviest = item

        return heaviest
            
class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: "Suitcase"):
        if self.__max_weight>=suitcase.weight():
            self.__max_weight -= suitcase.weight()
            self.__suitcases.append(suitcase)

    def __str__(self):
        if len(self.__suitcases)==1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
