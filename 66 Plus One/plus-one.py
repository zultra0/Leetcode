from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        number = ''
        plusOneArray = []
        for x in range(len(digits)):
            number += str(digits[x])
        plusOne = int(number) + 1
        plusOneString = str(plusOne)
        for x in range(len(plusOneString)):
            plusOneArray.append(plusOneString[x])
        return list(map(int, plusOneArray))