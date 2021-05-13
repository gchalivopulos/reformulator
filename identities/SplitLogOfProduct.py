from octeract import *

# Reformulate n*log(f*g) to n*log(f) + n*log(g) 
# but only if f and g are both positive (otherwise the reformulation is not equivalent)

# Symbolic match for any term of type constant*log(f*g)
my_match = Match("C(n)*log(E(f)*E(g))")

# Check that both f and g are definitely positive
my_filter = IsFullyFeasible("f >= 0") & IsFullyFeasible("g >= 0")

# Split logarithm
action = SubWith("n*log(f)+n*log(g)")

SplitLogOfProductMod = (my_match & my_filter).then(action)
