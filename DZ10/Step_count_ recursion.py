def options_count(n):
    if n == 0 or n == 1:
        return 1
    else:
        return options_count(n-1) + options_count(n-2)


if __name__ == "__main__":
    n = int(input("Введите число ступенек ->\n"))
    print(options_count(n))

