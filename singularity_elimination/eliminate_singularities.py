from octeract import *
from EliminateSingularityLog import EliminateSingularityLogMod
from EliminateSingularitySqrt import EliminateSingularitySqrtMod


m = Model()

m.add_variable("y",0,10)
m.minimize("log(x^3+x^2+2)+sqrt(x^3+2*x+2)")

m.set("x").to("log(y+1)")
m.set("x").to("sqrt(y+1)")

print(m)

m.apply_mod(EliminateSingularityLogMod)
m.apply_mod(EliminateSingularitySqrtMod)

print(m)
