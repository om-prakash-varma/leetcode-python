#Link: https://leetcode.com/problems/add-strings?envType=problem-list-v2&envId=v1e5lgb3

'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(result[::-1])
    
'''
Approach:
---------
Simulate the way we add numbers by hand.

Start from the last digit of both strings and move left.
For each pair of digits:
1. Add the digits and the carry.
2. Store the last digit of the sum.
3. Update the carry.
4. Continue until all digits and carry are processed.

Finally, reverse the collected digits to get the answer.

Why:
----
Since the numbers are given as strings and cannot be converted
directly to integers, we perform digit-by-digit addition.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
'''