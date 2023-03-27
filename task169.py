def majority_element(nums):
    all_elements = set(nums)
    for el in all_elements:
        if nums.count(el) > len(nums) / 2:
            return el

def main():
    test = [1, 2, 2]
    print(majority_element(test))


if __name__ == "__main__":
    main()