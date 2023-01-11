#1
class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class CompleteBinaryTree:
    def __init__(self):
        self.root = None

    def parent(self, i: int) :
        return (i-1)//2

    def left_child(self, i: int) :
        return 2*i + 1

    def right_child(self, i: int) :
        return 2*i + 2

    def swap_node(self, i: int, j: int):
        node1 = self._get_node(i)
        node2 = self._get_node(j)
        node1.key, node2.key = node2.key, node1.key

    def _get_node(self, i: int):
        """ Helper function to find the node of the given index."""
        node = self.root
        for _ in range(i):
            node = node.next
        return node


#2
class MinimumPriorityQueue:
    def __init__(self):
        self.heap = CompleteBinaryTree()
        self.size = 0

    def insert(self, key):
        """Insert a new element into the priority queue.

        Args:
        key: The element to insert.

        Time Complexity: O(log n)
        """
        node = Node(key)
        if self.size == 0:
            self.heap.root = node
        else:
            parent_idx = self.heap.parent(self.size)
            parent_node = self.heap._get_node(parent_idx)
            if parent_node.next:
                parent_node.next.next = node
            else:
                parent_node.next = node
        self.size += 1
        self._swim(self.size - 1)

    def del_min(self):
        """Remove and return the smallest element in the priority queue.

        Returns:
        The smallest element in the priority queue.

        Time Complexity: O(log n)
        """
        if self.size == 0:
            return None
        min_val = self.heap.root.key
        last_node = self.heap._get_node(self.size - 1)
        self.heap.root.key = last_node.key
        if last_node.next:
            last_node.next = None
        self.size -= 1
        self._sink(0)
        return min_val

    def _swim(self, i: int):
        """ Helper function to move the node up until heap property is satisfied."""
        parent_idx = self.heap.parent(i)
        if parent_idx < 0:
            return
        parent_node = self.heap._get_node(parent_idx)
        if parent_node.key > self.heap._get_node(i).key:
            self.heap.swap_node(parent_idx,i)
            self._swim(parent_idx)

    def _sink(self, i: int):
        """ Helper function to move the node down until heap property is satisfied."""
        left_child_idx = self.heap.left_child(i)
        right_child_idx = self.heap.right_child(i)
        if left_child_idx >= self.size:
            return
        if right_child_idx >= self.size:
            min_idx = left_child_idx
        else:
            left_child = self.heap._get_node(left_child_idx)
            right_child = self.heap._get_node(right_child_idx)
            if left_child.key < right_child.key:
                min_idx = left_child_idx
            else:
                min_idx = right_child_idx
        if self.heap._get_node(i).key > self.heap._get_node(min_idx).key:
            self.heap.swap_node(i, min_idx)
            self._sink(min_idx)




#4
import time
import matplotlib.pyplot as plt

def benchmark(n):
    heap = MinimumPriorityQueue()
    start_time = time.time()
    for i in range(n):
        heap.insert(i)
    end_time = time.time()
    return (end_time - start_time)

n_values = [10, 100, 1000, 10000, 100000, 1000000]
times = [benchmark(n) for n in n_values]

plt.plot(n_values, times)
plt.xlabel('Number of elements')
plt.ylabel('Time (s)')
plt.show()

#5
import graphviz

def visualize_heap(heap):
    dot = graphviz.Digraph()
    queue = [(0, heap.root)]
    while queue:
        i, node = queue.pop(0)
        dot.node(str(i), str(node.key))
        if node.next:
            queue.append((2*i+1, node.next))
            dot.edge(str(i), str(2*i+1))
        if node.next.next:
            queue.append((2*i+2, node.next.next))
            dot.edge(str(i), str(2*i+2))
    return dot
dot = visualize_heap(heap)
dot.render('heap_tree.gv', view=True)
