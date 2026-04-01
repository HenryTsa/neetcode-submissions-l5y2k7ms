class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_dic = {}
        
        for char in s1:
            s1_dic[char] =  1 + s1_dic.get(char,0)
        #print(s1_dic)
        for l in range(len(s2)-len(s1)+1):
            res_dic = {}
            for idx in range(len(s1)):
                res_dic[s2[l + idx]] = 1 + res_dic.get(s2[l + idx],0)
            if res_dic == s1_dic:
                return True
            #print(res_dic)
        return False