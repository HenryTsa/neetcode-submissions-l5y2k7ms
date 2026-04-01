class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_idx = len(numbers)-1
        left_idx = 0
        while right_idx >= left_idx:
            tempt = numbers[left_idx] + numbers[right_idx]
            if tempt < target:
                left_idx += 1
            elif tempt > target:
                right_idx -=1
            else:
                return [left_idx+1,right_idx+1]
        return []