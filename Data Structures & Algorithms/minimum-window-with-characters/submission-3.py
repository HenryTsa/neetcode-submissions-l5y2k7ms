class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""
        dic = {}
        res_dic = {}
        res = "A"*len(s)
        for char in t:
            dic[char] = dic.get(char,0) + 1
        #print(dic)
        for idx in range(len(t)-1):
            res_dic[s[idx]] = res_dic.get(s[idx],0) + 1
       # print(res_dic)
        
        l = 0
        if self.checkdic(dic,res_dic):
            res = s[l:len(t)]

        for r in range(len(t)-1,len(s)):
            res_dic[s[r]] = res_dic.get(s[r],0) + 1
           # print(l,r,res_dic,"check")
            while self.checkdic(dic,res_dic):
                #print(l,r,res_dic)
                res = min(s[l:r+1],res,key = len)
                res_dic[s[l]] -= 1
                if res_dic[s[l]]==0:
                    del res_dic[s[l]]
                l += 1
        if res =="A"*len(s):
            return ""
        return res
    def checkdic(self,dic1,dic2):

        for key_value in dic1.keys():
            if key_value not in dic2 :
                return False
            if dic1[key_value] > dic2[key_value]:
                return False
        #print(dic1,dic2 ,"IN")
        
        return True