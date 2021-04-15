from octeract import *
from LinearizeBilinearBinaryBinary import LinearizeBilinearBinaryBinaryMod
from LinearizeBilinearContBinary import LinearizeBilinearContBinaryMod

m = Model()

m.add_variable("y1", 0, 1, BIN)
m.add_variable("y2", 0, 1, BIN)
m.add_variable("y3", 0, 1, BIN)
m.add_variable("x", -10, 10)
m.minimize("y1*y2 + x*y1")

m.set("y2*y3 + y2*x + y2*y1").to(0)

print(m)

m.apply_mod(LinearizeBilinearBinaryBinaryMod)
m.apply_mod(LinearizeBilinearContBinaryMod)

print(m)


