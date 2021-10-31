'''
https://leetcode.com/problems/first-missing-positive/

41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
Example 1:
Input: nums = [1,2,0]
Output: 3
Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

p.s.:
Success
Details 
Runtime: 832 ms, faster than 89.48% of Python3 online submissions for First Missing Positive.
Memory Usage: 68.1 MB, less than 25.38% of Python3 online submissions for First Missing Positive.
'''

class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        nums_p = [x for x in nums if x > 0]
        for i in range(len(nums_p)):
            if i+1 !=nums_p[i]: return i+1
        return len(nums_p)+1

nums = [1,4,2,0]

nums = [0,2,2,1,1]

s = Solution()
print(s.firstMissingPositive(nums))