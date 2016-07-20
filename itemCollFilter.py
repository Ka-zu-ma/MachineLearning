

#一般的には疎行列になる（多数ある映画の中で、1人が評価する数はどうしても限られる）なので、sparse を使うほうがよさそう。

import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine

df = pd.read_csv('u.data', sep = '\t', names = ['user_id','item_id','rating','timestamp'])

shape = (df.max().ix['user_id'],df.max().ix['item_id'])

R = np.zeros(shape)

for i in df.index:
	row = df.ix[i]
	R[row['user_id'] - 1, row['item_id'] - 1] = row['rating']

print(R);

#step1 アイテムの類似度を計算する

def compute_item_similarities(R):

	#n:movie counts
	n = R.shape[1]
	sims = np.zeros((n,n))

	for i in range(n):
		for j in range(i,n):
			if i == j:
				sim = 1.0
			else:
				# R[:,i]はアイテムiに関する全ユーザーの評価を並べた列ベクトル
				sim = similarity(R[:,i], R[:,j])

			sims[i][j] = sim
			sims[j][i] = sim

	return sims

def similarity(item1,item2):
	# item1 と item2 のどちらも評価済であるユーザの集合
	common = np.logical_and(item1 != 0, item2 != 0)

	v1 = item1[common]
	v2 = item2[common]

	sim = 0.0
	# 共通評価者が 2以上という制約にしている
	if v1.size > 1:
		sim = 1.0 - cosine(v1, v2)

	return sim


sims = compute_item_similarities(R)

print(sims)

#step2 評価を予測する

def predict(u,sims):

	x = np.zeros(u.size)
	x[u > 0] = 1

	scores = sims.dot(u)
	normalizers = sims.dot(x)

	prediction = np.zeros(u.size)

	for i in range(u.size):
		
		if normalizers[i] == 0 or u[i] > 0:
			prediction[i] = 0

		else:
			prediction[i] = scores[i] / normalizers[i]

	return prediction

u = np.array([5, 0, 1])

print (predict(u,sims))













