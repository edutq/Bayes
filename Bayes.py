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
	
	def addTable(self, probabilities_list):
		#get keys from probability list
		for key in probabilities_list.keys():
			#remove signs from string
			key = key.replace("+", "")
			key = key.replace("-", "")

			#split by pipe if it appears
			var = key.split('|')

			#check if the first position is equal to the nodes name
			if self.name == var[0]:
				self.table[key] = probabilities_list[key]
		return table

	def getParents(self):
		return self.parents

	def addParent(self, dictionary):

		#get keys from dictionary
		for k in dictionary.keys():
			#replace '+' and '-' sings from string
			k = k.replace("+", "")
			k = k.replace("-", "")
			#split query by the weird stick
			var = k.split('|')
			
			#check if this is the node to add the parents
			if self.name == var[0]:
				#check for parents in the condition
				if len(var) == 2:
					#get all the parents in the condition by spliting by comma
					for parent in var[1].split(","):
						#check if the parent is on the list 
						#don't repeat parents
						if not parent in self.parents:
							self.parents.append(parent)
				#set it as a root node
				elif len(var) == 1:
					#set parents as None since won't have any parents because is root node
					if self.name == var[0]:
						self.parents = None

def set_parents(node_list, probabilities_list):
	for element in node_list:
		element.addParent(probabilities_list)

def create_nodes(nodes_string):
	nodes_list = []
	for var in nodes_string.split(','):
		nodes_list.append(Node(var, [], {}))

	return nodes_list

def parse_probabilities(probabilities_list):
	statement_list = {}
	for statement in probabilities_list:
		variables = statement.split('=')

		statement_list[variables[0]] = float(variables[1])
		
	return 	statement_list

def bayes(nodes, probabilities, queries):
	nodes_list = create_nodes(nodes)
	print(nodes_list)
	probabilities_list = parse_probabilities(probabilities)
	print(probabilities_list)
	set_parents(nodes_list, probabilities_list)
	print()
	print()
	print(nodes_list)
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
