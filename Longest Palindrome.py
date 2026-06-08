#link: https://leetcode.com/problems/longest-palindrome?envType=problem-list-v2&envId=v1e5lgb3

'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        length = 0
        odd_found = False

        for freq in count.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length
'''
Approach:
---------
Count the frequency of each character.
For every character:
1. Use all possible pairs in the palindrome.
2. If a character has an odd count, one occurrence can
   be placed in the center.
After adding all pairs, add 1 if any character has an
odd frequency.
Why:
----
A palindrome is symmetric, so characters are mainly used
in pairs. At most one character with an odd count can
occupy the center position.
Time Complexity: O(n)
Space Complexity: O(1)
'''