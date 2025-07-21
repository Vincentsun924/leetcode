class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Create a hashmap/dictionary instance
        output = {}

        #for loop that goes through the nums, but since we want the index we need to enumerate
        for index, i in enumerate(nums):
            #get the complement
            second = target - i
            #only run this if loop if the complement is already in the ouput, that way we know its legit and it exists
            if second in output:
                #this is what we return when we have both the index and complement
                return [output[second], index]
            
            output[i] = index
            
        return False