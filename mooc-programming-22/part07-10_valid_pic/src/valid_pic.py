from datetime import *

def is_it_valid(pic: str):
    if pic[6]=='+':
        try:
            date = datetime(int("18"+pic[4:6]), int(pic[2:4]), int(pic[0:2])).strftime("%d%m%Y")
        except ValueError:
            return False
    elif pic[6]=='-':
        try:
            date = datetime(int("19"+pic[4:6]), int(pic[2:4]), int(pic[0:2])).strftime("%Y%m%d")
        except ValueError:
            return False
    elif pic[6]=='A':
        try:
            date = datetime(int("20"+pic[4:6]), int(pic[2:4]), int(pic[0:2])).strftime("%Y%m%d")      
        except ValueError:
            return False
    else:
        return False

    my_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    identifier = int(int(pic[0:6]+pic[7:10])%31)

    if my_str[identifier]==pic[10] and len(pic)==11:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("080842-720N"))