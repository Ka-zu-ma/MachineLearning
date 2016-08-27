
#sparse

import numpy as np
import pandas as pd
from scipy import sparse

df = pd.read_csv('u.data', sep='\t', names=['user_id','item_id', 'rating', 'timestamp'])

shape = (df.max().ix['user_id'] + 1, df.max().ix['item_id'] + 1)
R = sparse.lil_matrix(shape) 

for i in df.index:
    row = df.ix[i]
    R[row['user_id'], row['item_id']] = row['rating']

print(R.todense())
