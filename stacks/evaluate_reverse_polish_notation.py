class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #pop 2 for operators, but then pop back in thr total value
        #push 1 for numbers
        #only one stack for numbers
        nums = []
        operators = ["+", "-", "*", "/"]
        for s in tokens:
            if s not in operators:
                nums.append(int(s))
                #do not keep as token, make sure to turn a string -> number
            else:#does action as variable is created
                b= nums.pop()
                a= nums.pop()
                if s == "+":
                    nums.append(a + b)
                elif s == "-":
                    nums.append(a - b)
                elif s == "*": 
                    nums.append(a * b) 
                else:
                    nums.append(int(float(a) / b))
                    ###makr dutr to truncate down (automatically done by int())
        return nums[0]
    

"""
Core idea:
Numbers get pushed onto the stack.
Operators use the two most recent numbers.

Why stack:
The operation always uses the most recent available operands.
This is Last In, First Out.

The 32-bit integer statement means all answers and intermediate results
fit in the normal integer range. In Python, this does not change much
because Python integers can already grow large.

The main tricky part is division:
LeetCode wants integer division truncated toward zero, so use:
    int(float(a) / b)
instead of:
    a // b
because // floors negative numbers in Python.
"""