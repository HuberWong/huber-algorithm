from typing import Optional, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 构建滑动窗口, 注意数组和 k 的大小关系
        left, right = 0, min(k + 1, len(nums))
        # 使用 set 存储滑动窗口, 以判断是否存在重复值
        visited = set(nums[left: right])
        # 数组长度小于 k 的情况
        if len(visited) < right - left:
            return True
        # 数组长度大于等与 k 的情况
        while right < len(nums):
            visited.remove(nums[left])
            left += 1
            visited.add(nums[right])
            right += 1
            if len(visited) <= k:
                return True
        return False


if __name__ == '__main__':
    a = Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)

    print(a)
