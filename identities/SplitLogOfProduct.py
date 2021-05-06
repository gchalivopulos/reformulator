from octeract import *

# Reformulate log(f*g) to log(f) + log(g) if f*g is potentially positive,
# and enforce that the split is mathematically valid, i.e., that f, g need
# to be individually positive.

# Symbolic match for any term of type constant*log(f*g)
my_match = Match("C(n)*log(E(f)*E(g))")

# Only select the ones that might cross into negative domains
my_filter = IsFullyFeasible("f >= 0") & IsFullyFeasible("g >= 0")

# Split logarithm
action = SubWith("n*log(f)+n*log(g)")

SplitLogOfProductMod = (my_match & my_filter).then(action)
