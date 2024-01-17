class max_heap:
    def __init__(self):
        self.array = []
        self.size = 0
    def insert(self, key,value):
        self.array.append((key,value))
        self.size+=1
        self.sift_up(self.size-1)
    def sift_up(self, index):
        if self.size <=1:
            return
        current = index
        while self.parent_key(current) < self.key(current):
            self.swap(self.parent_index(current),current)
            current = self.parent_index(current)
    def parent_key(self, index):
        key,_ =  self.array[self.parent_index(index)]
        return key
    def right_key(self,index):
        if self.right_index(index) > self.size - 1:
            return float('-inf')
        key,_ =  self.array[self.right_index(index)]
        return key
    def left_key(self,index):
        if self.left_index(index) > self.size - 1:
            return float('-inf')
        key,_ =  self.array[self.left_index(index)]
        return key
    def left_index(self,index):
        return 2*(index+1)-1
    def right_index(self,index):
        return self.left_index(index)+1
    def parent_index(self,index):
        if index == 0:
            return 0
        return int((index+1)/2)-1
    def swap(self,index1,index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp
    def key(self,index):
        key,_ =  self.array[index]
        return key
    def extract_max(self):
        max = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.sift_down(0)
        self.size-=1
        return max
    def sift_down(self,index):
        if self.size <=1:
            return
        current = index
        while max(self.left_key(current),self.right_key(current)) > self.key(current):
            if self.left_key(current) >= self.right_key(current):
                self.swap(self.left_index(current),current)
                current = self.left_index(current)
            else:
                self.swap(self.right_index(current),current)
                current = self.right_index(current)
    def get_elements(self):
        return self.array[:self.size]
    def heapify(self,elements):
        self.array = elements
        self.size = len(elements)
        for index,_ in enumerate(self.array[:int(self.size/2)]):
            self.sift_down(index)
        return self
    
def heap_sort(elements):
    heap = max_heap()
    heap.heapify(elements)
    for _ in range(len(elements)):
        yield heap.extract_max()
    

def test_max_heap_insert():
    h = max_heap()
    h.insert(2,"a")
    h.insert(4,"b")
    assert h.get_elements() == [(4,'b'),(2,'a')]
    h.insert(3,"c")
    assert h.get_elements() == [(4,'b'),(2,'a'),(3,'c')]

def test_max_heap_extract_max():
    h = max_heap()
    h.insert(2,"a")
    h.insert(4,"b")
    h.insert(3,"c")
    h.insert(5,"d")
    h.insert(1,"e")
    assert h.extract_max() == (5,'d')
    assert h.get_elements()[0] == (4,'b')

def test_heap_sort():
    assert list(heap_sort([(5,"d"),(2,"a"),(4,"b"),(3,"c"),(1,"e")])) == [(5,"d"),(4,"b"),(3,"c"),(2,"a"),(1,"e")]

test_max_heap_insert()
test_max_heap_extract_max()
test_heap_sort()
