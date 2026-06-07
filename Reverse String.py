# link: https://leetcode.com/problems/reverse-string?envType=problem-list-v2&envId=v1e5lgb3

'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

'''
Approach:
---------
Use two pointers: one at the beginning and one at the end.

Swap the characters at both pointers, then move them
towards the center. Continue until the pointers meet.

Why:
----
Swapping characters from both ends reverses the string
in-place without using extra memory.

Time Complexity: O(n)
Space Complexity: O(1)
'''