class Solution:
    def canJump(self, nums: list) -> bool:
        def recursor(cur_index, cur_num, h):
            i = cur_num
            if (cur_index + i) >= len(nums) - 1:
                return True
            while i > 0:
                if nums[cur_index + i] != 0 and cur_index + i not in h:
                    h[cur_index + i] = True
                    result = recursor(cur_index + i, nums[cur_index + i], h)
                    if result:
                        return result

                i -= 1

        if len(nums) == 1:
            return True
        h = {}
        output = recursor(0, nums[0], h)
        return output or False

s = Solution()
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

