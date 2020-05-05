objs = []
reqs = []

def solve(objs, reqs):
    root = []
    for i in range(len(reqs)):
        if not reqs[i]:
            root.append(objs[i])
    if not root:
        print("Your requirements are cyclical")
        return []
    return [root] + subtree([root], objs, reqs)

def subtree(tree, objs, reqs):
    node = []
    for i in range(len(reqs)):
        if usable(tree, reqs[i]):
            node.append(objs[i])
    return [node] + subtree(tree + [node], objs, reqs)

def usable(tree, req):
    for r in req:
        found = False
        for node in tree:
            if r in node:
                found = True
        if not found:
            return False
    return True
