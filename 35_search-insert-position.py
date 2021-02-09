def search_insert(nums: list, target: int) -> int:
    for i, val in enumerate(nums):
        if nums[i] >= target:
            return i

    return len(nums)

print(search_insert([1,3,5,6], 0))
