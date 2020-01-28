#-*- coding: utf-8 -*-
from keras.models import ......
from keras.layers import ......
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import tensorflow as tf

# seed 값 설정
seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

df = pd.read_csv("./housing.csv", delim_whitespace=True, header=None)

print(df.info())    # 506개 dataframe, 14 col
print(df.head())

"""
Features
1. Per capita crime rate.
2. Proportion of residential land zoned for lots over 25,000 square feet.
3. Proportion of non-retail business acres per town.
4. Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
5. Nitric oxides concentration (parts per 10 million).
6. Average number of rooms per dwelling.
7. Proportion of owner-occupied units built prior to 1940.
8. Weighted distances to five Boston employment centres.
9. Index of accessibility to radial highways.
10. Full-value property-tax rate per $10,000.
11. Pupil-teacher ratio by town.
12. 1000 * (Bk - 0.63) ** 2 where Bk is the proportion of Black people by town.
13. % lower status of the population.

타깃은 주택의 중간 가격으로 천달러 단위입니다
"""

#%%
dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13]

X_train, X_test, Y_train, Y_test = ________(X, Y, test_size=0.2, random_state=seed)

#%%
# DNN Network Model 설계
# input feature : 13개, L1:30-units & relu, L2:6-units & relu, Output:1
........



model._____(loss='mean_squared_error',
              optimizer='adam', metrics=['mae'])

# Model Training
num_epochs = 200
all_mae_histories = []
history = model._____(X_train, Y_train, epochs=num_epochs, batch_size=32)

#mae_history = history.history['mean_absolute_error']  # error in keras2.3
mae_history = history.history['mae']
all_mae_histories.append(mae_history)

test_mse_score, test_mae_score = model.evaluate(X_test, Y_test)
print('-'*50)
print(test_mse_score, test_mae_score)

#%%
import numpy as np
average_mae_history = [
    np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
print(average_mae_history)

import matplotlib.pyplot as plt

plt.plot(range(1, len(average_mae_history) + 1), average_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Test MAE')
plt.show()

