# BASIC EXAMPLE

from octeract import *

# identifies cubed variables within certain bounds
trigger = Match("C(n)*V(var)^3") & IsFullyFeasible("abs(V(var)) < 11")

# creates linear variable to simulate cubed variable
mod = AddVariableSpan("sub", "V(var)^3") + AddConstraint("sub_con", "sub == V(var)^3")

# tracks cubed variable and either
#  - on first encounter: runs the mod and records linear variable
#  - on next encounters: retrieves linear variable
# then replaces cubed variable with linear variable
sub = Track("V(var)^3", mod) + SubWith("C(n)*sub")

# combines match and substitution
rule = trigger.then(sub)

# start model
m = Model()

# fill model
m.add_variable("x", -8, 8)
m.add_variable("y", -10, 10)
m.add_variable("z", -12, 12)
m.set_objective("3*y^2 - x^3 + 5*z^2")
m.add_constraint("con1", "y^3 - 3*x^2 >= 2")
m.add_constraint("con2", "3*z^3 + 2*x <= 5")
m.add_constraint("con3", "7*y - 5*z^3 <= 25")
print(m)

# solve model
m.global_solve()
m.print_solution_summary()

# reformulate model
m.apply_mod(rule)
print(m)

# solve model
m.global_solve()
m.print_solution_summary()
