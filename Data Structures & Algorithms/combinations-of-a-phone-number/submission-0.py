class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        number = []
        number.append("abc")
        number.append("def")
        number.append("ghi")
        number.append("jkl")
        number.append("mno")
        number.append("pqrs")
        number.append("tuv")
        number.append("wxyz")
        if len(digits) == 0 :
            return []
        #print(number[3])
        def backtrack(index_out,path):
            # 跑出去就可以船回來了
            if index_out == len(digits):
                res.append("".join(path))
                return 
            for i in range(len(number[int(digits[index_out])-2])):
                #print("number:",number[int(digits[index_out])-2])
                path.append(number[int(digits[index_out])-2][i])
                backtrack(index_out+1,path)
                path.pop()
        backtrack(0,[])
        return res
            