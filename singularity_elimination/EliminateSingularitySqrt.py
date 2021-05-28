from octeract import *

# Eliminate domain-based singularities for all square root terms
# If the function inside a square root term can be negative,
# add a constraint to ensure that it's always positive.

# Symbolic match for any term of type constant*sqrt(f)
my_match = Match("C(n)*sqrt(E(f))")

# Only select the ones that might cross into negative domains
my_filter = IsMaybeFeasible("f <= -1.e-12")

# Add a constraint to enforce positivity
my_actions = AddConstraint("f >= 0.000001")

EliminateSingularitySqrtMod = (my_match & my_filter).then(my_actions)
