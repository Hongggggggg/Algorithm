#https://leetcode-cn.com/problems/4sum-ii/
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hash_map = dict()
        for i in nums1:
            for j in nums2:
                key = i + j
                if key in hash_map:
                    hash_map[key] += 1
                else:
                    hash_map[key] = 1
        count = 0
        for i in nums3:
            for j in nums4:
                key = - i - j
                if key in hash_map:
                    count += hash_map[key]
        return count
        
