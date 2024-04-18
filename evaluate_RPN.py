class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['*','-','+','/']
        stack =[]
        for char in tokens:
            if char in operators:
                last_char = stack.pop()
                second_last_char = stack.pop()
                try:
                    if char == "+":
                        ans = int(second_last_char) + int(last_char)
                        # print(f"{second_last_char}+{last_char}: {ans}")
                    elif char == "-":
                        ans = int(second_last_char) - int(last_char)
                        # print(f"{second_last_char}-{last_char}: {ans}")
                    elif char == "*":
                        ans = int(second_last_char) * int(last_char)
                        # print(f"{second_last_char}*{last_char}: {ans}")
                    else :
                        ans = int(int(second_last_char) / int(last_char))
                        # print(f"{second_last_char}//{last_char}: {ans}")
                    stack.append(round(ans))
                except Exception as e:
                    return f"Error occured: {e}"
            else:
                stack.append(char)
        return int(stack[0])