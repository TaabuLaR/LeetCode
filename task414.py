def third_max(nums):
    changeable_nums = list(set(nums))
    max_value = max(changeable_nums)
    for i in range(2):
        index = changeable_nums.index(max_value)
        del changeable_nums[index]

        if not changeable_nums:
            return max(nums)

        max_value = max(changeable_nums)

    return max_value


def main():
    test = [10, 15, 15, 25]
    print(third_max(test))


if __name__ == "__main__":
    main()
