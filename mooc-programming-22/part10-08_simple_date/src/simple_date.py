class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"

    def __eq__(self, another: "SimpleDate"):
        return self.__str__()==another.__str__()
    
    def __ne__(self, another: "SimpleDate"):
        return self.__str__()!=another.__str__()

    def __lt__(self, another: "SimpleDate"):
        if self._year<=another._year:
            if self._year==another._year:
                
                if self._month<=another._month:
                    if self._month==another._month:
                        
                        if self._day<=another._day:
                            if self._day==another._day:
                                return False
                            else:
                                return True
                        else:
                            return False
                    else:
                        return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    def __gt__(self, another: "SimpleDate"):
        return not self.__lt__(another)
    
    def __add__(self, days_to_add: int):
        days = self._day + days_to_add
        month = self._month
        year = self._year

        while days>30:
            month += 1
            days -= 30

            while month>12:
                year += 1
                month -= 12
            
        return SimpleDate(days,month,year)
    
    def __sub__(self, another: "SimpleDate"):
        total_days_1 = self._day + self._month * 30 + self._year * 30 * 12
        total_days_2 = another._day + another._month * 30 + another._year * 30 * 12

        return abs(total_days_1 - total_days_2)

if __name__ == "__main__":  
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)