from itertools import permutations
#exercise 1
def grammsToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

#exercise 2
def fahrenheitToCelsius(Fahrenheit: float):
    Celsius = (5 / 9) * (Fahrenheit - 32)
    return Celsius

#exercise 3
def solve(numheads, numlegs):
    c = -(numlegs-4*numheads)/2
    r = numheads-c
    return r, c

#exercise 4
def filter_prime(l):
    nwl = []
    for i in l:
        if i < 1:
            continue
        check = True
        for j in range(2, int(pow(i, 1/2))+1):
            if i%j == 0:
                check = False
                break
        if check:
            nwl.append(i)
    return nwl

#exercise 5
def perm(s):
    return list(permutations(s))

#exercise 6
def changeOrder(s):
    print(' '.join(reversed(s.split())))


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        
    return False

def sph_vol(r):
    from math import pi
    return (4/3) * pi * (r**3)


def uniqueList(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i) 
    return res

def is_pal(s):
    return True if s == s[::-1] else False

def hist(arr):
    for i in arr:
        print('*' * i)


def guessNumber():
    from random import randint
    rand = randint(1, 20)

    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')
    counter = 0
    while True:
        num = int(input())
        counter += 1
        if num < rand:
            print('Your guess is too low.\nTake a guess.')
        elif num> rand:
            print('Your guess is too high.\nTake a guess.')
        else:
            print(f'Good job, {name}! You guessed my number in {counter} guesses!')
            break