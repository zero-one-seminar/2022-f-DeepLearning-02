import numpy as np

X = np.array([1, 2])  # 入力
W = np.array([[1, 3, 5], [2, 4, 6]]) # 重み
Y = np.dot(X, W) # 出力
print(Y)
