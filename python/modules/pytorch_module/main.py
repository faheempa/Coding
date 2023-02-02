import torch

x =torch.empty(1) # 1 D
print(x)
x =torch.empty(1,2) # 2D
print(x)
x =torch.empty(1,2,3) # 3D
print(x)
x =torch.empty(1,2,3,4) #4D
print(x)
x=torch.zeros(2) 
print(x)
x=torch.ones(2)
print(x)
x=torch.ones(2, dtype=torch.int)
print(x.dtype)
x=torch.ones(2, dtype=torch.double)
print(x.dtype)
x=torch.ones(2, dtype=torch.float16)
print(x.dtype)
print(x.size())
x=torch.tensor([1.3, 5.6])
print(x)
print("-"*50)

x=torch.rand(2,2)
y=torch.rand(2,2)
print(x)
print(y)
print(x+y)