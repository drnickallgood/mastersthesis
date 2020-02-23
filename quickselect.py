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

    def kFindMost(self,hashes,k):
        """

        """
        # fix indexing
        #k = k+1

        # Copy hashes to new structure
        newHashes = hashes
        
        # Finding the most common hash in hashs
        if k <= 0:
            print("Error! Invalid k")
            exit(1)
        if k == 1:
            return self.findMost(newHashes)
        for i in range(k):
            if len(newHashes) == 0:
                break
            # get largest hash
            most = self.findMost(newHashes)
            # if current most occuring hash is less than our index
            # Remove from list to get the next one
            if i < k:
                newHashes[:] = (h for h in newHashes if h != most)
                    
        return most

    def findMost(self,hashes):
        """
        : type nums: string
        : type k: int - occurs the most, 2nd most
        : return type: string
        """
        counter = 0
        curr_hash = hashes[0]

        for i in hashes:
            curr_freq = hashes.count(i)
            if curr_freq > counter:
                counter = curr_freq
                curr_hash = i
                
        return curr_hash
        
        
        
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


#hashes = ["14kj", "14kj", "1a30$d", "2a9bl34ac", "14kj", "1a30$d", "nick"]
#qs = QuickSelect()
#a = [1,2,3,4,5,9,7,2,19]


#print(qs.kFindMost(hashes,1))
#print(hashes)
#print(qs.kFindMost(hashes,2))
#print(hashes)

#print(qs.kFindMost(hashes,3))
#print(qs.kFindMost(hashes,4))




