from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        max_key = -1e9
        max_count = 0
        for key, count in dic.items():
            if max_count < count:
                max_count = count
                max_key = key
        return max_key
