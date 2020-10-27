class Heap:
    items = []
    root = 1

    def add(self, x):
        self.items.append(x)
        self.maxHeapify(self.items, self.root, len(self.items))
    
    def getMax(self):
        pass
    #min for min heap
    def extractMax(self):
        pass
    def heapSort(self):
        A = [4,1,3,2,16,9,10,14,8,7]
        temp = 0
        for i in range(len(self.items)//2, 1, -1):
            self.maxHeapify(self.items, i, len(self.items))
        
        for i in range(len(self.items), 2, -1):
            temp = self.items[0]
            self.items[0] = self.items[i]
            self.items[i] = temp
            self.maxHeapify(self.items, 1, i)

    def maxHeapify(self, L, i, n):
        #[4,1,3,2,16,9,10,14,8,7] -> [16,14,10,8,7,9,3,2,4,1]
        left_child = 2*(i)
        right_child = 2*(i)+1
        index_largest = i
        print("Initial: " + str(index_largest))
        if (left_child < n and right_child < n):
            print("left_child_index: " + str(left_child))
            print("right_child_index: " + str(right_child))
        if left_child < n and L[left_child] > L[i]:
            index_largest = left_child
        else:
            index_largest = i

        if right_child < n and L[right_child] > L[index_largest]:
            index_largest = right_child
        print("largest index: " + str(index_largest))
        if(index_largest != i):
            temp = L[i]
            L[i] = L[index_largest]
            L[index_largest] = temp
            maxHeapify(L, index_largest, n)
    




       
       

