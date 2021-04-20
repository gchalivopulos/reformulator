from octeract import *
from EliminateSingularityLog import EliminateSingularityLogMod

m = Model()

m.add_variable("y",0,10)
m.minimize("log(x^3+x^2+2)")

m.set("x").to("log(y+1)")

print(m)

m.apply_mod(EliminateSingularityLogMod)

print(m)
