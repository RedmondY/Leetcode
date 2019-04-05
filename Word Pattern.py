'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split(' ')
        if len(pattern) != len(s):
            return False
        
        p2s_d = {}
        s2p_d = {}

        for i, p in enumerate(pattern):
            if p2s_d.get(p, None):
                if p2s_d[p] != s[i]:
                    return False
            else:
                p2s_d[p] = s[i]

            if s2p_d.get(s[i], None):
                if s2p_d[s[i]] != p:
                    return False
            else:
                s2p_d[s[i]] = p

        return True