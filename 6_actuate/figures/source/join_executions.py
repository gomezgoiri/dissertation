import json

def join_elements(el, el_to_join):
	for k in el: # e.g., rest or space
		prelength = len(el[k]["num_nodes"])
		addlength = len(el_to_join[k]["num_nodes"])
		assert( el[k]["num_nodes"]==el_to_join[k]["num_nodes"] )
		assert( len(el[k]["num_nodes"]) == len(el[k]["requests"]) )
		assert( len(el_to_join[k]["num_nodes"]) == len(el_to_join[k]["requests"]) )
		
		# join "requests"
		for i in range(len(el[k]["requests"])):
			el[k]["requests"][i] += el_to_join[k]["requests"][i]


def assertNRepetitions(elements, number):
	for k in elements:
		for req in elements[k]["requests"]:
			assert( len(req) == number ) # "This case should have been executed %d times." % number

if __name__ == "__main__":
	import sys
	
	sys.argv.pop(0)
	
	elements = None
	i = len(sys.argv)
	for arg in sys.argv:
		i -= 1
		if arg.endswith(".json"):
			with open(arg, "r") as ifile:
				if elements is None:
					elements = json.load(ifile)
				else:
					join_elements(elements, json.load(ifile))
		else:
			if i!=0 and i!=1: # not last two elements
				print "Not a file"
	
	last = len(sys.argv)
	if sys.argv[last-2] == "-n":
		assertNRepetitions(elements, int(sys.argv[last-1]))
	print json.dumps(elements)