import numpy as np

# probability of pic being a cat or not
p = [1, 0]
# probability of model making this prediction
q = [0.25, 0.75]

# cross entropy
H = 0
for i in range(len(p)):
    H -= p[i] * np.log(q[i])
print(H)

# explicitly written
H = -(p[0] * np.log(q[0]) + p[1] * np.log(q[1]))
print(H)

# p[1] is always 0, p[0] is always 1
H = -np.log(q[0])
print(H)

# implementing in pytorch
import torch as tor
import torch.nn.functional as F

p_tensor = tor.tensor(p, dtype=float)
q_tensor = tor.tensor(q, dtype=float)

H = F.binary_cross_entropy(q_tensor, p_tensor)
print(H)
