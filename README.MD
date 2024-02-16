## To contribute
Fork the repository (fork button should be somewhere around top row)

This creates a copy of this repository owned by you

Clone the copy of the repository (the fork)

Make changes locally

Push the changes to your fork

Once you're done with all changes go to your fork in github and press "Compare & Pull request"

This makes a request to add your changes to the original repository

## To run
Make sure that AVLTree and AVLNode are imported correctly into each file

### graph_tree.py
Draws graph representation of tree.

Install necessary packages
```
pip install networkx
pip install matplotlib
```

Import the package with

```python
from graph_tree import draw_binary_tree
```

And if your tree is named `tree`, draw it with

```python
draw_binary_tree( tree.get_root() )
```

### tests.py

You can import the tests with
```python
from tests import tests
```
All methods are static so you can simply run whichever function you want

### UnitTestAVLTree.py

Import with

```python
from UnitTestAVLTree import TestAVLTree
```