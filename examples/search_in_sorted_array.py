def find_x_in_sorted_array(nums, x):
    for i, num in enumerate(nums):
        if x == num:
            return i


print(find_x_in_sorted_array([1, 2, 3, 4, 5, 6, 7, 8], 6))
