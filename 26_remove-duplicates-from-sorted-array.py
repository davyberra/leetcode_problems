import time

def remove_duplicate(nums: list) -> int:
    if len(nums) <= 1:
        return len(nums)
    else:
        current_place = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[current_place] = nums[i]
                current_place += 1
        print(nums)
        return len(nums[:current_place]), nums[:current_place]
t_0 = time.time()
print(remove_duplicate([0,0,1,1,1,2,2,3,3,4,7,12,12,13,15,15,16,16,16,45,67,67,67]))
print(time.time() - t_0)

