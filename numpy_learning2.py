import numpy as np

#<テストデータを生成>

#0が10個ある配列
z = np.zeros(10)



#1が10個ある配列
z = np.ones(10)


#1ずつ増える配列
z = np.arange(10, step=2)

#正規分布に従う乱数を10個生成
z = np.random.randn(10)



#二項分布に従う乱数を10個生成
z = np.random.binomial(n=100, p=0.1, size=(10))



#ポアソン分布に従う乱数を10個生成
z = np.random.poisson(lam = 10, size = (10))



#ある範囲の整数をランダムに生成
z = np.random.randint(low = 0, high = 2, size = 10)#0~high - 1 が生成される範囲

#2*3の行列を生成
z = np.arange(6).reshape((2,3))

#2*3*4*5の行列を生成
z = np.arange(2*3*4*5).reshape((2,3,4,5))

#<ある行、列だけを抽出する(インデックスで指定)>

x = np.array([[1,2,3],[4,5,6]])
x = np.arange(9).reshape((3,3))

#2列目を抽出
z = x[:,1]

#2行目以降を抽出

z = x[1:]

#2列目以降を抽出

z = x[:,1:]

#2列目までを抽出

z = x[:,:2]

#<条件に合うデータだけを置き換える(条件式で指定)>

x = np.arange(9).reshape((3,3))

print(x)

y = np.eye(3)

print(y)


#条件に合うデータを抽出

z = x[x&gt;=5]










print(z)
