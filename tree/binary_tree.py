from curses import noecho
import queue
from requests import delete


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, node, key):
        if node is None or node.data == key:
            return node is not None
        elif key < node.data:
            return self._find_value(node.left, key)
        else:
            return self._find_value(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                if child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else :
            node.right, deleted = self._delete_value(node.right, key)

        return node, deleted

    def DfsPreOrder(self):
        def _DFS(node):
            if node is None:
                pass
            else:
                print(node.data, end=' ')
                _DFS(node.left)
                _DFS(node.right)
        _DFS(self.root)

    def DfsInOrder(self):
        def _DFS(node):
            if node is None:
                pass
            else:
                _DFS(node.left)
                print(node.data, end=' ')
                _DFS(node.right)
        _DFS(self.root)

    def DfsPostOrder(self):
        def _DFS(node):
            if node is None:
                pass
            else:
                _DFS(node.left)
                _DFS(node.right)
                print(node.data, end=' ')
        _DFS(self.root)
    
    def Bfs(self):
        def _BFS(node):
            queue = [node]
            while queue:
                node = queue.pop(0)
                if node is not None:
                    print(node.data, end = ' ')
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        _BFS(self.root)
    

if __name__ == '__main__':
    data = [20,6,8,12,78,32,65,32,7,9]
    tree = BinarySearchTree()

    for d in data:
        tree.insert(d)

    print(tree.find(9))
    print(tree.find(3))
    print(tree.delete(78))
    print(tree.delete(6))
    print(tree.delete(11))
    print('='*30)
    print('='*30)
    tree.DfsPreOrder()
    print('\n')
    tree.DfsInOrder()
    print('\n')
    tree.DfsPostOrder()
    print('\n')
    tree.Bfs()
