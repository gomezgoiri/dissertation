#! /bin/python

# Using: https://github.com/gjhiggins/n3_pygments_lexer

import os
from optparse import OptionParser
from pygments import highlight
from pygments.formatters import LatexFormatter
from notation3_lexer import Notation3Lexer



# pygmentize -f latex -O full -l python options.input > "%s.tex"%output 
# pygmentize -f latex -l python options.input > "%s.tex"%output 
def generate_pygments_tex_file( input_file_path, output_file_path ):
    if output_file_path is None:
	inputf_no_ext = input_file_path.split(".")[0]
	output_file_path = inputf_no_ext + ".tex"
	
    print "Reading Notation 3 file: " + input_file_path
    with open (input_file_path, "r") as input_file:
	code = input_file.read()
	# LatexFormatter( full = True ) may be useful to see the packages, color definitions, etc. required by the LaTeX document importing it
	# linenos = True to show line numbers
	
	linenos = not inputf_no_ext.endswith("nolinenos")
	highlighted_code = highlight(	code,
					Notation3Lexer(),
					LatexFormatter( linenos = linenos )
					)
	
	# super-ugly fix to hidde syntax errors.
	# It would be better to simply fix the lesser
	highlighted_code = r"\expandafter\def\csname PY@tok@err\endcsname{}" + "\n" + highlighted_code
	
	print "Generating pygmented file: " + output_file_path
	with open (output_file_path, "w") as output_file:
	    output_file.write( highlighted_code )



if __name__=="__main__":
    parser = OptionParser( usage = "usage: %prog [options] input_file" )
    parser.add_option("-o", "--output", dest="output", default=None,
		      help="Tex output file")

    (options, args) = parser.parse_args()

    if len(args) == 0:
	#os.chdir("/mydir")
	for filep in os.listdir("."):
	    if filep.endswith(".n3"):
		generate_pygments_tex_file( filep, None )
    else:
	generate_pygments_tex_file( args[0], options.output )