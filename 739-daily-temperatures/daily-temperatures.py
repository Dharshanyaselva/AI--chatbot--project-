class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans[stack.pop()] = idx - stack[-1]
            
            stack.append(idx)
        
        return ans
      