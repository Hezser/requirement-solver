# TODO: We are not setting nodes to be children of all parents which they require, only the first parent found. To fix this, we probably need to make build_subtree non-recursive and perform within a while loop over obj not being empty

class Node:

    obj      = {}
    children = []
    # parent   = None

    def __init__(self, obj):
        self.objs = objs

    # def add_object(self, obj):
    #     self.objs.update(obj)

    def add_child(self, child):
        self.children.append(child)

    # def set_parent(self, parent):
    #     self.parent = parent

class Solver:

    def __init__(self, objs, reqs):
        self.objs = objs
        self.reqs = reqs

    def solve():
        root = Node(None)
        for (k, v) in objs.items():
            if not reqs[k]:
                # child = Node({k, v}).add_parent(root)
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
                # child = Node({k, v}).add_parent(parent)
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

