from sklearn.svm import SVC #Import svm model
svm = SVC()
def get_model_fit(X_train_id, y_train_id,model_id):
    #model.fit(only take train variables of X and  y)
    accuracies = {}
    model_id.fit(X_train_id,y_train_id)
    acc = model_id.score(X_train_id,y_train_id)*100
    accuracies['SVM'] = acc
    return accuracies