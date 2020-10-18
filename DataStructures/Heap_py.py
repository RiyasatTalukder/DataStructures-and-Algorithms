class Heap:
    items = []
    root = 1

    def add(self, x):
        self.items.append(x)
        self.maxHeapify(self.items, self.root, len(self.items))

    def heapSort(self):
        return 0

    def maxHeapify(self, L, i, n):
        left_child = 2*i
        right_child = 2*i+1
        index_largest = i-1
        if left_child < n and L[left_child] > L[i]:
            index_largest = left_child
        else:
            index_largest = i

        if right_child < n and L[right_child] > L[i]:
            index_largest = right_child
        
        if(index_largest != i):
            temp = L[i]
            L[i] = L[index_largest]
            L[index_largest] = temp
            self.maxHeapify(L, index_largest, n)
        
        return 0



       
       

