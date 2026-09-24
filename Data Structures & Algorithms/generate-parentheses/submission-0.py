class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opencount,closecount,path):
            #print(opencount,closecount,path)
            if len(path) == 2*n:
                res.append("".join(path))
                return
            if opencount < n:
                path.append('(')
                opencount += 1
                backtrack(opencount,closecount,path)
                opencount -= 1
                path.pop()
            if closecount < opencount:
                path.append(')')
                closecount += 1
                backtrack(opencount,closecount,path)
                closecount -= 1
                path.pop()
        backtrack(0,0,[])
        return res
