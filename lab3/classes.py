import math
#exercise 1

class Strings:
    stroka: str
    def getString(self, stroka):
        self.stroka = stroka
    def printString(self):
        print(self.stroka)

#exercise 2

class Shape:
    length: float
    area: float
    def __init__(self):
        self.area = 0
    def calculateArea(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def calculateArea(self):
        self.area = self.length * self.length
        return self.area

#exercise 3

class Rectangle(Shape):
    width: float
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def calculateArea(self):
        self.area = self.length * self.width
        return self.area
#exercise 4
class Point:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x = {self.x}, y = {self.y}")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, x, y):
        return math.sqrt((x - self.x)**2 + (y - self.y)**2)

#exercise 5

class Account:
    owner: str
    balance: int
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, deposit):
        self.balance += deposit
    def withdraw(self, withdraw):
        if(self.balance < withdraw):
            print("Account shall not be overdrawn")
            return -1
        self.balance -= withdraw
        return 1
acc = Account('vasya_pupkin', 0)
acc.deposit(123)
print(acc.balance)
acc.withdraw(100)
print(acc.balance)
acc.withdraw(100)

#exercise 6

def filt(n):
    if n<2: return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

l = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

nums = list(filter(lambda x:filt(x), l))
print(nums)