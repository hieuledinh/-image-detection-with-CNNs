import numpy as np

maxtrix_1d = np.array([1, 2, 3])
maxtrix_2d = np.array([[1, 2, 3], [2, 4, 6], [7, 8, 9]])
maxtrix_3d = np.array(
    [[[1, 2, 3], [2, 4, 6], [7, 8, 9]], [[1, 2, 3], [2, 4, 6], [7, 8, 9]]]
)

# print(maxtrix_2d)
print(maxtrix_3d)

# padding
# maxtrix_1d_padding = np.pad(maxtrix_1d,(2,4), 'constant', constant_values=(3,1))
# print(maxtrix_1d_padding)

# maxtrix_2d_padding = np.pad(maxtrix_2d, ((1, 2), (2, 3)), "constant", 
#                             constant_values=((5, 1), (3, 4)))
# print(maxtrix_2d_padding)

maxtrix_3d_padding = np.pad(maxtrix_3d, ((1, 2), (2, 3),(1,4)), "constant", constant_values=((1,2),(3,4),(5,6)))
print(maxtrix_3d_padding)
