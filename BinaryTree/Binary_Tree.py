class Tree:
    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return self.value is None

    def max(self):
        if self.right.right is None:
            return self.value
        return self.right.max()

    def insert(self, data):
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
            print(f"Successfully inserted data: {data}")
            return
        if data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
            return
        elif data == self.value:
            print("Duplicate value detected.")
            return

    def delete(self, data):
        if self.isempty():
            return
        if data < self.value:
            self.left.delete(data)
        if data > self.value:
            self.right.delete(data)
        if data == self.value:
            if self.left is None and self.right is None:
                self.value = None
                return
            if self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            else:
                self.value = self.left.max()
                self.left.delete(self.left.max())
                return

    def inorder(self):
        if self.isempty():
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()

    def preorder(self):
        if self.isempty():
            return []
        return [self.value] + self.left.preorder() + self.right.preorder()

    def postorder(self):
        if self.isempty():
            return []
        return self.left.postorder() + self.right.postorder() + [self.value]

    def __str__(self):
        return f"[{", ".join(map(str, self.inorder()))}]"


binary_tree = Tree()
