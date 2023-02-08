def get_classification_report(y_t, y_p):
    # in classification_report only takes y_test and y_prediction variables to give the report
    return print(classification_report(y_t, y_p))
#this is example 
#get_classification_report(y_test,y_pred)