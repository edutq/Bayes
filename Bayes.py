import itertools
import copy

class Node:

	def __init__(self, name, children, parent, table):
		self.name = name
		self.children = children
		self.parent = parent
		self.table = table

	def __repr__(self):
		return "Node:\n\tName: %s \n\tChildren: %s \n\tParents: %s \n\tTable: %s\n" % (self.name, self.children, self.parent, self.table)

def create_nodes(nodes_string):
	nodes_list = []
	for var in nodes_string.split(','):
		nodes_list.append(Node(var, None, None, None))

	return nodes_list

def bayes(nodes, probabilities, queries):
	nodes_list = create_nodes(nodes)
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
