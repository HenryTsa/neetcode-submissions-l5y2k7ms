class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_dic = {}
        res_dic = {char : s2[0:len(s1)].count(char) for char in s2[0:len(s1)]}
        print(res_dic)
        for char in s1:
            s1_dic[char] =  1 + s1_dic.get(char,0)
        print(s1_dic)
        for l in range(len(s2)-len(s1)+1):
            if res_dic == s1_dic:
                return True
            res_dic[s2[l]]-=1
            if res_dic[s2[l]]==0:
                del res_dic[s2[l]]
            if l + len(s1) < len(s2):
                res_dic[s2[l+len(s1)]] =  1 +res_dic.get(s2[l+len(s1)],0)
            #print(res_dic)
        return False