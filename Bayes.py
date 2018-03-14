import itertools
import copy
import json
import decimal

class Node:

	def __init__(self, name, parents, table):
		self.name = name
		self.parents = parents
		self.table = table

	def __repr__(self):
		return "Node:\n\tName: %s \n\tParents: %s \n\tTable: %s\n" % (self.name, self.parents, self.table)

	def getParents(self):
		return self.parents

	def addParentandTable(self, dictionary):

		#get keys from dictionary
		for k in dictionary.keys():
			#replace '+' and '-' sings from string
			key = copy.deepcopy(k);
			k = k.replace("+", "")
			k = k.replace("-", "")
			#split query by the weird stick
			var = k.split('|')
			
			#check if this is the node to add the parents
			if self.name == var[0]:
				#add table value
				self.table[key] = dictionary[key]
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

	def completeTable(self):
		key = None
		auxdictionary = copy.deepcopy(self.table)
		for k in self.table:
			if k[0] == "+":
				key = k.replace("+", "-", 1)

				if not key in self.table:

					auxdictionary[key] = round(1.0 - self.table[k], 4)
			elif k[0] == "-":
				key = k.replace("-", "+", 1)

				if not key in self.table:
					auxdictionary[key] = round(1.0 - self.table[k], 4)

		self.table = auxdictionary

def set_parents(node_list, probabilities_list):
	for element in node_list:
		element.addParentandTable(probabilities_list)
		element.completeTable()

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

def parse_query(query): 
	#this method receives the probability to be calculated and converts it to the conditional probability form
	#Numerator: P(Evidence, Query)
	#Denominator: P(Evidence)
	return parsed_query

def conditional_probability(parsed_query):
	numerator = 0
	denominator = 0
	#get the numerator / denominator from the parsed query
	#check all the nodes that are given
	#not given nodes have to be calculated by true and false 
	#Apply all the permutations possible (call create_permutations method)
	# for each permutation (I think this is the chain rule(?) --- call chain_rule method)
		#calculate probabilities for each node in the permutation (multiplication)
		#consider all the parents of each node
		#check probability table to calculate each node's probability
	
	# Add up all permutations
	# Do the same for the denominator 
	#divide 
	return numerator / denominator

def create_permutations():
	permutations = []

	return permutations

def chain_rule():
	#get permutations
		# for each permutation
		#calculate probabilities for each node in the permutation (multiplication)
		#consider all the parents of each node
		#check probability table to calculate each node's probability
	return probability 

def bayes(nodes, probabilities, queries):
	nodes_list = create_nodes(nodes)
	#print(nodes_list)
	probabilities_list = parse_probabilities(probabilities)
	#print(probabilities_list)
	set_parents(nodes_list, probabilities_list)

	#print(nodes_list)


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
