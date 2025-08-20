import numpy as np
import matplotlib.pyplot as plt

###### シグモイド関数
def sigmoid_function(x):
  return 1/(1+np.exp(x)) # exp => ネイピア数の累乗を表す

### 実行 ###
x = np.linspace(-5, 5)
y = sigmoid_function(x)

plt.plot(x, y)
plt.show()
