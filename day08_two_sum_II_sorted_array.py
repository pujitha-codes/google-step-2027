class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # LeetCode lo 1-indexed adugutharu
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1 # sum takkuva undi, left penchu
            else:
                right -= 1 # sum ekkuva undi, right tagginchu
