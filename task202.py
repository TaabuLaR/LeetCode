def is_happy(n):
    summ = 0
    num = str(n)
    been = []
    while summ != 1:
        summ = 0
        for s in num:
            summ += int(s) ** 2
        num = str(summ)
        if num in been:
            return False
        been.append(num)

    return True


def main():
    test = 19
    print(is_happy(test))


if __name__ == "__main__":
    main()
