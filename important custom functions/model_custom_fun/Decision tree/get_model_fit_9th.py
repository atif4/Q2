dt = DecisionTreeClassifier()
def get_model_fit(X_train_id, y_train_id, model_id):
    #model.fit(only take train variables of X and  y)
    return model_id.fit(X_train_id,y_train_id)