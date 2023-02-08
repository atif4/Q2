def get_model_fit(X_train_id, y_train_id):
    #model.fit(only take train variables of X and  y)
    return logR.fit(X_train_id,y_train_id)
#this is the example 
#get_model_fit(X_train,y_train)