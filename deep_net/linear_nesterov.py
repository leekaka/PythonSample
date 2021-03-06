import numpy as np
import math 

# 普通的全梯度下降+nag方法

sample = 10
num_input = 5

#加入训练数据
normalRand = np.random.normal(0,0.1,sample)
weight = [7,99,-1,-333,0.06]
x_train = np.random.random((sample, num_input))
y_train = np.zeros((sample,1))
for i in range (0,len(x_train)):
	total = 0
	for j in range(0,len(x_train[i])):
		total += weight[j]*x_train[i,j]
	y_train[i] = total+normalRand[i]

# 训练
weight = np.random.random(num_input+1)
lastGrade = np.zeros((num_input+1,))
rate = 0.05
discount = 0.9

for epoch in range(0,100):

	# 预走一步
	oldWeight = np.copy(weight)
	for i in range(0,len(weight)):
		weight[i] = weight[i]-rate*discount*lastGrade[i]

	# 计算loss
	predictY = np.zeros((len(x_train,)))
	for i in range(0,len(x_train)):
		predictY[i] = np.dot(x_train[i],weight[0:num_input])+weight[num_input]
	loss = 0
	for i in range(0,len(x_train)):
		loss += (predictY[i]-y_train[i])**2
	print("epoch: %d-loss: %f"%(epoch,loss))

	# 计算梯度并更新
	weight = oldWeight
	for i in range(0,len(weight)-1):
		grade = 0
		for j in range(0,len(x_train)):
			grade += (predictY[j]-y_train[j])*x_train[j,i]
		lastGrade[i] = lastGrade[i]*discount+grade
		weight[i] = weight[i] - rate*lastGrade[i]

	grade = 0
	for j in range(0,len(x_train)):
		grade += (predictY[j]-y_train[j])
	lastGrade[num_input] = lastGrade[num_input]*discount+grade
	weight[num_input] = weight[num_input] - rate*lastGrade[num_input]

print(weight)