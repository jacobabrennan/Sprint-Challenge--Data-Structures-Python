Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

The complexity is O(n), as the callback function must be called for each value
in the tree. Alternatively, the answer of linear complexity could be justified
as depth_first_for_each must be called for each node in the tree, and the
number of nodes in the tree is equal to the number of values.

2. What is the space complexity of your `depth_first_for_each` function?

The space complexity is O(0) (none) as no data structures or variables are
used. The function simply calls itself recursively.

3. What is the runtime complexity of your `breadth_first_for_each` method?

Like the depth_first_for_each method above, each node in the tree is iterated
over once, for a runtime complexity of O(n).

4. What is the space complexity of your `breadth_first_for_each` method?

The maximum number of items contained in the Queue is, in the worst case, the
number of items in a full final depth, which is a ((n/2)+1). This means the
space complexity is linear, or O(n).

5. What is the runtime complexity of the provided code in `names.py`?

The runtime complexity was O(n^2), as the algorithm consisted of two nested
loops, each of which iterated over an entire array. A more exact description
might be O(n*m), as the two lists could technically differ vastly in size.

6. What is the space complexity of the provided code in `names.py`?

The space complexity was O(n), as the only storage needed was the list of
duplicate names.

7. What is the runtime complexity of your optimized code in `names.py`?

The runtime complexity is O(n), where n is the total number of names. There
are no nested loops or recursion.

Edit: This fails to account for the complexity of the sort opperations, which
are O(n log(n)). This means the whole algorithm has a complexity of
O(n log(n)).

8. What is the space complexity of your optimized code in `names.py`?

The space complexity is also O(n), as all that needs to be stored are the two
original names lists, and the list of duplicates. Both lists are sorted in
place, and the only other variables declared store single indices or individual
names for comparison, and the number of these is constant.