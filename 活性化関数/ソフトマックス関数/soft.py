import numpy as np

def softmax_function(x):
    return np.exp(x) / np.sum(np.exp(x)) # ソフトマックス関数

### 実行
y = softmax_function(np.array([1,2,3]))
print(y)