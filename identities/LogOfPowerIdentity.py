from octeract import *

# Reformulate log(f^g) to g*log(f) if f is positive,
# and enforce that the split is mathematically valid, i.e., that f has to be positive

# Symbolic match for any term of type constant*log(f*g)
my_match = Match("C(n)*log(C(n1)*E(f)^E(g))")

# Only select the ones that might cross into negative domains
my_filter = IsFullyFeasible("f >= 0")

# Split logarithm
action = SubWith("n*g*log(n1*f)")

LogOfPowerIdentityMod = (my_match & my_filter).then(action)
