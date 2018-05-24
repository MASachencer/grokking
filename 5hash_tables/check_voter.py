voted = {}
voted2 = set()


def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')


def check_voter2(name):
    if name in voted2:
        print('kick them out!')
    else:
        voted2.add(name)
        print('let them vote!')


check_voter('tom')
check_voter('mike')
check_voter('mike')
check_voter2('tom')
check_voter2('mike')
check_voter2('mike')
