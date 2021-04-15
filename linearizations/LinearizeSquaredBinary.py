from octeract import *

# Linearize quadratic term x^2 where x binary
# =============================================
# y^2 = y
# =============================================

# Define symbolic trigger
my_trigger = Match('C(n)*V(x)^2') 

# Filter binaries 
my_filter = IsBinary('x')

# Specify how to change the model
substitute_term = SubWith('n*x')

# Create mod
LinearizeSquaredBinaryMod = (my_trigger & my_filter).then(substitute_term)
