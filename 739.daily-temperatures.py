class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # this stores only indxes of the temperatures.
        result_stack = [0] * len(temperatures) # store the results in this array

        # General cases
        for index in range(0,len(temperatures)-1):
            if temperatures[index] < temperatures[index+1]:
                result_stack[index] = 1
                counter = len(stack)
                while counter>0 and temperatures[stack[counter-1]] < temperatures[index+1]:
                    a = stack[counter-1] # replace a with a proper variable name
                    b = index + 1 - a # replace b with a proper variable name
                    result_stack[a] = b
                    counter -= 1
                    stack.pop()
            else:
                stack.append(index)
        return result_stack
        