# 第一次提交出现问题：因为第二次循环的时候出错，不能够选择下一个单词
# 将range改为当前状态即可
# 另外，感觉Python的效率真的低，C++可能就快很多
# 思路：
# 主要两个循环，第一个循环循环第一个单词，第二个循环循环下面一个，和冒泡排序差不多
# twoSum1中设置了一个Tag，找到目标后就直接跳出循环，稍微快了一点点。

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        target_list = []
        TAG = False
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    target_list.append(i)
                    target_list.append(j)
                    TAG = True
                    break
            if TAG == True:
                break
                
        return target_list
        
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j]:
                    result.append(i)
                    result.append(j)
        return result