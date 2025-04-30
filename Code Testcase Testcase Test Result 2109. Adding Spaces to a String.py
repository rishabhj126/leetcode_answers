class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str

        Looping spaces (Exceeded Time Limit)-
        1. Create new empty string
        2. loop spaces and till the value location arrive, keep adding indexes from s
        3. return new string

        newStr = ""
        indexOfs = 0
        if(len(spaces) == 0):
            return s
        for space in spaces:
            newStr += s[indexOfs: space] + " "
            indexOfs = space
        newStr += s[indexOfs:]
        if(spaces.pop() == len(s)):
            return newStr[: -1]
        return newStr

        Split and join
        1. Split s at spaces
        2. join with space between
        """
        words = []
        lastIndex = 0
        for space in spaces:
            words.append(s[lastIndex: space])
            lastIndex = space
        words.append(s[lastIndex:])
        return " ".join(words)
