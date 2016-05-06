'''
Zombit monitoring
=================

The first successfully created zombit specimen, Dolly the Zombit, needs constant monitoring, and Professor Boolean has tasked the minions with it. Any minion who monitors the zombit records the start and end times of their shifts. However, those minions, they are a bit disorganized: there may be times when multiple minions are monitoring the zombit, and times when there are none!

That's fine, Professor Boolean thinks, one can always hire more minions... Besides, Professor Boolean can at least figure out the total amount of time that Dolly the Zombit was monitored. He has entrusted you, another one of his trusty minions, to do just that. Are you up to the task?

Write a function answer(intervals) that takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the zombit. All values will be positive integers no greater than 2^30 - 1. You will always have end > start for each interval.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) intervals = [[1, 3], [3, 6]]
Output:
    (int) 5

Inputs:
    (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
Output:
    (int) 16

solution
first pair

second pair
[1,2] + [2,3] = [1,3]
[2,4]+[1,3] = [1,4]
[1,4]+[2,3] =[1,4]
[1,2]+[3,4] = [1,2],[3,4] =2 time units
'''
def answer(intervals):
	intervals=sorted(intervals)
	time=0
	lower_bound=0
	upper_bound=0
	for interval in intervals:

		l, u = interval
		if l > upper_bound:
			time+= upper_bound- lower_bound
			lower_bound=l
			upper_bound=u
		elif u > upper_bound:
			upper_bound = u

	time+= upper_bound- lower_bound
	return time

print(answer([[2, 4], [0, 3]]))