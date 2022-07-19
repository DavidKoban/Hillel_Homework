def options_count(n):
    if n < 0:
        return 0
    elif n == 1 or n == 2:
        return n
    elif n == 3:
        return options_count(n - 1) + options_count(n - 2) +1
    else:
        return options_count(n-1) + options_count(n-2) + options_count(n-3)


if __name__ == "__main__":
    n = int(input("Введите число ступенек ->\n"))
    print(options_count(n))

