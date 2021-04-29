from octeract import *

# Symbolically match any fraction
my_match = Match("C(n)*E(f1)/E(f2)")

# Grab only the ones that could have zero denominators
my_filter = IsMaybeFeasible("f2==0")

# Add auxiliary variable with the range of f1/f2 as bounds
add_auxiliary_var = AddVariableSpan('w','f1/f2')

# Substitute f1/f2 with new var w
sub = SubWith("w")

# Remove the fraction by multiplying with f2
add_constraint1 = AddConstraint("fraction", "f2*w == f1")

# Enforce f2 != 0 for consistency
add_constraint2 = AddConstraint("denominator", "abs(f2) > 0.000001")

# Chain actions
my_actions = add_auxiliary_var + sub + add_constraint1 + add_constraint2

# Build mod
EliminateSingularityFractionMod = (my_match & my_filter).then(my_actions)
