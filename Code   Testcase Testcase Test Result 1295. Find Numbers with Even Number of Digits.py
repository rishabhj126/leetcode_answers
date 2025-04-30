class Solution(object):

    def checkIfEvenLength(self, num):
        return len(str(num)) & 1 == 0

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Brute force-
        1. Iterate each number 
        2. Check length is even. if yes, increase count
        3. return count


        """
        count_of_even_number = 0
        for num in nums:
            
            if self.checkIfEvenLength(num):
                count_of_even_number += 1

        return count_of_even_number
