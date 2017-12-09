class Solution(object):
    def combine(self, a, b):
        output = []
        for i in a:
            for j in b:
                output.append(i + j)

        return output
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        map_ = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        output = map_[digits[0]]

        if len(digits) > 1:
            for d in digits[1:]:
                output = self.combine(output, map_[d])
        else:
            output = map(lambda x: x, output)
            
        return output
        
solution = Solution()

print solution.letterCombinations("2")