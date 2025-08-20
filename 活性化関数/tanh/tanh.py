import numpy as np
import matplotlib.pyplot as plt

####### tanh
### -1 から 1 の間を滑らかに変化する関数
def tanh_function(x):
  return np.tanh(x)

### 実行 ###
x = np.linspace(-5, 5)
y = tanh_function(x)

plt.plot(x, y)
plt.show()
