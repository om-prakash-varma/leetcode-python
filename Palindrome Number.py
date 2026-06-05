"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

'''
Approach:
---------
Convert the number to a string and compare it with its reverse.

If both are the same, the number reads the same from left to right
and right to left, so it is a palindrome.

Why:
----
Reversing a string in Python is simple and allows us to check
for a palindrome in one line.

Time Complexity: O(n)
Space Complexity: O(n)
'''