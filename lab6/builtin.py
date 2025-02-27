def task1(numbers):
    
    return eval('*'.join(list(map(str, numbers))))

def task2(s):

    uppercasse = len([i for i in s if i.isupper()])

    lowercase = len([i for i in s if i.islower()])

    print(f'uppercase letters = {uppercasse}\nlowercase letters = {lowercase}')



def task3(s):

    print(True if s == s[::-1] else False)

def task4():

    from time import sleep
    from math import sqrt
    num = int(input("input number: "))
    sleepTime = int(input("input seconds: "))

    sleep(sleepTime / 1000)

    print(f'Square root of {num} after {sleepTime} miliseconds is {sqrt(num)}')

def task5(tup):
    
    return True if all(tup) else False

# task4()
# print(task1([1,2,34]))