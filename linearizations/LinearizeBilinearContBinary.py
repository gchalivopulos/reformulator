from octeract import *

# Linearize bilinear term x*y where y is binary
# =============================================
# x_l*y-w<=0
# w-x_u*y<=0
# w-x+x_l*(1-y)<=0
# -w+x-x_u*(1-y)<=0
# x_l<=w<=x_u
# =============================================

# Define symbolic trigger
my_trigger = Match('V(x)*V(y)') 

# Filter binaries and account for permutations - we bind binary to b and non-binary to nb
xbin_filter = (IsBinary('x') & ~ IsBinary('y') & Bind('x', 'b') & Bind('y', 'nb'))
ybin_filter = (IsBinary('y') & ~ IsBinary('x') & Bind('y', 'b') & Bind('x', 'nb'))

# Combine the filters
my_filter = (xbin_filter | ybin_filter)

# Specify how to change the model
# Add auxiliary variable with the same bounds as x*y
add_auxiliary_var = AddVariableSpan('w_xy','b*nb')
# Add parameters for the bounds of the continuous variable
add_parameters = AddParameter('nb_LB','nb','lb') + AddParameter('nb_UB','nb','ub')
substitute_term = SubWith('w_xy')
add_constraint0 = AddConstraint('nb_LB*b-w_xy <= 0')
add_constraint1 = AddConstraint('w_xy-nb_UB*b <= 0')
add_constraint2 = AddConstraint('w_xy-nb-nb_LB*(1-b) <= 0')
add_constraint3 = AddConstraint('-w_xy+nb-nb_UB*(1-b) <= 0')

add_constraints = add_constraint0 + add_constraint1 + add_constraint2 + add_constraint3

# Add all modifications 
my_actions = add_auxiliary_var + add_parameters + substitute_term + add_constraints

# Create mod
LinearizeBilinearContBinaryMod = (my_trigger & my_filter).then(my_actions)
