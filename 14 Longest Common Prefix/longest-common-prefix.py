from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] 
        i = 1
        
        while i < len(strs): 
            j = 0
            while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]: 
                j += 1
            prefix = prefix[:j]
            i += 1
        return prefix
