def oldest_person(people: list):
    pos = 0

    for i in range(1,len(people)):
        if people[i][1]<=people[pos][1]:
            pos = i

    return people[pos][0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))

    people_list = [("Arthur", 1977), ("Emily", 2014)]
    print(oldest_person(people_list))

    people_list = [('Jacob', 2016), ('Harry', 2019), ('Oliver', 2012), ('Wendy', 2013), ('Jane Doe', 2020)]
    print(oldest_person(people_list))