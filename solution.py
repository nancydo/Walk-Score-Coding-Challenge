class Vertex:
	def __init__(self):
	    self.children = set()
	    self.parents = set()

# open the input file
file = open("input/1", "r")

graph = {}

# create the graph
for line in file:
	line = line.rstrip("\n");
	edge = line.split("\t")
	input = edge[0]
	output = edge[1]

	if input not in graph:
		graph[input] = Vertex();
	graph[input].children.add(output)

	if output not in graph:
		graph[output] = Vertex()
	graph[output].parents.add(input)

# print the graph
for key, value in graph.iteritems():
	if value.children:
		for c in value.children:
			print key + "\t" + c;
