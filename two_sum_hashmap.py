def twoSum(nums, target):
    seen = {} # dictionary/hashmap: number -> index

    for i, num in enumerate(nums):
        complement = target - num # manaki kavalsina number

        if complement in seen:
            return [seen[complement], i] # dorikindi!

        seen[num] = i # ee number ni store cheddam

    return [] # dorakaledhu

# Test
print(twoSum([2, 7, 11, 15], 9)) # Output: [0, 1]
print(twoSum([3, 2, 4], 6)) # Output: [1, 2]
print(twoSum([3, 3], 6)) # Output: [0, 1]