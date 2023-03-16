abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

layers = int(input("Layers: "))
rest = 0

word = ""

while layers!=0:
    word = word[0:rest]+abc[layers-1]*(layers*2-1)+word[len(word)-rest:len(word)]
    print(word)

    layers-=1
    rest+=1

layers+=2
rest-=2

while rest>=0:
    word = word[0:rest]+abc[layers-1]*(layers*2-1)+word[len(word)-rest:len(word)]
    print(word)

    layers+=1
    rest-=1