"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.

Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1
"""

# def answer(food, grid):
# 	min_food= -1
# 	start = (0,0, food)
# 	size = len(grid)
# 	end = (size-1, size-1)
# 	queue = [start]
# 	while len(queue) > 0:
# 		x, y, food_left = queue.pop(0)
# 		food_left -= grid[x][y]
# 		if food_left < 0:
# 			continue

# 		if (x, y) == end:

# 			min_food = food_left if 0 <= food_left < min_food or -1 == min_food else min_food
# 		elif food_left > 0:
# 			#get neighbors
# 			if x+1 < size:
# 				queue.append((x+1, y, food_left))
# 			if y+1 <size:
# 				queue.append((x, y+1, food_left))


# 	return min_food

from heapq import heappush
from heapq import heappop
# def answer(food, grid):
# 	min_food= -1
# 	start = (0,0, food)
# 	size = len(grid)
# 	end = (size-1, size-1)
# 	queue = [(food, start)]
# 	while len(queue) > 0:
# 		priority, value = heappop(queue)
# 		x, y, food_left = value
# 		food_left -= grid[x][y]
# 		if (x, y) == end:
# 			min_food = food_left if 0 <= food_left < min_food or (min_food == -1 and food_left >=0) else min_food
# 			return min_food
# 		elif food_left > 0:
# 			#get neighbors
# 			if x+1 < size and food_left-grid[x+1][y] >=0:
# 				heappush(queue,(food_left-grid[x+1][y],(x+1, y, food_left)))
# 			if y+1 <size and food_left-grid[x][y+1] >=0:
# 				heappush(queue,(food_left-grid[x][y+1],(x, y+1, food_left)))
# 	return min_food


#  1  function Dijkstra(Graph, source):
#  2
#  3      create vertex set Q
#  4
#  5      for each vertex v in Graph:             // Initialization
#  6          dist[v] ← INFINITY                  // Unknown distance from source to v
#  7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
#  8          add v to Q                          // All nodes initially in Q (unvisited nodes)
#  9
# 10      dist[source] ← 0                        // Distance from source to source
# 11      
# 12      while Q is not empty:
# 13          u ← vertex in Q with min dist[u]    // Source node will be selected first
# 14          remove u from Q 
# 15          
# 16          for each neighbor v of u:           // where v is still in Q.
# 17              alt ← dist[u] + length(u, v)
# 18              if alt < dist[v]:               // A shorter path to v has been found
# 19                  dist[v] ← alt 
# 20                  prev[v] ← u 
# 21
# 22      return dist[], prev[]

# def answer(food, grid):
# 	min_food= -1
# 	start = (0,0)
# 	size = len(grid)
# 	end = (size-1, size-1)
# 	queue = [(-food, start)]
# 	while len(queue) > 0:
# 		food, value = heappop(queue)
# 		x, y = value
# 		if x+1 < size and food_left-grid[x+1][y] >=0:
# 			heappush(queue,(food_left-grid[x+1][y],(x+1, y, food_left)))
# 		if y+1 <size and food_left-grid[x][y+1] >=0:
# 			heappush(queue,(food_left-grid[x][y+1],(x, y+1, food_left)))
def answer(food, grid):
    n = len(grid)
    a_grid = [[set() for i in range(n)] for j in range(n)]
    a_grid[0][0] = {grid[0][0]}
  
    for row, x_val in enumerate(grid):
        for col, y_val in enumerate(x_val):
            if row != 0:
                a_grid[row][col] |= {y_val + x for x in a_grid[row-1][col] if (y_val + x) <= food}
            if col != 0:
            	a_grid[row][col] |= {y_val + x for x in a_grid[row][col-1] if (y_val + x) <= food}
    ans_arr = sorted(a_grid[n-1][n-1], reverse=True)
    
    for food_left in ans_arr:
        if food_left <= food:
            return food-food_left
    return -1


food = 13
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
print(answer(food, grid))