import itertools
import copy

class node:
	def __init__(self, name, children, parent, table):
		self.name = name
		self.children = children
		self.parent = parent
		self.table = table

def bayes(nodes, probabilities, queries):
	return 0


if __name__ == "__main__":

	nodes = input()
	numberprobabilities = int(input())
	
	probabilities = []
	for x in range(0, numberprobabilities):
		probabilities.append(input())

	numberqueries = int(input())
	queries = []

	for x in range(0, numberqueries):
		queries.append(input())

	bayes(nodes, probabilities, queries)
