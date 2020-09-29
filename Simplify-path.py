#NAME : SIMPLIFY PATH
#CATEGORY : STACKs
#DIFFICULTY : MEDIUM
#LINK : https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitPath = path.split('/')
        for val in splitPath:
            if val == "":
                print("nothing")
            elif val == ".":
                print("nothing")
            elif val == "..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append("/"+val)
        if(len(stack)==0):
            stack.append("/")
        return"".join(stack)