"""
Original Source: https://github.com/aanmtn/QuickSelect/blob/master/main.py

Need to modify, needs to find desired number of frequent hash-grams
i.e hashes that occur k times or greater..

get list of hashes that occur more than k times

"""
import numpy as np

class QuickSelect:

    def __init__(self,arr,freq):
        self.arr = arr
        self.freq = freq

    def partition(self,l, r):
        x = self.arr[r]
        i = l - 1
        for j in range(l, r):
            if self.arr[j] <= x:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.arr[i + 1], self.arr[r] = self.arr[r], self.arr[i + 1]
            
        return i + 1

    def kthlargest(self,arr,k):
        l = 0
        r = len(arr) - 1
        split_point = self.partition(l, r) #choosing a pivot and saving its index
        if split_point == r - k + 1: #if the choosen pivot is the correct elemnt, then return it
            result = arr[split_point]
        elif split_point > r - k + 1: #if the element we are looking for is in the left part to the pivot then call 'kthlargest' on that part after modifing k
            result = self.kthlargest(arr[:split_point],k - (r - split_point + 1))
        else: #if the element we are looking for is in the left part to the pivot then call 'kthlargest' on that part
            result = self.kthlargest(arr[split_point + 1:r+1],k)
        return result

    def get_klargest(self,k):
        return self.kthlargest(self.arr,k)

    def topkhashes(self):
        first = self.kthlargest(self.arr,1)
        second = self.kthlargest(self.arr,2)
        third = self.kthlargest(self.arr,3)
        fourth = self.kthlargest(self.arr,4)
        
        
#just for testing
a = [1, 3, 2, 5, 7, 6, 8, 9, 4]

qs = QuickSelect(a,5)

print(qs.get_klargest(2))
#print(kthlargest(a, 4))

