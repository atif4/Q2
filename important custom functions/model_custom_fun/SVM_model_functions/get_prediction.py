def get_prediction(x_test_id):
    global y_pred
    #to get the Prediction of y you have to give X_test variable
    y_pred = logR.predict(x_test_id)
    return y_pred