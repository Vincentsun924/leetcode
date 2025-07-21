class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #make the storage variables
        output = []
        firstseen = {}
        #we want to sort the nums so we can get the indexes that tell us how many things are before it.
        nums2 = sorted(nums)
        
#loop through and store the index and the values in key/value pair
        for index, value in enumerate(nums2):
            #we want only to keep the first instance of the value's index if there is duplicates
            if value not in firstseen:
                firstseen[value] = index

#here we are just appending the values in nums to the output list based on the order they appear.
        for num in nums:
            output.append(firstseen[num])

        return output

    