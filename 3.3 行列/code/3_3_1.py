import numpy as np

# (1次元)配列
A = np.array([1, 2, 3, 4]) 
print(A)           # 配列の表示
print(np.ndim(A))  # 配列の次元
print(A.shape)     # 配列の形状
print(A.shape[0])  # 配列の形状（タプル）の1つ目の要素

# 2次元配列
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))
print(B.shape)  