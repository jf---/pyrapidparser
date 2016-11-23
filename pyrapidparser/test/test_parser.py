from rapid_ast import ModulesAST
from rapid_parser import RAPIDParser

parser = RAPIDParser(lex_optimize=True, yacc_debug=False, yacc_optimize=False)


fname = "/Users/jelleferinga/Documents/workspace/PyRAPID/Code/PyRAPID/C1-L02-02_C1-L02-07_15-rev5.prg"
f = open(fname, "r")
text = f.read()

# set debuglevel to 2 for debugging
t = parser.parse(text, 'x.rapid', debuglevel=0)



allmodule = ModulesAST(t)



