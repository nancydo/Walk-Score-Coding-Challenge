import sys

class Vertex:
	def __init__(self):
	    self.children = set()
	    self.parents = set()

graph = {}

# create the graph
for line in sys.stdin:
	line = line.rstrip("\n");
	edge = line.split("\t")

	# ignore lines that don't fit the format
	if len(edge) == 2:
		input = edge[0]
		output = edge[1]

		if input not in graph:
			graph[input] = Vertex();
		graph[input].children.add(output)

		if output not in graph:
			graph[output] = Vertex()
		graph[output].parents.add(input)

# process the graph to get rid of vertices which have
# one input and one output
for key, value in graph.iteritems():
	if len(value.parents) == 1 and len(value.children) == 1:
		# connect neighbors directly
		parent = list(value.parents)[0]
		child = list(value.children)[0]

		# replace the parent's child with this key's child
		graph[parent].children.add(child)
		graph[parent].children.remove(key)

		# similarly, replace the child's parent with this key's parent
		graph[child].parents.add(parent)
		graph[child].parents.remove(key)

		# removing the item from the dictionary causes problems with
		# the loop, so instead, mark it as having no parents and children
		value.parents = value.children = 0

# print the graph
for key, value in graph.iteritems():
	if value.children:
		for c in value.children:
			print key + "\t" + c;