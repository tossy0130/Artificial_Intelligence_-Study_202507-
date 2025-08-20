import numpy as np
import matplotlib.pyplot as plt

###### ステップ関数
def step_function(x):
  # 0 以下の場合は 0 を返し、それ以外は 1を返す
  return np.where(x<=0, 0, 1)

### 実行
x = np.linspace(-5, 5)
y = step_function(x)

plt.plot(x, y)
plt.show()