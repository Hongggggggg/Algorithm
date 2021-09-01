def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_loc = i
        for j in range(i + 1, len(nums)):
            if nums[min_loc] > nums[j]:
                min_loc = j
        nums[min_loc], nums[i] = nums[i], nums[min_loc]
        print(nums)
    return nums


nums = [5, 6, 4, 8, 3, 2, 0, 9, 1]
selection_sort(nums)
