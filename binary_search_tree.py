import timeit
import random

class BST:
    def __init__(self):
        self.empty = True
        self.left = None
        self.right = None
        self.key = None
        self.val = None

    def insert(self, new_key, new_val):
        node = self
        while not node.empty:
            if new_key <= node.key:
                node = node.left
            else:
                node = node.right
        node.key = new_key
        node.val = new_val
        node.left = BST()
        node.right = BST()
        node.empty = False

    def search(self, target):
        node = self
        while not node.empty:
            if target == node.key:
                return node.val
            elif target <= node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError(target)

    def in_order(self):
        if self.empty:
            return []
        else:
            left_items = self.left.in_order() 
            right_items = self.right.in_order()
            this_item = (self.key, self.val)
            return left_items + [this_item] + right_items

    def __getitem__(self, target):
        return self.search(target)

    def __setitem__(self, new_key, new_val):
        return self.insert(new_key, new_val)

    def __contains__(self, target):
        try:
            _result = self.search(target)
        except KeyError:
            return False
        else:
            return True

    def __bool__(self):
        return not self.empty

def test_insert_sorted(n):
    tree = BST()
    for x in range(n):
        tree.insert(x, None) 

for n in range(0, 10001, 1000):
    time = timeit.timeit("test_insert_sorted(n)", number=1, setup="from __main__ import test_insert_sorted, n")
    print(f"{n},{time}")

def test_insert_shuffled(n):
    tree = BST()
    keys = list(range(n))
    random.shuffle(keys)
    for x in keys:
        tree.insert(x, None) 

for n in range(0, 10001, 1000):
    time = timeit.timeit("test_insert_shuffled(n)", number=1, setup="from __main__ import test_insert_shuffled, n")
    print(f"{n},{time}")
