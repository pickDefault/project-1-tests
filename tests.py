from avl_template import AVLTree, AVLNode

AVLNode.__repr__ = lambda self: str(self.get_key())

class tests:
    
    @staticmethod
    def testInsertDelete():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        
        # test RL rotation
        tests.insert_array(tree, keys[0:5])
        tests.assert_neighbors(tree, 7, 4, 11) 

        # test LR rotation
        tests.insert_array(keys[5:6], keys[5:6]) # insert 15
        tests.assert_neighbors(tree, 15, None, None)
        tests.assert_neighbors(tree, 23, 15, 30)
        tests.assert_neighbors(tree, 11, 7, 23)
        tests.assert_neighbors(tree, 7, 4, None)
        tests.test_root(tree, 11)
        
        # test L rotation
        tests.insert_array(tree, keys[6:8]) # insert 40, 43
        tests.assert_neighbors(tree, 40, 30, 43)
        tests.assert_neighbors(tree, 23, 15, 40)
        
        # tests R rotation
        tests.insert_array(tree, keys[8:10]) # insert 2, 1
        tests.assert_neighbors(tree, 4, 2, 7)
        tests.assert_neighbors(tree, 2, 1, None)
        tests.assert_neighbors(tree, 7, None, None)
        tests.assert_neighbors(tree, 11, 4, 23)
        tests.test_root(tree, 11)
        
        # test deletions
        tests.test_deletion(tree, 1, 0)
        tests.assert_neighbors(tree, 4, 2, 7)
        tests.assert_neighbors(tree, 2, None, None)
        tests.assert_neighbors(tree, 7, None, None)
        tests.assert_neighbors(tree, 11, 4, 23)
        tests.test_root(tree, 11)
        
        tests.test_deletion(tree, 2, 0)
        tests.assert_neighbors(tree, 4, None, 7)
        tests.assert_neighbors(tree, 7, None, None)
        tests.assert_neighbors(tree, 11, 4, 23)
        tests.test_root(tree, 11)
        
        # test L rotation
        tests.test_deletion(tree, 7, 1)
        tests.assert_neighbors(tree, 11, 4, 15)
        tests.assert_neighbors(tree, 23, 11, 40)
        tests.test_root(tree, 23)
        
        # TODO: empty the tree and test to see everything is correct
        
    @staticmethod
    def assert_neighbors(tree, node_key, left_key, right_key):
        node = tree.search(node_key)
        right_result = tree.search(right_key) if right_key != None else None
        left_result = tree.search(left_key) if left_key != None else None
        node_right = node.get_right() if node != None else None
        node_left = node.get_left() if node != None else None

        assert node_right is right_result, \
            f"Checking neighbors for {node_key}, right neighbor is {node.get_right()} but search returned something else when searching for key {right_key}"
        assert node_left is left_result, \
            f"Checking neighbors for {node_key}, left neighbor is {node.get_left()} but search returned something else when searching for key {left_key}"
        
    @staticmethod
    def insert_array(tree, key_array):
        for key in key_array:
            tree.insert(key, key)
            
    @staticmethod
    def test_deletion(tree, deletion_key, num_balancing_actions):
        deletion_node = tree.search(deletion_key)
        check_balacing_actions = tree.delete(deletion_node)

        assert tree.search(deletion_key) is None, \
            f"Deleting {deletion_key}, searching for deleted key did not return None"
        assert check_balacing_actions == num_balancing_actions, \
            f"Deleting {deletion_key}, deletion returned {check_balacing_actions} balancing actions instead of {num_balancing_actions}"
    
    @staticmethod
    def test_root(tree, root_key):
        assert tree.get_root() is tree.search(root_key), \
            f"Root is {tree.get_root()}, but search returned something else when searching for {root_key}"    
    
    @staticmethod
    def test1():
        tree=AVLTree()


        tree.insert(6,",")
        tree.insert(7,",")

        #
        # print(tree.get_root().get_key())
        tree.delete(tree.get_root())
        # print(tree.get_root().get_key())
        tree.delete(tree.get_root())
        # print(tree.get_root())
        tree.insert(6,",")
        # print(tree.get_root().get_key())
        # print(tree.get_root().get_left().get_key())
        # print(tree.get_root().get_right().get_key())