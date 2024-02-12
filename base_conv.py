


def base_sym(var):   #function to help get base
    if var < 10:
        return str(var)
    elif var == 10:
        return 'A'
    elif var == 11:
        return 'B'
    elif var == 12:
        return 'C'
    elif var == 13:
        return 'D'
    elif var == 14:
        return 'E'
    elif var == 15:
        return 'F'


def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    div = num//b
    r = num%b
    if div == 0:
        return base_sym(r)     #if num can be divided by b returns base
    else:
        return convert(div,b) + base_sym(r)    #calls itself after getting quotient plus the base

num = int(input('number: '))
b = int(input('b: '))

print(convert(num,b))
