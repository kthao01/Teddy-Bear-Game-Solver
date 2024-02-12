import sys

def last_2_digits(number):       #function for getting product of last two digits
    a_string = str(number)       #by turning to string and slicing
    a_length = len(a_string)
    c = a_string[a_length - 1: a_length]
    b = a_string[a_length - 2: a_length-1]
    return int(c) * int(b)


def bears(n):

    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""

    if n == 42:           #checks if n is less that 42 or is 42 
        return True
    elif n < 42:
        return False

    if n%2 == 0 and bears(n//2):  #if n is divisable by 2 calls function for n//2
        return True
    elif n%3 == 0 and bears(n-last_2_digits(n)): #if n is divisable by 3 or 4 calls function for n-product
        return True                              #of last two digits
    elif n%4 == 0 and bears(n-last_2_digits(n)):
        return True
    elif n%5 == 0 and bears(n-42):   #if n is divisable by 5 calls for n-42
        return True
    return False

sys.setrecursionlimit(1500)      #kept on getting a recursion error and this fixed it
print(bears(250))

