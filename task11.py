def max_area(height):
    max_volume = 0
    left = 0

    for n in range(1, len(height)):
        volume1 = (n - left) * min(height[n], height[left])  # n wall will a new right
        volume2 = min(height[n], height[n - 1])  # n wall will a new right; n-1 wall will new left

        max_volume = max(max_volume, volume1, volume2)

        # if volume2 is greater
        if height[n - 1] - height[left] >= n - 1 - left:
            left = n - 1

        # print(left, n, volume1, volume2, max_volume)
    return max_volume


def main():
    test = [1,2,3,4,5,6]
    print(max_area(test))


if __name__ == "__main__":
    main()
