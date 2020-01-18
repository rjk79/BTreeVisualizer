from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
   return render_template('form.html')

@app.route('/result', methods = ['POST', 'GET'])

def result():
    result = request.form
    # print(result.items())
    for k, v in result.items():
        serialization = v
    
    serialization = v

    class TreeNode():
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def deserialize(data):
        data = iter(list(data))

        def recurse():
#           consumes the iterable
            currVal = next(data, '$')

            if currVal == "#" or currVal == "$":
                return None
            curr = TreeNode(int(currVal))
            curr.left = recurse()
            curr.right = recurse()
            return curr
        return recurse()
    # import pdb;pdb.set_trace()

    root = deserialize(serialization)
    # a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)
    # d = TreeNode(4)
    # e = TreeNode(5)
    # f = TreeNode(6)
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f
    def printTree(root):
#   m = height
#   n is odd
# map each child to a val +- rel to parent
        def getHeight(node):
            if not node: return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        height = getHeight(root)
        width = 2**height-1     #-1 after powering
        res = [[" " for _ in range(width)] for _ in range(height*2)]

        def update(node, level, left, right):
            if not node: return
            mid = (left + right) //2
            res[level][mid] = str(node.val)
            if node.left: res[level+1][mid-1] = "/"
            if node.right: res[level+1][mid+1] = "\\"
            update(node.left, level + 2, left, mid)
            update(node.right, level + 2, mid + 1, right) #mid + 1 since dont want to //(floor) to idx

        update(root, 0, 0, width)
        return res
    output = printTree(root)
    print([" ".join(line) for line in output])
    return "<pre>" + "<br/>".join(" ".join(line) for line in output) + "</pre>" + "<br/>" + serialization
