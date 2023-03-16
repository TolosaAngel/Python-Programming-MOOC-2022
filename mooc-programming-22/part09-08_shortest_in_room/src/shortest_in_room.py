class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return not bool(len((self.persons)))
    
    def print_contents(self):
        combined_height = 0
        names = str()

        for person in self.persons:
            names += f"\n{person} ({person.height} cm)"
            combined_height += person.height
        
        answer = f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm" + names

        print(answer)
    
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest = 0
            self.name_of_shortest = str()

            for person in self.persons:
                if shortest==0 or person.height<shortest:
                    shortest = person.height
                    self.name_of_shortest = person

            return self.name_of_shortest
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            self.persons.remove(self.shortest())
            return self.name_of_shortest

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()