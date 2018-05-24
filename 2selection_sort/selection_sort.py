def find_smallest(lis):
    smallest = lis[0]
    smallest_index = 0
    for i in range(1, len(lis)):
        if lis[i] < smallest:
            smallest = lis[i]
            smallest_index = i
    return smallest_index


def selection_sort(lis):
    new_lis = []
    for i in range(len(lis)):
        smallest = find_smallest(lis)
        new_lis.append(lis.pop(smallest))
    return new_lis


def find_smallest2(lis):
    smallest = lis[0]
    for i in lis[1:]:
        if i < smallest:
            smallest = i
    return smallest


def selection_sort2(lis):
    new_lis = []
    for i in range(len(lis)):
        smallest = find_smallest2(lis)
        new_lis.append(smallest)
        lis.remove(smallest)
    return new_lis


print(selection_sort([5, 3, 6, 2, 10]))
print(selection_sort2([5, 3, 6, 2, 10]))
