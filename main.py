class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        merge_array = nums1 + nums2
        merge_array.sort()
        median = 0

        
        if m == 0 and n == 0:
            return None
        elif m + n == 1:
            median = merge_array[0]
        elif m + n == 2:
            median = (merge_array[0] + merge_array[1]) / 2.0
        elif m + n > 3 and (m + n) % 2 == 0:
            middle_index = len(merge_array) // 2
            middle_element = merge_array[middle_index]
            second_middle_index = (len(merge_array) // 2) - 1
            second_middle_element = merge_array[second_middle_index]
            median = (middle_element + second_middle_element) / 2.0
        elif (m + n) % 2 == 1:
            middle_index = len(merge_array) // 2
            median = merge_array[middle_index]

        return median

solution = Solution()
nums1 = [3]
nums2 = [-2, -1]

print(solution.findMedianSortedArrays(nums1, nums2))


    
