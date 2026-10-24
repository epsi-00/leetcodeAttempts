# Brute Force Approach

# Time: O(n²)

# Hashmap Approach

# Time O(n)
# Space O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # hashmap, val : index

        for i, n in enumerate(nums): # gets index & current number
            diff = target - n # calculates number needed to reach target
            if diff in prevMap: # checks if diff is in hash map
                return [prevMap[diff], i] # return the two numbers' indices
            prevMap[n] = i # stores current number and its index for future lookup
        return