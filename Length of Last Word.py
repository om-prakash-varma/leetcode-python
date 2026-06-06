#link: https://leetcode.com/problems/length-of-last-word/description/
'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])  
    
'''
Approach:
---------
Remove leading and trailing spaces using strip().

Split the string into words using split() and
return the length of the last word.

Why:
----
split() separates the string into individual words,
making it easy to access the last word and find its length.

Time Complexity: O(n)
Space Complexity: O(n)
'''