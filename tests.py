from avl_template import AVLTree, AVLNode

AVLNode.__repr__ = lambda self: str(self.get_key())


class Tests:
    # These functions do the actual testing
    @staticmethod
    def test_insert_delete():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]

        # test RL rotation
        TestHelper.insert_array(tree, keys[0:5])
        TestHelper.assert_neighbors(tree, 7, 4, 11, 5)

        # test LR rotation
        TestHelper.insert_array(tree, keys[5:6])  # insert 15
        TestHelper.assert_neighbors(tree, 15, None, None, 6)
        TestHelper.assert_neighbors(tree, 23, 15, 30, 6)
        TestHelper.assert_neighbors(tree, 11, 7, 23, 6)
        TestHelper.assert_neighbors(tree, 7, 4, None, 6)
        TestHelper.test_root(tree, 11)

        # test L rotation
        TestHelper.insert_array(tree, keys[6:8])  # insert 40, 43
        TestHelper.assert_neighbors(tree, 40, 30, 43, 8)
        TestHelper.assert_neighbors(tree, 23, 15, 40, 8)

        # testHelper R rotation
        TestHelper.insert_array(tree, keys[8:10])  # insert 2, 1
        TestHelper.assert_neighbors(tree, 4, 2, 7, 10)
        TestHelper.assert_neighbors(tree, 2, 1, None, 10)
        TestHelper.assert_neighbors(tree, 7, None, None, 10)
        TestHelper.assert_neighbors(tree, 11, 4, 23, 10)
        TestHelper.test_root(tree, 11)

        # test deletions
        TestHelper.test_deletion(tree, 1, 2)
        TestHelper.assert_neighbors(tree, 4, 2, 7, 9)
        TestHelper.assert_neighbors(tree, 2, None, None, 9)
        TestHelper.assert_neighbors(tree, 7, None, None, 9)
        TestHelper.assert_neighbors(tree, 11, 4, 23, 9)
        TestHelper.test_root(tree, 11)

        TestHelper.test_deletion(tree, 2, 0)
        TestHelper.assert_neighbors(tree, 4, None, 7, 8)
        TestHelper.assert_neighbors(tree, 7, None, None, 8)
        TestHelper.assert_neighbors(tree, 11, 4, 23, 8)
        TestHelper.test_root(tree, 11)

        # test L rotation
        TestHelper.test_deletion(tree, 7, 2)
        TestHelper.assert_neighbors(tree, 11, 4, 15, 7)
        TestHelper.assert_neighbors(tree, 23, 11, 40, 7)
        TestHelper.test_root(tree, 23)

        # TODO: empty the tree and test to see everything is correct

    @staticmethod
    def test_avl_to_array():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        TestHelper.insert_array(tree, keys)

        TestHelper.test_avl2array(tree, keys)


class TestHelper:
    # Helper functions for tests class. No need to use any of them.
    @staticmethod
    def assert_neighbors(tree, node_key, left_key, right_key, size):
        node = tree.search(node_key)
        right_result = tree.search(right_key) if right_key is not None else None
        left_result = tree.search(left_key) if left_key is not None else None
        node_right = node.get_right() if node is not None else None
        node_left = node.get_left() if node is not None else None

        if right_key is None:
            node_right = node_right.get_key()
        if left_key is None:
            node_left = node_left.get_key()

        assert node_right is right_result, (
            f"Checking neighbors for {node_key}, right neighbor is {node.get_right()} but search returned something "
            f"else when searching for key {right_key}"
        )

        assert node_left is left_result, (
            f"Checking neighbors for {node_key}, left neighbor is {node.get_left()} but search returned something else "
            f"when searching for key {left_key}"
        )
        assert tree.size() == size, f"size error"

    @staticmethod
    def insert_array(tree, key_array):
        for key in key_array:
            tree.insert(key, key)

    @staticmethod
    def test_deletion(tree, deletion_key, num_balancing_actions):
        deletion_node = tree.search(deletion_key)
        check_balancing_actions = tree.delete(deletion_node)

        assert (
                tree.search(deletion_key) is None
        ), f"Deleting {deletion_key}, searching for deleted key did not return None"
        assert (
                check_balancing_actions == num_balancing_actions
        ), f"Deleting {deletion_key}, deletion returned {check_balancing_actions} balancing actions instead of {num_balancing_actions}"

    @staticmethod
    def test_root(tree, root_key):
        assert tree.get_root() is tree.search(
            root_key
        ), f"Root is {tree.get_root()}, but search returned something else when searching for {root_key}"


    @staticmethod
    def test_avl2array(tree, tree_keys_array):
        """
        :param tree: tree to test
        :param tree_keys_array: Array with all keys present in the tree
        """
        expected_array = [
            (key, key) for key in sorted(tree_keys_array)
        ]  # tests.insert_array uses the key as a value, so we do the same here
        avl_to_array_result = tree.avl_to_array()

        assert (
                expected_array == avl_to_array_result
        ), f"Expected avl_to_array() to return \n{expected_array}\nbut got\n{avl_to_array_result}"
