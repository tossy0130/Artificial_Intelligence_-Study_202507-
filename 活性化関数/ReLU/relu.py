import numpy as np
import matplotlib.pyplot as plt

def relu_function(x):
  return np.where(x <= 0, 0, x)

### 実行 ###
x = np.linspace(-5, 5)
y = relu_function(x)

plt.plot(x, y)
plt.show()
