import unittest
import random
from tree import *

class TestTrees(unittest.TestCase):

    def test_tree_creation(self):
        print("\nTesting creation of a tree...")
        data = []
        root = createTree(data)
        self.assertTrue(isValidBST(root))

        data = [1]
        root = createTree(data)
        self.assertTrue(isValidBST(root))

        data = [69 for i in range(0,100)]
        root = createTree(data)
        self.assertTrue(isValidBST(root))
    
        for _ in range(300):
            data = [random.randrange(-100,100) for _ in range(0,random.randrange(0,1000))]
            root = createTree(data)
            self.assertTrue(isValidBST(root))
        
        print("Tree creation is OK!")

    def test_inorder_t(self):
        print("\nTesting inorder traversal...")
        data = [random.randrange(-100,100) for _ in range(0,random.randrange(0,1000))]
        root = createTree(data)
        self.assertEqual(inorderT(root), sorted(set(data)))
        print("In order traversal is OK!")

if __name__ == '__main__':
    print("Starting tests...")
    unittest.main()