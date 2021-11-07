class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeInsert(root:TreeNode, z:TreeNode):
    y = None
    x = root
    while x:
        y = x
        if z.val < x.val:
            x = x.left
        else: x = x.right
    
    if y == None: return z
    if z.val < y.val:
        y.left = z
    else: y.right = z
    return root

prev = None  
def doubleSortedFromT(x: TreeNode, prev: TreeNode):
    if x:
        prev=doubleSortedFromT(x.left, prev)
        
        x.left = prev
        if prev:
            prev.right = x
        prev = x
        prev=doubleSortedFromT(x.right, prev)
    return prev


arr = [7,14,32,65,87,43,13,24,5]
m_root = None
for i in arr:
    m_root = TreeInsert(m_root, TreeNode(i))

prev = doubleSortedFromT(m_root,prev)
# while prev:
#     print(prev.val)
#     prev = prev.left

while prev.left:
    prev = prev.left



while prev:
    print(prev.val)
    prev = prev.right



