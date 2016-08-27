import numpy as np

#1.テストデータを生成

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

print(z)
