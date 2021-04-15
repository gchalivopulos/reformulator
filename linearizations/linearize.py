from octeract import *
from LinearizeBilinearBinaryBinary import LinearizeBilinearBinaryBinaryMod
from LinearizeBilinearContBinary import LinearizeBilinearContBinaryMod
from LinearizeSquaredBinary import LinearizeSquaredBinaryMod

m = Model()

m.add_variable("y1", 0, 1, BIN)
m.add_variable("y2", 0, 1, BIN)
m.add_variable("y3", 0, 1, BIN)
m.add_variable("x", -10, 10)
m.minimize("2*y1*y2 + 3*x*y1 + y1^2")

m.set("y2*y3 + y2*x + 5*y2*y1 - 5*y2^2").to(0)

print(m)

m.apply_mod(LinearizeBilinearBinaryBinaryMod)
m.apply_mod(LinearizeBilinearContBinaryMod)
m.apply_mod(LinearizeSquaredBinaryMod)

print(m)


