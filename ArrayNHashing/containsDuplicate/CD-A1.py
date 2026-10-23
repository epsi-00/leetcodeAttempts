## Brute Force approach

# Time: O(n²)
# Space: O(1)

## Sorting approach

# Iterates the array only once

# Time: O(n log n)
# Space: O(1)

## HashSet approach

# sacrifices memory

# Time: O(n)
# Space: O(n)

# Hashset solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set() # creates an empty set to store numbers previously encountered

        for n in nums: # iterates each element in nums
            if n in hashset: # checks if element is in hashset
                return True # if element is duplicated return True
            hashset.add(n) # if not add current number and remember for future interations
        return False # returns False if no duplicates are found