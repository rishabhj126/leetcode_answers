class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int

        Brute Force:
        1. Split sentence into list of words
        2. Iterate and find word start with searchWord
        3. if found, return index
        4. finally return -1
        """
        words = sentence.split(" ")
        for word in words:
            if(word.startswith(searchWord)):
                return words.index(word) + 1
        return -1
        
