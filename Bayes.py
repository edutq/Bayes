import itertools
import copy
import json
import decimal
import math

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

def parse_query(query, node_list): 
	#this method receives the probability to be calculated and converts it to the conditional probability form
	numerator = ""
	denominator = ""
	for element in query:
		#print(element)
		numerator = ""
		denominator = ""
		var = element.split("|")
		if len(var) == 2:
			numerator = var[0] + ',' + var[1]
			denominator = var[1]
		elif len(var) == 1:
			numerator = var[0]
		
		conditional_probability(numerator, denominator, node_list)
	return 0

def conditional_probability(numerator, denominator, node_list):

	#get the numerator / denominator from the parsed query
	print()
	print("numerator")
	
	numeratorhidden = []
	numeratorgiven = numerator.split(',')
	print(numeratorgiven)
	for element in numeratorgiven:

		if "+" in element:
			auxelement = element.replace('+', "")
		elif "-" in element:
			auxelement = element.replace('-', "")
		node = get_node(auxelement, node_list)
		ancestors = []
		if node.parents:
			get_ancestors(node, node_list, ancestors)

		for ancestor in ancestors:

			if not "+" + ancestor in numeratorgiven and not "-" + ancestor in numeratorgiven and not ancestor in numeratorhidden:
				numeratorhidden.append(ancestor)
	print(numeratorhidden)
	if numeratorhidden:
		permitationsnumerator = create_permutations(numeratorhidden)
		enumeratorNUvariables = appendgivenandhidden(numeratorgiven, permitationsnumerator)
		print(enumeratorNUvariables)
	else:
		enumeratorNUvariables = numeratorgiven
	print()
	print("denominator")
	
	denominatorhidden = []
	denominatorgiven = denominator.split(',')
	print(denominatorgiven)
	for element in denominatorgiven:

		if "+" in element:
			auxelement = element.replace('+', "")
		elif "-" in element:
			auxelement = element.replace('-', "")
		node = get_node(auxelement, node_list)
		ancestors = []
		if node.parents:
			get_ancestors(node, node_list, ancestors)

		for ancestor in ancestors:

			if not "+" + ancestor in denominatorgiven and not "-" + ancestor in denominatorgiven and not ancestor in denominatorhidden:
				denominatorhidden.append(ancestor)
	print(denominatorhidden)

	if denominatorhidden:
		permitationsdenominator = create_permutations(denominatorhidden)
		#print(denominatorgiven)
		enumeratorDEvariables = appendgivenandhidden(denominatorgiven, permitationsdenominator)
		print(enumeratorDEvariables)
	else:
		enumeratorDEvariables = denominatorgiven
	#check all the nodes that are given
	#not given nodes have to be calculated by true and false 
	#Apply all the permutations possible (call create_permutations method)
	# for each permutation (I think this is the chain rule(?) --- call chain_rule method)
		#calculate probabilities for each node in the permutation (multiplication)
		#consider all the parents of each node
		#check probability table to calculate each node's probability
	numeratorvalue = chain_rule(enumeratorNUvariables)
	denominatorvalue = chain_rule(enumeratorDEvariables)
	# Add up all permutations
	# Do the same for the denominator 
	#divide 
	return 0

def get_node(name, node_list):
	for element in node_list:
		if element.name == name:
			return element
	return False

def appendgivenandhidden(given, combinations):
	result = []
	aux = []
	for i in range(len(combinations)):
		aux = []
		for element in given:

			aux.append(element)
		for element in combinations[i]:
			aux.append(element)
		result.append(aux)
	return result

def get_ancestors(node, node_list, ancestors):
	if node.parents:
		for element in node.parents:
			if element not in ancestors:
				ancestors.append(element)
			newnode = get_node(element, node_list)
			get_ancestors(newnode, node_list, ancestors)
	else:
		if node.name not in ancestors:
			ancestors.append(node.name)

def create_permutations(hiddenvariables):
	combinations = []
	allpositive = copy.deepcopy(hiddenvariables)
	allnegative = copy.deepcopy(hiddenvariables)
	combination_list = []
	number = 0
	flag = True
	for i in range(len(allpositive)):
		allpositive[i] = "+" + allpositive[i]
	for i in range(len(allnegative)):
		allnegative[i] = "-" + allnegative[i]


	for i in range(2**(len(hiddenvariables) - 1)):
		number = math.ceil(math.sqrt(i))
		if number == 0:
			number = 1
		combination_list = []
		for j in range(len(hiddenvariables)):

			if j == number - 1:
				if flag:
					combination_list.append(allpositive[j])
					flag = False
				else: 
					combination_list.append(allnegative[j])
					flag = True
			else:
				combination_list.append(allpositive[j])

		combinations.append(combination_list)
	reverse_combinations = reverse(combinations)
	for element in reverse_combinations:
		combinations.append(element)
	#print(reverse_combinations)

	return combinations

def reverse(combi):

	rev = []
	aux_list = []
	for element in combi:
		aux_list =[]
		for item in element:
			if "+" in item:
				aux_list.append(item.replace("+", "-"))
			elif "-" in item:
				aux_list.append(item.replace("-", "+"))
		rev.append(aux_list)
	return rev

def chain_rule(list_combinations):
	#get permutations
		# for each permutation
		for element in list_combinations:
			print(element)
		#calculate probabilities for each node in the permutation (multiplication)
		#consider all the parents of each node
		#check probability table to calculate each node's probability
	return probability 

def bayes(nodes, probabilities, queries):
	nodes_list = create_nodes(nodes)
	probabilities_list = parse_probabilities(probabilities)
	set_parents(nodes_list, probabilities_list)
	parse_query(queries, nodes_list)
	#print(nodes_list)
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
