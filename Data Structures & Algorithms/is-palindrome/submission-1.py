class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tempt = ""
        for char in s:
            c = char.lower()
            if ("a" <= c <= "z") or ("0" <= c <= "9"):
                tempt = tempt + char.lower()
        #print(tempt)
        left_idx = 0
        right_idx = len(tempt)-1 
        while left_idx < right_idx:
            print(s[left_idx],s[right_idx])
            if tempt[left_idx]!= tempt[right_idx]:
                return False
            else:
                left_idx += 1
                right_idx -= 1

        return True