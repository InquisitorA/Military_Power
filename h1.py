import os
import glob
import pandas as pd
import numpy as np


# L=np.array([i+1 for i in range (133)])
# L1=pd.read_csv("countries.csv")
# L2=pd.read_csv("country_n.csv")

# ct=0
# for i in range(0,len(L1)):
# 	for j in range(0,len(L2)):
# 		if(L1.iat[i,2]==L2.iat[j,0]):
# 			ct+=1
# 			for k in range(0,7):
# 				L1.iat[i,k+8]=L2.iat[j,k+2]


# print(ct)


# L1.to_csv("countries_n.csv",index=False,encoding='utf-8-sig')


L3=pd.read_csv("countries_n.csv")
mp={}
N=[]

for i in range(0,len(L3)):
	mp[L3.iat[i,3]]=L3.iat[i,0]
	N.append(L3.iat[i,3])
	
# L3.to_csv("states_n.csv",index=False,encoding='utf-8-sig')

L4=pd.read_csv("cities.csv")
# mp={}
rs=[]

for j in range(0,len(L4)):
	if(L4.iat[j,5] in mp):
		L4.iat[j,4]=mp[L4.iat[j,5]]
	else:
		L4.iat[j,4]=0
		rs.append(j)
	




# L4=pd.read_csv("cities_n.csv")
# rs=[]
# for j in range(0,len(L4)):
# 	if(L4.iat[j,2]==0):
# 		rs.append(j)

L4=L4.drop(rs)
L4.to_csv("cities_nn.csv",index=False,encoding='utf-8-sig')






