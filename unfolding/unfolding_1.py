import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/john/workspace/foil_activation/rf')
from rf_manager import package_rfs
sys.path.append('/home/john/workspace/foil_activation/response')
from response_manager import package_responses
sys.path.append('/home/john/workspace/sandii')
from sandii import iterate


# import response functions
b = package_responses(1, 1)
b_err = np.sqrt(b)

# import responses
A = package_rfs([0, 1, 2, 3, 10, 11, 12, 13, 14])

# import default spectrum
x0 = np.ones(len(A[0]))

solution = iterate(x0, b, b_err, A)
plt.plot(solution)
plt.yscale('log')
