def is_power_of_two(n):
    while True:
        if n == 1:
            return True
        elif (n * 10) % 10 != 0:
            return False
        n /= 2


def main():
    test = 1
    print(is_power_of_two(test))


if __name__ == "__main__":
    main()
