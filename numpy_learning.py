import numpy as np

print(np.__version__)
np.show_config()

Z = np.zeros(10)
print(Z)

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))

# %run `python -c "import numpy; numpy.info(numpy.add)"`

Z = np.zeros(10)
Z[4] = 1
print(Z) 


Z = np.arange(10,50)
print(Z)



Z = np.arange(50)
Z = Z[::-1]
print(Z)


Z = np.arange(9).reshape(3,3)
print(Z)

nz = np.nonzero([1,2,0,0,4,0])
print(nz)

## numpy.eye() で生成、identity() と似ているが列数指定ができる
Z = np.eye(3)
print(Z)

Z = np.random.random((3,3,3))
print(Z)

Z = np.random.random((10.10))
Zmin,Zmax = Z.min(),Z.max()
print(Zmin,Zmax)

Z = np.random.random(30)
m = Z.mean()
print(m)

# 15
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)

# 16 
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

#17
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)

#18
Z = np.diag(1 + np.arange(4),k = -1)
print(Z)

#19 0と1がチェック柄のように並ぶ
Z = np.zeros((8,8),dtype = int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

#20 100番目の要素のインデックス　(6,7,8)が行列の次元
print(np.unravel_index(100,(6,7,8)))

# 21

Z = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(Z)

#22
Z = np.random.random((5,5))
Zmax,Zmin = Z.max(),Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)

#23












































