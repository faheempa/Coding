# entropy
import numpy as np

# 25% probability of an event happening and 75% not happening
x = [0.25, 0.75]

H = 0
for p in x:
    H = H + (-p * np.log(p))

print("Entropy: ", H)

# explicitily wriiten as
p=0.25
H = -(p * np.log(p) + (1-p) * np.log(1-p))
print("Entropy: ", H)


