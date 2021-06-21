class Solution:
    def merge(self, nums1: list, m, nums2: list, n):
        temp = []
        for i in range(m + n):
            if i < m:
                temp.append(nums1[i])
            if len(nums2) > 0 and len(temp) > 0:
                if temp[0] >= nums2[0]:
                    nums1[i] = nums2.pop(0)
                else:
                    nums1[i] = temp.pop(0)
            elif len(nums2) == 0:
                nums1[i] = temp.pop(0)
            elif len(temp) == 0:
                nums1[i] = nums2.pop(0)


