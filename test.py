import numpy as np # numpyをnpとしてimport
from numpy.random import randint # numpy.random.randintをrandintとしてimport
# 変数arr1に、各要素が0以上10以下の整数の行列(5 × 2)を代入
arr1 = randint(0, 11, (5, 2))
print(arr1)
# 変数arr2に0~1までの一様乱数を3つ代入
arr2 = np.random.rand(3)
print(arr2)