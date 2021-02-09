def remove_element(nums: list, val: int) -> int:
    j = 0
    for i, _ in enumerate(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    if j == 0:
        return j
    else:
        return len(nums[:j]), nums[:j], j


print(remove_element([0,1,2,2,3,0,4,2,0,0,4,4,2,2], 2))
