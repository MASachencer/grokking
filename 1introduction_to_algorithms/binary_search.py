def binary_search(lis, item):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lis[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


my_lis = [1, 3, 5, 7, 9]

print(binary_search(my_lis, 3))
print(binary_search(my_lis, -1))
