def get_precision_recall(y_test_id,y_pred_id,pos_label_id):
    #calculating precision and reall
    global precision, recall, f1
    precision = precision_score(y_test_id,y_pred_id,pos_label=pos_label_id)
    recall = recall_score(y_test_id,y_pred_id,pos_label=pos_label_id)
    f1 = f1_score(y_test,y_pred,pos_label=pos_label_id)
    return "precision score of "+pos_label_id+": "+str(precision),"recall score of "+pos_label_id+": "+str(recall),"f1_score of "+pos_label_id+": "+str(f1)