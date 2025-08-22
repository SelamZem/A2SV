class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = m + n
        ptr = x - 1

        if m == 0:
            nums1[:n] = nums2
            return
        if n == 0:
            return

        while ptr >= 0:
            if n <= 0:
                return
            if m <= 0:
                nums1[:n] = nums2[:n]
                return

            if nums2[n-1] >= nums1[m-1]:
                nums1[ptr] = nums2[n-1]
                n -= 1
            else:
                nums1[ptr] = nums1[m-1]
                m -= 1
            ptr -= 1
