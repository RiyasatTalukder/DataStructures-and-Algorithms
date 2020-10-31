class Heap:
    items = [-1] #placeholder for the 0th index as we will be working with >= 1 index
    root = 1

    def add(self, x):
        self.items.append(x)
        self.maxHeapify(self.items, self.root, len(self.items))
    
    def getMax(self):
        return self.items[1]
    #min for min heap
    def extractMax(self):
        pass
    def heapSort(self):
        temp = 0
        for i in range(len(self.items)//2, 0, -1):
            self.maxHeapify(self.items, i, len(self.items))
        
        for i in range(len(self.items)-1, 1, -1):
            temp = self.items[1]
            self.items[1] = self.items[i]
            self.items[i] = temp
            self.maxHeapify(self.items, 1, i)

    def maxHeapify(self, L, i, n):
        #[4,1,3,2,16,9,10,14,8,7] -> [16,14,10,8,7,9,3,2,4,1]
        left_child = 2*(i)
        right_child = 2*(i)+1
        if left_child < n and L[left_child] > L[i]:
            index_largest = left_child
        else:
            index_largest = i

        if right_child < n and L[right_child] > L[index_largest]:
            index_largest = right_child
        if(index_largest != i):
            temp = L[i]
            L[i] = L[index_largest]
            L[index_largest] = temp
            self.maxHeapify(L, index_largest, n)
    




       
       

