from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x,y = datasets.make_regression(n_samples=100,n_features=1,noise=30)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train,y_train)

print("回帰分析は",e.coef_,"です。")
# regression coefficient
print("切片は",e.intercept_,"です。")
#2点間の

y_pred = e.predict(x_test)

print("学習データによる決定係数は",e.score(x_train,y_train),"です。")
print("テストデータによる決定係数は",e.score(x_test,y_test),"です。")
# e.score = 決定係数を導き出す式

plt.scatter(x_train,y_train,label="train")
plt.scatter(x_test,y_test,label="test")
plt.plot(x_test,y_pred,color="m")
plt.legend()

plt.show()

from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x,y = datasets.make_regression(n_samples=100,n_features=1,noise=30)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train,y_train)

print("回帰係数は",e.coef_,"です。")
print("切片は",e.intercept_,"です。")

y_pred = e.predict(x_test)

print("学習データによる決定係数は",e.score(x_train,y_train),"です。")
print("テストデータによる決定係数は",e.score(x_test,y_test),"です。")

plt.scatter(x_train,y_train,label="train")
plt.scatter(x_test,y_test,label="test")
plt.plot(x_test,y_pred,color="m")
plt.legend()

plt.show()

from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x,y = datasets.make_regression(n_samples=100,n_features=1,noise=30)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train,y_train)

print("回帰係数は",e.coef_,"です。")
print("切片は",e.intercept_,"です。")

y_pred = e.predict(x_test)

print("学習データによる決定係数は",e.score(x_train,y_train),"です。")
print("テストデータによる決定係数は",e.score(x_test,y_test),"です。")

plt.scatter(x_train,y_train,label="train")
plt.scatter(x_test,y_test,label="test")
plt.plot(x_test,y_pred,color="m")
plt.legend()

plt.show()

from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x,y = datasets.make_regression(n_samples=100,n_features=1,noise=30)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train,y_train)

print("回帰係数は",e.coef_,"です。")
print("切片は",e.intercept_,"です。")

y_pred = e.predict(x_test)

print("学習データは",e.score(x_train,y_train),"です。")
print("テストデータは",e.score(x_test,y_test),"です。")

plt.scatter(x_train,y_train,label="train")
plt.scatter(x_test,y_test,label="test")
plt.plot(x_test,y_pred,color="m")
plt.legend()

plt.show()

from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

data,label = datasets.make_blobs(n_samples=500,n_features=2,centers=5)

e = cluster.KMeans(n_clusters=5)
e.fit(data)

print(e.labels_)
print(e.cluster_centers_)

plt.scatter(data[:,0],data[:,1],marker="o",c=e.labels_,edgecolor="k")
plt.scatter(e.cluster_centers_[:,0],e.cluster_centers_[:,1],marker="x")

plt.show()

from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

data,label = datasets.make_blobs(n_samples=500,n_features=2,centers=5)

e = cluster.KMeans(n_clusters=5)
e.fit(data)

print(e.labels_)
print(e.cluster_centers_)

plt.scatter(data[:,0],data[:,1],marker="o",c=e.labels_,edgecolor="k")
plt.scatter(e.cluster_centers_[:,0],e.cluster_centers_[:,1],marker="x")
plt.show()

from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
x,y = datasets.make_regression(n_samples=200,n_features=1,noise=40)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x,y)

print("回帰係数は",e.coef_,"です。")
print("切片は",e.intercept_,"です。")

y_pred = e.predict(x_test)

print("学習データの決定係数は",e.score(x_train,y_train),"です。")
print("テストデータの決定係数は",e.score(x_test,y_test),"です。")

plt.scatter(x_train,y_train,label="train")
plt.scatter(x_test,y_test,label="test")
plt.plot(x_test,y_pred,color="m")
plt.legend()
plt.show()

from sklearn import cluster

np.random.seed(2)
data,label = datasets.make_blobs(n_samples=5000,n_features=2,centers=10,cluster_std=100)

e = cluster.KMeans(n_clusters=10)
e.fit(data)

print(e.labels_)
print(e.cluster_centers_)

plt.scatter(data[:,0],data[:,1],marker="o",c=e.labels_,edgecolor="k")
plt.scatter(e.cluster_centers_[:,0],e.cluster_centers_[:,1],marker="x")
plt.show()