43827 : 7 -> 6261
1827 : 7 -> 261
427 : 7 -> 61
7 :7 - > 1

def func(x, y):
    temp = x/1000
    if x > y:
        return x/y + func(x%1000)
    if res > y:
        return func(x-1, y) + res
    else:
        return res