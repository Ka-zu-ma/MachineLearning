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

z = x[x>=5] #5以上を抽出

z = x[(x>=5)&(x<8)] #5以上8未満を抽出

#yが1になっているxのデータを抽出

z = x[y==1]

x[x<5] = 0

x[x>=5] = 1 


#欠損値を置き換える

x = np.array([[1,2,3],[4,np.nan,5],[6,7,8]])

#欠損値を0に置き換え
#x[np.isnan(x)] = 0

#欠損値を平均値(欠損値除いた平均値)に置き換え

x[np.isnan(x)] = np.nanmean(x)


#欠損値を含む行または列を除外する


x = np.array([[1,2,3],[4,np.nan,5],[6,7,8]])

z = x[~np.isnan(x).any(axis=1)]

#欠損値を含む列を除外

z = np.ma.compress_cols(np.ma.masked_invalid(x))

#配列を連結する(行方向、列方向)

x1 = np.arange(start = 0,stop = 3)

x2 = np.arange(start = 3,stop = 6)





#行を追加
z = np.vstack([x1,x2])


#列を追加

z = np.hstack([x1,x2])
z = np.r_[x1,x2]#上と同じ


#行を追加(補足)

z = np.dstack([x1,x2])

z = np.c_[x1,x2] #上と同じ

z = np.vstack([x1,x2]).T #vstackの結果を転置

#転置行列とは、m 行 n 列の行列 A に対して A の (i, j) 要素と (j, i) 要素を入れ替えた n 行 m 列の行列


#<集計する(基本統計量、行方向、列方向)>

x = np.arange(10)

#合計
z = x.sum()













print(z)
