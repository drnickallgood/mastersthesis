"""
Needs to find desired number of frequent hash-grams
i.e hashes that occur k times or greater..

get list of hashes that occur more than k times

"""
"""
Original Source: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/190483/quickselect-algorithm-in-java-and-python
"""
import random

class QuickSelect:

    # Finds k largest from list based on k
    # 1 = Largest
    # len(nums) = smallest
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums,0,len(nums)-1,k-1)
        
    def quickSelect(self,nums,start,end,k):
        if start == end:
            return nums[start]
        
        pivot_point = self.give_pivot(start,end)
        pivot_index = self.partitian(nums,start,end,pivot_point)
        
        if pivot_index == k:
            return nums[k]
        elif k < pivot_index:
            return self.quickSelect(nums,start,pivot_index-1,k)
        else: 
            return self.quickSelect(nums,pivot_index+1,end,k)
    
    def partitian(self,nums,start,end,pivot):
        pivot_val = nums[pivot]
        nums[pivot],nums[end] = nums[end],nums[pivot]
        i = start - 1
        for j in range(start,end):
            if nums[j] > pivot_val:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            
        nums[i+1],nums[end] = nums[end],nums[i+1]
        return i+1
    
    def give_pivot(self,start,end):
        return random.randint(start,end)


qs = QuickSelect()
a = [1,2,3,4,5,9,7,2,19]

print(qs.findKthLargest(a,1))



