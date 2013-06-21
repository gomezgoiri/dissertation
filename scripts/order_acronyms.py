import re
from optparse import OptionParser
from collections import OrderedDict


def order_acronyms_alphabetically( filename ):
    acro_dict = {}
  
    with open( filename, 'r') as filee:
	regexp = re.compile( r"^(\s+\\acro\{(\w+)\}\[\w+\]\{.+\}.*)$", re.MULTILINE ) # r"(\s+\\acro\{(\w+)\}*)"
	for ex in regexp.findall( filee.read() ):
	    #print ex
	    acro_dict[ ex[1] ] = ex[0]

    for k in sorted( acro_dict.keys() ):
      print acro_dict[k]


if __name__=="__main__":
	parser = OptionParser()
	(options, args) = parser.parse_args()
	order_acronyms_alphabetically( args[0] )