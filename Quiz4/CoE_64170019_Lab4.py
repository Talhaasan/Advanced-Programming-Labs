import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([31, 32, 33, 49, 53, 69, 101, 109, 120, 132, 141]).reshape((-1, 1))
Y = np.array([540, 650, 705, 840, 850, 890, 900, 1150, 1200, 1550, 1700])

#a
regression = LinearRegression()
regression.fit(X, Y)
print('r_value :', regression.score(X, Y))
print('intercept :', regression.intercept_)
print('slope :', regression.coef_)

#b
Y_pred = regression.intercept_ + regression.coef_ * X
print('predicted y values:', Y_pred)

#c
plt.scatter(X,Y,color='red')
plt.plot(X,Y_pred, color='blue')
plt.show()