def count(lis):
    if lis == []:
        return 0
    else:
        return 1 + count(lis[1:])


print(count([2, 4, 6]))
