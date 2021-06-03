class Monarchy:
    def __init__(self, head):
        self.head = Node(head)
        self.family = {}
        self.family[head] = self.head
        self.order = []

    def birth(self, child, parent):
        newChild = Node(child) 
        self.family[parent].children.append(newChild)
        self.family[child] = newChild
        pass 

    def death(self, name):
        self.family[name].alive = False 

    def getOrderOfSuccession(self):
        self.order = []
        self.dfs(self.head)
        return self.order

    def dfs(self, root):
        if root.alive:
            self.order.append(root.name)
        for c in root.children:
            self.dfs(c)

class Node:
    def __init__(self, name):
        self.name = name 
        self.children = []
        self.alive = True 
