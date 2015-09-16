class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums: return ranges
        start, end = 0, 0
        while end < len(nums):
            r = str(nums[start])
            while end < len(nums) and nums[end] == nums[start] + end - start:
                end += 1
            while end < len(nums) and nums[start] == nums[end]:
                start += 1
                end += 1

            if start + 1 == end:
                ranges.append(r)
            else:
                ranges.append(r+'->'+str(nums[end-1]))
            start = end
        return ranges

    def test(self):
        list1 = [0,1,2,4,5,7]
        print self.summaryRanges(list1)
        list2 = [1]
        print self.summaryRanges(list2)
        list3 = [1,3,5]
        print self.summaryRanges(list3)
        list4 = [2,2,2,2]
        print self.summaryRanges(list4)

s = Solution()
s.test()
