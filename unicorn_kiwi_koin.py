import sys


# Author: @Ramish fuh

def funct(a, total, number_of_unicorns):
    if number_of_unicorns == 1:
        return [total]
    if len(a) == 1 or len(a) == 2:
        a[0] = total
        a[1] = 0
        return a
    else:
        b = funct(a[1:], total, number_of_unicorns - 1)
        counter = 0
        c = [(i, b[i]) for i in range(len(b))]
        c.sort(key=lambda tup: tup[1])
        _sum = 0
    while counter < (number_of_unicorns - 1) // 2:
        arr_index, arr_value = c[counter]
        a[arr_index + 1] = arr_value + 1
        counter += 1
        _sum += arr_value + 1
    total -= _sum
    a[0] = total
    return a


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please enter a list of numbers to sort")
        sys.exit(1)
    passed_args = [x for x in args]
    unicorn, total = passed_args[0], passed_args[1]
    unicorn = int(unicorn)
    total = int(total)
    print(funct([0] * unicorn, total, unicorn))
