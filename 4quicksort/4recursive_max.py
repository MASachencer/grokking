def max2(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        return lst[0] if lst[0] > max2(lst[1:]) else max2(lst[1:])


print(max2([2, 4, 6]))
