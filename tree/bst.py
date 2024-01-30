class BST_Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if value <= self.value:
            if self.left == None:
                self.left = BST_Node(value)
                self.left.parent = self
                return self.left
            else:
                return self.left.insert(value)
        if value > self.value:
            if self.right == None:
                self.right = BST_Node(value)
                self.right.parent = self
                return self.right
            else:
                return self.right.insert(value)
    def show(self):        
        if self.left:
            self.left.show()
        print(self.value)
        if self.right:
            self.right.show()
    def in_order(self):        
        in_order = []
        if self.left:
            in_order+=self.left.in_order()
        in_order+=[self.value]
        if self.right:
            in_order+=self.right.in_order()
        return in_order
    def get_count(self):
        count = 0
        if self.left:
            count+=self.left.get_count()
        if self.right:
            count+=self.right.get_count()
        return count+1
    def is_in_tree(self,value):
        if self.value == value:
            return True
        if self.left and value <= self.value:
            return self.left.is_in_tree(value)
        if self.right and value > self.value:
            return self.right.is_in_tree(value)
        return False
    def get_hight(self):
        left_hight = 0
        right_hight = 0
        if self.left:
            left_hight = self.left.get_hight()
        if self.right:
            right_hight = self.right.get_hight()
        return max(left_hight,right_hight) + 1
    def get_min(self):
        if self.left:
            return self.left.get_min()
        return self.value
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value
    def is_bst(self):
        if self.left and self.left.value <= self.value :
            if not self.left.is_bst():
                return False
        if self.right and self.right.value > self.value :
            if not self.right.is_bst():
                return False
        return True
    def delete(self, value):
        if self.value == value:
            successor,parent = self.find_successor()
            if successor == None:
                self.value = None
            else:
                if successor == self.left:
                    self.value = successor.value
                    self.left = successor.left
                    self.right = successor.right
                elif successor == self.right:
                    self.value = successor.value
                    self.right =  successor.right    
                else:
                    self.value = successor.value
                    parent.left = None
                    successor.value = None
            return
        if self.left and value <= self.value:
            self.left.delete(value)
        if self.right and value > self.value:
            self.right.delete(value)

    def find_successor(self):
        if not self.right and not self.left:
            return None,self
        if self.right:
            successor = self.right
            while successor.left is not None :
                parent = successor
                successor = successor.left
            return successor,parent
        return self.left,self
    def get_node(self,value):
        if self.value == value:
            return self
        if self.left and value <= self.value:
            return self.left.get_node(value)
        if self.right and value > self.value:
            return self.right.get_node(value)
        return None


def get_tree_1():
    tree = BST_Node(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(3)
    tree.insert(2)
    tree.insert(5.5)

    return tree

def main():
    tree = get_tree_1()
    tree.show()
    print(f"count : {tree.get_count()}")
    print(f"is in tree 2 : {tree.is_in_tree(2)}")
    print(f"is in tree 8 : {tree.is_in_tree(8)}")
    print(f"height : {tree.get_hight()}")
    print(f"min : {tree.get_min()}")
    print(f"max : {tree.get_max()}")
    print(f"is bst : {tree.is_bst()}")

def test_tree_delete():
    tree = get_tree_1()
    tree.delete(3)
    assert tree.in_order() == [2,4,5,5.5,6]

    tree = get_tree_1()
    tree.delete(4)
    assert tree.in_order() == [2,3,5,5.5,6]

    tree = get_tree_1()
    tree.delete(5)
    assert tree.in_order() == [2,3,4,5.5,6]

    tree = get_tree_1()
    tree.delete(6)
    assert tree.in_order() == [2,3,4,5,5.5]

test_tree_delete()
    
if __name__ == "__main__":
    main()
