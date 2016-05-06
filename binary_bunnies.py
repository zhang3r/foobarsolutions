'''
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''
from math import factorial as f

def nCr(n,r):
    return f(n) / f(r) / f(n-r)

class node():
	def __init__(self, val):
		self.val = val
		self.left=None
		self.right=None

	def add(self,node):
		if self.val > node.val:
			if self.left is None:
				self.left = node
			else:
				self.left.add(node)
		else:
			if self.right is None:
				self.right =node
			else:
				self.right.add(node)
	def get_count(self):
		count =1
		pairs =0
		total =0
		if self.left is not None and self.right is not None:
			l_count, l_pairs, l_total= self.left.get_count()
			r_count, r_pairs, r_total= self.right.get_count()
			pairs += 2 + l_pairs+r_pairs
			l_pairs = 1 if l_pairs <= 0 else l_pairs
			r_pairs = 1 if r_pairs <= 0 else r_pairs
			
			total = nCr((l_count + r_count), r_count) * l_pairs * r_pairs
			count+=l_count+r_count
		elif self.left is not None:
			m_count, m_pairs, m_total = self.left.get_count()
			count += m_count
			pairs += m_pairs
			total +=m_total
		elif self.right is not None:
			m_count, m_pairs, m_total= self.right.get_count()
			count += m_count
			pairs += m_pairs
			total +=m_total

		else:
			total+=1
		
		return (count, pairs, total)


def answer(seq):
	#build tree
	if len(seq) < 1:
		return "0"
	total= 1
	tree = node(seq[0])
	for x in seq[1:]:
		tree.add(node(x))
	count, pairs, total = tree.get_count()
	return str(int(total))


# [5,2,3,1,8]
# 8
seq = [8,7,6,5,4,3,2]
print(answer(seq))