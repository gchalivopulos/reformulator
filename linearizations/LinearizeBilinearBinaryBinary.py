from octeract import *

# Linearize bilinear term x*y where x,y binary
# =============================================
# x*y = w
# w <= x
# w <= y
# x + y - 1 <= w
# 0 <= w <= 1
# =============================================

# Define symbolic trigger
my_trigger = Match('V(x)*V(y)') 

# Filter binaries 
my_filter = (IsBinary('x') & IsBinary('y'))

# Specify how to change the model
# Add auxiliary variable with the same bounds as x*y
add_auxiliary_var = AddVariableSpan('w_xy','x*y')
# Add parameters for the bounds of the continuous variable
substitute_term = SubWith('w_xy')
add_constraint0 = AddConstraint('w_xy <= x')
add_constraint1 = AddConstraint('w_xy <= y')
add_constraint2 = AddConstraint('x + y - 1 <= w_xy')

add_constraints = add_constraint0 + add_constraint1 + add_constraint2

# Add all modifications 
my_actions = add_auxiliary_var + substitute_term + add_constraints

# Create mod
LinearizeBilinearBinaryBinaryMod = (my_trigger & my_filter).then(my_actions)
