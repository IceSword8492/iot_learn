import warnings

warnings.filterwarnings('ignore')

import numpy as np
import time
from numpy.random import rand

# * 行の大きさ
N = 150

# * 行列を初期化します
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.array([[0] * N for _ in range(N)])

# * 開始時間を取得します
start = time.time()

# * for文を使って行列の掛け算を実行します
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("pythonの機能のみでの計算結果: %.4f[sec]" % float(time.time() - start))

# * NumPyを使って計算します

# * 開始時間を取得します
start = time.time()

# * NumPyを使って行列の掛け算を実行します
matC = np.dot(matA, matB)

print("NumPyを使った場合の計算結果: %.4f[sec]" % float(time.time() - start))
