def solve(l):
    # Sort the list 
    l.sort()
    
    # Initialize result and left pointer 
    res = 0
    left = 0
    
    # Traverse the list 
    for right in range(len(l)): 
        
        # If current element is different from left element, 
        # then we can remove elements from left to (right - 1) 
        if l[right] != l[left]:
            res += right - left
            left = right
            
    # Add elements from left to end if left is not equal to end 
    res += len(l) - left
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(l))
