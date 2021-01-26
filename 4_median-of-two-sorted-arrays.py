class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()

        if len(nums1) > 1:
            x = 0
            for num in nums1:
                x = x + num
            output = x / len(nums1)
        elif len(nums1) == 1:
            output = nums1[0]
        elif len(nums1) == 0:
            output = "Error - no values found."

        print(output)


s = Solution()
s.findMedianSortedArrays([1, 3, 5, 6, 10], [4, 6, 7, 8])