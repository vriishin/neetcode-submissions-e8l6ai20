class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        rule = (len(nums1) + len(nums2)) % 2
        termlength = len(nums1) + len(nums2)

        def median(nums1, nums2, termlength):
            i = len(nums1) + len(nums2)

            while i > termlength:
                # front
                if nums1 and nums2:
                    nums1.pop(0) if nums1[0] <= nums2[0] else nums2.pop(0)
                elif nums1:
                    nums1.pop(0)
                else:
                    nums2.pop(0)

                i -= 1

                if i > termlength:
                    # back
                    if nums1 and nums2:
                        nums1.pop(-1) if nums1[-1] >= nums2[-1] else nums2.pop(-1)
                    elif nums1:
                        nums1.pop(-1)
                    else:
                        nums2.pop(-1)

                    i -= 1

            return nums1, nums2
        if rule == 1: 
            median(nums1, nums2, 1)
        else:
            median(nums1,nums2,2)

        if rule == 1 and nums1:
            return nums1[0]
        elif rule == 1 and nums2:
            return nums2[0]
        elif rule==0 and (nums1 and nums2):
            sol = ((nums1[0] + nums2[0])/2)
            return sol
        elif rule == 0 and nums1:
            sol = ((nums1[0] + nums1[1])/2)
            return sol
        elif rule == 0 and nums2:
            sol = (nums2[0] + nums2[1])/2
            return sol        
        

        