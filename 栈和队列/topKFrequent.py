#https://leetcode-cn.com/problems/top-k-frequent-elements/
import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        #统计元素出现频率
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        print(map_)

        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆

        #用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
            print(pri_que)

        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒叙来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

a = Solution()
a.topKFrequent([1,1,1,1,2,2,2,3,3,4,6,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8], 3)