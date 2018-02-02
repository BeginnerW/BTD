import numpy as np
from sktensor import dtensor,tucker

T = np.zeros((3, 4, 2))
T[:, :, 0] = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
T[:, :, 1] = [[13, 16, 19, 22], [14, 17, 20, 23], [15, 18, 21, 24]]
print T
T = dtensor(T)
Y = tucker.hooi(T, [2, 3, 1], init='nvecs')
print "___"