class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
        
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
            
if __name__ == '__main__':

    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)
    
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))
    
    for ch in root.depth_first():
        print(ch)