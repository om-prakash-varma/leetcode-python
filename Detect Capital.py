# link: https://leetcode.com/problems/detect-capital?envType=problem-list-v2&envId=v1e5lgb3

'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()      
    
'''
Approach:
---------
Check if the word follows any of the valid capitalization rules:

1. All letters are uppercase (e.g., "USA")
2. All letters are lowercase (e.g., "leetcode")
3. Only the first letter is uppercase (e.g., "Google")

Return True if any of these conditions is satisfied.

Why:
----
Python provides built-in string methods that directly check
these capitalization patterns, making the solution simple and readable.

Time Complexity: O(n)
Space Complexity: O(1)
'''