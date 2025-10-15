"""

We are given an array of n s in the plane, and the problem is to find out the closest pair of s in the array. This problem arises in a number of applications. For example, in air-traffic control, you may want to monitor planes that come too close together, since this may indicate a possible collision. Recall the following formula for distance between two s p and q.
∥pq∥=(px​−qx​)2+(py​−qy​)2​

"""
import math

import matplotlib.pyplot as plt

coords = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# coords = [(0, 0), (0, 5), (10, 0), (11, .5), (20, 20)]

# Extract coordinates
x_coords = [coord[0] for coord in coords]
y_coords = [coord[1] for coord in coords]

# Create the plot
plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, color='blue')

# Annotate each 
for (x, y) in coords:
    lbl = f'({x}, {y})'
    plt.text(x + 0.3, y + 0.3, lbl, fontsize=12)

# Styling
plt.grid(True)
plt.title(" Closest Pair")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

"""

find close by x
find close by y

* sort by x axis
* find closest in x axis
    * find closest in left 
    * find closest in right
    * find closest in mid
    
     

"""


# Find closest pair in strip area
def strip_closest(strip, d):
    min_dist = d
    pair = None
    strip.sort(key=lambda p: p[1])  # Sort by y-coordinate
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):  # Check next up to 6 points
            dist = math.dist(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])
    return min_dist, pair


def cal_dist(x, y):
    return math.dist(x, y)


min = math.inf


def recur_helper(co_ords):
    n = len(co_ords)

    # base case
    if len(co_ords) < 3:
        print("co ords", co_ords)
        dist = math.dist(co_ords[0], co_ords[1])
        return co_ords, dist

    mid = n // 2
    # divide
    left = co_ords[:mid]
    right = co_ords[mid:]

    # conquer
    dist_l, cls_pair_l = recur_helper(left)
    dist_r, cls_pair_r = recur_helper(right)

    # combine - Get best result from left/right
    if dist_l < dist_r:
        d_min = dist_l
        best_pair = cls_pair_l
    else:
        d_min = dist_r
        best_pair = cls_pair_r

    # Step 2: build a "strip" of points close to the dividing line
    mid_point = co_ords[mid]
    strip = [p for p in co_ords if abs(p[0] - mid_point[0]) < d_min]
    # Check strip for closer pair

    d_strip, pair_strip = strip_closest(strip, d_min)
    if d_strip < d_min:
        return d_strip, pair_strip
    else:
        return d_min, best_pair


def find_closest(co_ords):
    closest_pair = None
    sort_by_x = sorted(co_ords, key=lambda x: x[0])
    return recur_helper(sort_by_x)


print(find_closest(coords))
