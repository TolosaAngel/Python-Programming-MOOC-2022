class ListHelper:
    def __dictionary_creation(my_list: list):
        my_dictionary = {}

        for element in my_list:
            if element in my_dictionary:
                my_dictionary[element] += 1
            else:
                my_dictionary[element] = 1

        return my_dictionary

    @classmethod
    def greatest_frequency(cls, my_list: list):
        my_dictionary = cls.__dictionary_creation(my_list) 
        max_appearances = 0
        most_common = 0

        for element in my_dictionary:
            if my_dictionary[element]>=max_appearances:
                max_appearances = my_dictionary[element]
                most_common = element

        return most_common

    @classmethod
    def doubles(cls, my_list: list): 
        my_dictionary = cls.__dictionary_creation(my_list) 
        counter = 0

        for element in my_dictionary:
            if my_dictionary[element]>=2: 
                counter += 1
        
        return counter

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))