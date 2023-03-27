def contains_duplicate(nums):
    return not (len(nums) == len(set(nums)))


def main():
    test = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate(test))


if __name__ == "__main__":
    main()
