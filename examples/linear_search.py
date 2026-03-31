def find_index(nums, target):
    for i, value in enumerate(nums):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    print(find_index([10, 20, 30, 40], 30))

