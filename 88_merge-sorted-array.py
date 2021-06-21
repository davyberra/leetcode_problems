class Solution:
    def merge(self, nums1: list, m, nums2: list, n):
        j = 0
        temp = None
        if m == 0:
            nums1 = nums2
        elif n != 0:
            for i in range(m + n):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    j += 1
                else:
                    if not temp:
                        temp = nums1[i]
                    if temp <= nums2[j]:
                        nums1[i] = temp
                    else:
                        nums1[i] = nums2[j]
                        j += 1


