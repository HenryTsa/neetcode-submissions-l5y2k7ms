class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def backtrack(start,path):
            print(start,path)
            if start == len(s):
                #print("heheee")
                res.append(path.copy())
                return 
            
            for i in range(start+1,len(s)+1):
                sub = s[start:i]
                #print("sub",sub)
                # 判斷回文
                if sub == sub[::-1]:
                    #print("hi",i,path)
                    path.append(sub)
                    backtrack(i,path)
                    path.pop()


        backtrack(0, [])
        return res