def quicksort(lis):
    if len(lis) < 2:
        return lis
    else:
        pivot = lis[0]
        greater = [i for i in lis[1:] if i >= pivot]
        less = [i for i in lis[1:] if i <= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
