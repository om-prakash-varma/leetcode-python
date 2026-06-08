#link: https://leetcode.com/problems/find-common-characters?envType=problem-list-v2&envId=v1e5lgb3

'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''
from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        return list(common.elements())        
'''
Approach:
---------
Count the frequency of each character in the first word.

For every remaining word, keep only the characters that
appear in both words with their minimum frequency.

Finally, return all remaining characters, including duplicates.

Why:
----
A character is common only if it appears in every word.
Using frequency counts helps track how many times each
character can appear in the final answer.

Time Complexity: O(n * m)
Space Complexity: O(1)
'''