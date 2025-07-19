#solution class that inherits from object ( a convention)
class Solution(object):
#a method that takes in 2 arguments
#self refers to the instance of the class (required)
#nums is a list of integers
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) != len(set(nums)):
        #     return True
        # else:
        #     return False

        return len(nums) != len(set(nums))

# Run test cases when file is executed directly
if __name__ == "__main__":
    #defines the instance of the solution class, we need to call solutions.containsDuplicate()
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # Output: True
    print(s.containsDuplicate([1, 2, 3, 4]))  # Output: False
    print(s.containsDuplicate([]))           # Output: False
    print(s.containsDuplicate([0, 0]))        # Output: True