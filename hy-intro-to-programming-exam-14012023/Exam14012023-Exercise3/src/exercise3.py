def points(stats):
    data = stats.split(":")
    statistics  = data[1].split("-")

    if statistics[0].isdigit() and statistics[1].isdigit() and statistics[2].isdigit():
        win = int(statistics[0])
        loss = int(statistics[1])
        tie = int(statistics[2])
    else:
        raise ValueError("All stats were not Integers")

    points = win*3+tie*1
    return points

if __name__ == "__main__":
    print(points("Heba hawks:5-6-1"))
    print(points("Brewsters:3-12-10"))
    print(points("Sleepers:0-0-0"))
    print(points("Kumpula Intelligence:0-8-1"))
    #print(points("KBC:AAA-1-ll"))
    #print(points("Navy jerries:7-xx-1"))
    #print(points("Loosisters:8-5-abb"))
    #print(points("KBC:6-xx-1"))