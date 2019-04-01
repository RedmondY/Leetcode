'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


'''

'''
当s = ''的时候，肯定为true
设置一个列表来存储s中的词是否存在于wordDict中
之后设置两个循环
第一个循环从s最后一个字母开始 
第二个循环一个个开始找 如果存在于wordDict中则 设置列表中为True


'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':  
            return True
        checklist = [False]*(len(s)+1)
        checklist[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict and checklist[j+1] == True:
                    checklist[i]=True
        return checklist[0]