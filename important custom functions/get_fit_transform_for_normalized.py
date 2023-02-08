scaler = StandardScaler()
def get_fit_transform(metric):
    global X
    X = scaler.fit_transform(metric)
    return X
get_fit_transform(X)