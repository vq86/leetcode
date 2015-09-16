class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return []
        results = digits[:]
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            results[i] += carry 
            if results[i] < 10: carry = 0
            else:
                carry = 1
                results[i] -= 10
            i -= 1
        else:
            if carry:
                results.insert(0, carry)
        return results

    def test(self):
        digit1 = [1,2,3,4,5]
        print self.plusOne(digit1)
        digit2 = [1,2,3,7,9,3,2]
        print self.plusOne(digit2)
        digit3 = []
        print self.plusOne(digit3)
        digit4 = [9]
        print self.plusOne(digit4)

s = Solution()
s.test()
