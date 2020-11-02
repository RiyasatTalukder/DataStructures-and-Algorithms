class Heap:
    '''
    The following is a Max-Heap implementation with the standard methods.
    The code assumes that the user follows a 1-based indexing instead of the standard
    -1 is used as an error code as well as a placeholder value
    '''

    items = [-1] #placeholder for the 0th index as we will be working with >= 1 index
    root = 1

    #O(lgn)
    def add(self, x):
        self.items.append(-1)
        self.increaseKey(len(self.items)-1, x)
    #O(1)
    def getMax(self):
        return self.items[1]
    
    #O(lgn)
    def extractMax(self):
        if len(self.items) < 1:
            return -1
        maximum = self.items[1]
        self.items[1] = self.items[len(self.items)-1]
        self.items.pop() 
        self.maxHeapify(self.items,1,len(self.items))
        return maximum
    
    #O(lgn)
    def increaseKey(self, i, value):
        if(value < self.items[i]):
            return -1
        self.items[i] = value
        parent = i//2
        while (i > 1 and self.items[parent] < self.items[i]):
            temp = self.items[i]
            self.items[i] = self.items[parent]
            self.items[parent] = temp
            i = parent
            parent = i//2
    
    #O(nlgn)
    def heapSort(self):
        temp = 0
        #For our case, self.items is always a heap so we do not require to rehepify
        #However, for a general array, we would first need to hepify using the following code
        """
        for i in range(len(self.items)//2, 0, -1):
            self.maxHeapify(self.items, i, len(self.items))
        """
        for i in range(len(self.items)-1, 1, -1):
            temp = self.items[self.root]
            self.items[self.root] = self.items[i]
            self.items[i] = temp
            self.maxHeapify(self.items, self.root, i)
    
    #O(lgn)
    def maxHeapify(self, L, i, n):
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
    
    def getHeap(self):
        return self.items[1:]
               

