class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "/": lambda a, b: int(b / a),
            "*": lambda a, b: a * b
        }
        for i in tokens:
            if i in ops:
                stack.append(ops[i](stack.pop(), stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]
