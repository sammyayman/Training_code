import numpy as np
print('\033c')
# arrA = np.array([[1, 2, 3, 4, 5] , [6-1j, 7-2j, 8+3j, 9+4j, 10] , [True, False, True, False, True] , ['a', 'b', 'c', 'd', 'e']], dtype=object)
# print(arrA)
# print(arrA.dtype)
# print(arrA.shape)
# print(arrA.size)
# print(arrA.ndim)

arrB = np.array([[1, 2, 3, 4, 5], [0, 1, 0, 1, 1]])
arrB_obj = arrB.astype(object)
arrB_obj[1] = arrB_obj[1].astype(bool)
print(arrB_obj[1])  # -> [False  True False  True  True]
print(arrB_obj)
# print(arrB.dtype)
# print(arrB.shape)
# print(arrB.size)
# print(arrB.ndim)


arr2d = np.arange(12).reshape(3, 4)   # 0..11 → shape (3,4)
# Example with start/stop/step:
arr2d_custom = np.arange(10, 22, 1).reshape(3, 4)  # shape (3,4)
print(arr2d_custom)