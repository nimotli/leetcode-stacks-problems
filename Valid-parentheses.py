#NAME : VALID PARENTHESES
#CATEGORY : STACKs
#DIFFICULTY : EASY
#LINK : https://leetcode.com/problems/valid-parentheses/
def getOpener(car):
    if car==')':
        return '('
    elif car == ']':
        return '['
    elif car == '}':
        return '{'
    return ''

def isValid(s):
    stack = []
    for car in s:
        if len(stack)==0:
            stack.append(car)
        elif getOpener(car)==stack[len(stack)-1]:
            stack.pop()
        else :
            stack.append(car)
    return len(stack)==0

s="({[)"

print(isValid(s))