def get_xy_mean_value(c_id1,c_id2):
    global X, Y, x_mean, y_mean, n
    X = df[c_id1].values
    Y = df[c_id2].values
    x_mean = np.mean(X)
    y_mean = np.mean(Y)
    n = len(X)
    #return X, Y, x_mean, y_mean, n