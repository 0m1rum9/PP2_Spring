def down(n):
    for i in range(n, -1, -1):
        yield i

for i in down(5):
    print(i)