from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def get_r_square():
    #it is array for n_numbers_of_x and dimension is 1
    X_re = X.reshape((n,1))
    reg = LinearRegression()
    reg_fit = reg.fit(X_re,Y)
    Y_pred = reg.predict(X_re)
    r2_score = reg.score(X_re,Y)
    return r2_score