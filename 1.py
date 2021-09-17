def min3(a1, a2, a3):
    return min(a1, a2, a3)


def equals3(a1, a2, a3):
    if a1 == a2 == a3:
        return 3
    elif a1 == a2 != a3 or a1 == a3 != a2 or a1 != a2 == a3:
        return 2
    else:
        return 0


def array_sum(arr):
    return sum(arr)


def array_zeros(arr):
    return sum(map(lambda x: 1 if x == 0 else 0, arr))


a = list(map(int, input().split()))
if len(a) == 3:
    print('min or equals?\n1: min\n2: equals\n3: zeros')
    command = int(input())
    if command == 1:
        print(min3(a[0], a[1], a[2]))
    elif command == 2:
        print(equals3(a[0], a[1], a[2]))
    elif command == 3:
        print(array_zeros(a))
else:
    print('sum or zeros?\n1: sum\n2: zeros')
    command = int(input())
    if command == 1:
        print(array_sum(a))
    elif command == 2:
        print(array_zeros(a))
