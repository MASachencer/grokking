def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


def countdown2(i):
    while i > 0:
        print(i)
        i -= 1


countdown(5)
countdown2(5)
