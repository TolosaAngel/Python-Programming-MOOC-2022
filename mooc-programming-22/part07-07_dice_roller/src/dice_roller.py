from random import choice

def roll(die: str):
    dieA = "333336"
    dieB = "222555"
    dieC = "144444"

    if die=="A":
        return int(choice(dieA))
    elif die=="B":
        return int(choice(dieB))
    else:
        return int(choice(dieC))

def play(die1: str, die2: str, times: int):
    die1wins = die2wins = draws = 0
    
    for i in range(times):
        die1_value = roll(die1)
        die2_value = roll(die2)

        if die1_value>die2_value:
            die1wins += 1
        elif die1_value<die2_value:
            die2wins += 1
        else:
            draws += 1
    
    return die1wins,die2wins,draws

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    print()

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)