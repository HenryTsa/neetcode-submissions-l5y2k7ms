class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        zero_num = 0
        for number in nums:
            if number != 0:
                cur = cur * number
            else:
                zero_num += 1
        #print(zero_num)
        answer = []
        for number in nums:
            if zero_num >= 2:
                answer.append(0)
                continue
            elif zero_num == 1:
                if number != 0:
                    answer.append(0)
                else:
                    answer.append(cur)
            else:
                answer.append(int(cur/number))
        
        return answer