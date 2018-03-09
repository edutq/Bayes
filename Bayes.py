import itertools
import copy
import json

class Node:

	def __init__(self, name, parents, table):
		self.name = name
		self.parents = parents
		self.table = table

	def __repr__(self):
		return "Node:\n\tName: %s \n\tParents: %s \n\tTable: %s\n" % (self.name, self.parents, self.table)
	
	def getParents(self):
		return self.parents

	def addParent(self, parent_node):
		self.parents.append(parent_node)


def create_nodes(nodes_string):
	nodes_list = []
	for var in nodes_string.split(','):
		nodes_list.append(Node(var, [], [], None))

	return nodes_list

def parse_probabilities(probabilities_list):
	statement_list = []
	for statement in probabilities_list:
		variables = statement.split('=')

		table_row = {variables[0] : float(variables[1])}
		statement_list.append(table_row)
	return 	

def bayes(nodes, probabilities, queries):
	nodes_list = create_nodes(nodes)
	print(nodes_list)
	probabilities_list = parse_probabilities(probabilities)
	print(probabilities_list)
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
