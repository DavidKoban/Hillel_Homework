import decimal


def options_count(n):
    n = n + 1
    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


if __name__ == "__main__":
    n = int(input("Введите число ступенек ->\n"))
    print(options_count(n))
    