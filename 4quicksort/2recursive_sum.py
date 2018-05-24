def sum(lis):
    if len(lis) == 0:
        return 0
    else:
        return lis[0] + sum(lis[1:])


print(sum([2, 4, 6]))
