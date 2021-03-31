from octeract import *
from LinearizeBilinearContBinary import LinearizeBilinearContBinaryMod

m = Model()
m.import_model_file('model.nl')
print("======== Model before =========")
print(m)

m.apply_mod(LinearizeBilinearContBinaryMod)

print("======== Model after =========")
print(m)

m.write_problem_to_NL_file('/my/file/name.nl')
#m.write_problem_to_LP_file('/my/file/name.lp')
#m.write_problem_to_MPS_file('/my/file/name.mps')
#m.write_problem_to_GAMS_file('/my/file/name.gms')
