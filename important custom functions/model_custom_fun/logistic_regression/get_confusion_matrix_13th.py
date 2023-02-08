def get_confusion_matrix(y_test_id, y_pred_id):
    # in confusion_matrix_plot only takes y_test and y_prediction variables to get the metrix
    return confusion_matrix(y_test_id,y_pred_id)
#this is example 
#get_confusion_matrix(y_test,y_pred)