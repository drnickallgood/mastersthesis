"""
Original Source: https://github.com/aanmtn/QuickSelect/blob/master/main.py
"""

class QuickSelect:

    def __init__(self,arr):
        self.arr = arr

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
        
#just for testing
#a = [1, 3, 2, 5, 7, 6, 8, 9, 4]

#qs = QuickSelect(a)

#print(qs.get_klargest(4))
#print(kthlargest(a, 4))

