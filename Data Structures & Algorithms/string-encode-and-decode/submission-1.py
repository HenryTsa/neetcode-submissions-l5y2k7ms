class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for i in range(len(strs)):
            encoded_string.append(strs[i])
            encoded_string.append("~")
        
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        cur_word = []
        answer = []
        for i in range(len(s)):
            if s[i]!="~":
                cur_word.append(s[i])
            else :
               
                cur_word = "".join(cur_word)
                print(cur_word)
                answer.append(cur_word)
                cur_word = []
        print(answer)
        return answer