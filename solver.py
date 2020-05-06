# TODO: We are not setting nodes to be children of all parents which they require, only the first parent found. To fix this, we probably need to make build_subtree non-recursive and perform within a while loop over obj not being empty
# TODO: Different approach - Initially, create all nodes, and then create edges based on requirements. However, this does not allow for dynamic checks of cycles etc.

class Node:

    obj      = {}
    children = []

    def __init__(self, obj):
        self.objs = objs

    def add_child(self, child):
        self.children.append(child)

class Solver:

    def __init__(self, objs, reqs):
        self.objs = objs
        self.reqs = reqs

    def solve():
        root = Node(None)
        for (k, v) in objs.items():
            if not reqs[k]:
                root.add_child(Node({k, v}))
                del objs[k]
        if not root.children:
            print("Your requirements are cyclical")
            return None
        for child in root.children:
            build_subtree(child, root)
        return root

    def build_subtree(parent, root):
        if not objs:
            return
        for (k, v) in objs.items():
            if usable(parent, reqs[k]):
                parent.add_child(Node({k, v}))
                del objs[k]
        for child in parent.children:
            build_subtree(child)

    def usable(node, req, root):
        for obj in req:
            if not find(obj, root):
                return False
        return True

    def find(req, root):
        if not root.children:
            return False
        if obj in root.obj:
            return True
        for child in root.children:
            if find(req, child):
                return True
        return False

