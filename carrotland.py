"""
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover. 

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) vertices = [[2, 3], [6, 9], [10, 160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
Output:
    (int) 1730960165

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""
# too slow
# import math
# def slope(point1, point2):
# 	denominator = (point2[0]-point1[0]) if (point2[0]-point1[0]) !=0 else float("nan")
# 	return (point2[1]-point1[1])/(1.0*denominator)
# def answer(points):
# 	left = min(points, key= lambda point: point[0])
# 	right = max(points, key= lambda point: point[0])

# 	lines = [(slope(points[1], points[2]), points[1], points[2]),(slope(points[0], points[1]), points[0], points[1]),(slope(points[0], points[2]) ,points[0], points[2])]
	
# 	total_points =0

# 	for x in range(left[0], right[0]):
# 		#calculate lline down and line up
# 		upper_line=None
# 		lower_line=None
# 		for line in lines:
# 			slope_, p_1, p_2 = line
# 			if math.isnan(slope_):
# 				continue
# 			if p_2[0]>= x > p_1[0] or p_1[0]>= x > p_2[0]:
# 				y_int = p_2[1]-p_2[0]*slope_
# 				y_out =(slope_*x+y_int)
# 				if upper_line is None:
# 					upper_line = y_out
# 				elif upper_line < y_out:
# 					lower_line= upper_line
# 					upper_line=y_out
# 				else:
# 					lower_line=y_out
# 		if upper_line is not None and lower_line is not None:
# 			# print(x, upper_line, lower_line)
# 			total_points += abs(math.floor(upper_line)- math.floor(lower_line))
# 	return total_points
from fractions import gcd
import math
def distance(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	return math.sqrt((x2-x1)**2+(y2-y1)**2)
def commondenominator(point1, point2):
	x1, y1 = point1
	x2, y2 = point2
	return gcd(x2-x1, y2-y1)
def answer(points):
	# heron to caclulate area
	# 	1. find length of all 3 sides
	# 	2. s = (a+b+c)/2
	#	3. A = sqrt(s(s-a)(s-b)(s-c))
	distances = [(distance(points[1], points[2]),commondenominator(points[1], points[2]), points[1], points[2]),(distance(points[0], points[1]), commondenominator(points[0], points[1]), points[0], points[1]),(distance(points[0], points[2]) ,commondenominator(points[0], points[2]),points[0], points[2])]
	dists = [dist[0] for dist in distances]
	s = sum(dists)/2
	A = math.sqrt(s*(s-dists[0])*(s-dists[1])*(s-dists[2]))
	A=round(A, 4)
	# find the points on the perimeter
	#	1. line and mod x1+x2 % slope
	if A <=0:
		return 0
	
	perimeter_points_count =0
	perimeter_pts = [abs(dist[1]) for dist in distances]
	
	perimeter_points_count= sum(perimeter_pts)

	# use picks theorem to calculate points inside
	# 	1. A= i +b/2 -1
	#	i= points inside
	# 	b= points on perimeter
	return int(A+1-perimeter_points_count/2)
	
# vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
# vertices = [[2, 3], [6, 9], [10, 160]]
# vertices = [[-1, -1], [0, 1], [1, 0]]
vertices = [[0,0],[3,0],[0,3]]
print(answer(vertices))