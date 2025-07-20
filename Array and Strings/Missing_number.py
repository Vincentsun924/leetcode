class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
#runtime O(nlogn) because sorting and n inf ront from the for loop

#since range n starts from 1 and nums start from 0 we compare if the next thing in nums exists via indexing and if it doesnt just return the i which is one more greater than the nums index. 
        for i in range(n):
            if nums[i] != i:
                return i
        # for cases where the last number is missing and nums less than 3 in length, just returns the last would be number.
        return len(nums)

#test case
if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([0, 2]))  # Output: 1

