def get_prediction(x_test_id,model_id):
    global y_pred
    #to get the Prediction of y you have to give X_test variable
    y_pred = model_id.predict(x_test_id)