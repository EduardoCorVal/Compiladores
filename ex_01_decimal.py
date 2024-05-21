from delta import Compiler, Phase

source = '666'

c = Compiler('program')
# Si no se poné la fase, 
c.realize(source, Phase.EVALUATION)

# SYNTACTIC_ANALYSIS
# Parse tree -> Me da el arbol de parseo de los elementos
# print(c.parse_tree_str)

# SEMANTIC_ANALYSIS
print(c.parse_tree_str)

# CODE_GENERATION
# print(c.wat_code)

# EVALUATION 
# print(c.result)
