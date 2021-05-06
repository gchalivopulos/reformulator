from octeract import *

# Reformulate log(f*g) to log(f) + log(g) if f*g is potentially positive,
# and enforce that the split is mathematically valid, i.e., that f, g need
# to be individually positive.

# Symbolic match for any term of type constant*log(f*g)
my_match = Match("C(n)*log(E(f)*E(g))")

# Only select the ones that might cross into negative domains
my_filter = IsMaybeFeasible("f*g >= 0") 

# Split logarithm
action1 = SubWith("n*log(f)+n*log(g)")

# Add constraints to enforce positivity
action2 = AddConstraint("force_positive_f_log", "f>=0")
action3 = AddConstraint("force_positive_g_log", "g>=0")

# Chain actions
my_actions = action1 + action2 + action3

SplitLogOfProductMod = (my_match & my_filter).then(my_actions)
