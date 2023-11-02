class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split('/') 

        for x in temp:
            if x != '.' and x != '' and x != '..':
                stack.append(x)

            elif x == '..':
                if stack:
                    stack.pop()
        
        return '/' + '/'.join(stack)
