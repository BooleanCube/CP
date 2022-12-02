from io import StringIO
import sys
 
class StringBuilder:
    _file_str = None
 
    def __init__(self):
        self._file_str = StringIO()
 
    def append(self, str):
        self._file_str.write(str)
        return self
 
    def to_string(self):
        return str(self)
 
    def __str__(self):
        return self._file_str.getvalue()
 
def update(tree, l, r, u):
    if l == r:
        tree[l] += u
        return
    if l%2 == 1:
        tree[l] += u
        l+=1
    if l == r:
        tree[l] += u
        return
    if r%2 == 0:
        tree[r] += u
        r-=1
    update(tree, l>>1, r>>1, u)
 
def point(tree, idx):
    sum = tree[idx]
    while idx > 0:
        idx >>= 1
        sum += tree[idx]
    return sum
 
n,q = map(int, sys.stdin.readline().split())
tree = [0]*(2*n)
tree[n:2*n] = list(map(int, sys.stdin.readline().split()))
r = StringBuilder()
for i in range(q):
    l = list(map(int, sys.stdin.readline().split()))
    type = l[0]
    if type == 1:
        a,b,u = l[1],l[2],l[3]
        update(tree, n+a-1, n+b-1, u)
    elif type == 2:
        idx = l[1]
        r.append(str(point(tree, n+idx-1))).append("\n")
 
sys.stdout.write(r.to_string())

