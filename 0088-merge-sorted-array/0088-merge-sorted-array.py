class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
         """
    
        # Pointers for nums1, nums2, and the end of nums1 (target)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # While there are still elements to compare in nums2
        while p2 >= 0:
            # If nums1 still has elements and its current element is larger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # If nums2 element is larger or nums1 is exhausted
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        