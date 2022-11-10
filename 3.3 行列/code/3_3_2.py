import numpy as np

# 行列の積（2×2）
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A.shape)      # -> (2, 2)
print(B.shape)      # -> (2, 2)
print(np.dot(A, B)) # AとBの積を計算

# 行列の積（2×3と3×2）
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)      # -> (2, 3)
print(B.shape)      # -> (3, 2)
print(np.dot(A, B)) 
print(np.dot(B, A)) # この2つは結果が異なる
