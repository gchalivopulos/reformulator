from octeract import *

# Reformulate |f| to f if f is positive.

# Symbolic match for any term of type constant*log(f*g)
my_match = Match("C(n)*abs(E(f))")

# Only select the ones that might cross into negative domains
my_filter = IsFullyFeasible("f >= 0")

# Split logarithm
action = SubWith("n*f")

PositiveAbsMod = (my_match & my_filter).then(action)
