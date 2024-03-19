# UCF Online HSPT 2024-25: Gravitational Paradox
# Solution by Samarth Upadhya

# unfinished

"""
Solution:


Time Complexity: O(log(n))
Space Complexity: O(1)
"""

from math import sqrt, hypot, atan, sin, pi

# find the area of a segment of a circle intersection
def segment_area(radius, theta):
    return radius * radius / 2 * (theta - sin(theta))

# read the input
d, p = map(float, input().split())

# setup the radius and the total area of the earth
r = d / 2
total_area = pi * r * r

# binary search for the tether length
lo, hi, ans = 0, d, 0
for _ in range(100):
    ans = lo + (hi - lo) / 2

    if ans > d:
        hi = ans
        continue

    x = (ans*ans)/(2*r)
    y = sqrt(ans*ans - x*x)

    theta = 2 * atan(y / x)
    area = segment_area(ans, theta)

    dx = abs(r - x)
    theta = 2 * atan(y / dx)
    if r < x: theta = 2*pi - theta
    
    area += segment_area(ans, theta)

    ratio = area / total_area

    if ratio < p: lo = ans
    else: hi = ans

print(ans)
