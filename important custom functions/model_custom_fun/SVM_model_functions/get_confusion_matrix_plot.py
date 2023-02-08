def get_plot_confusion_matrix(model_id, x_test_id, y_test_id,cmap_id):
    #plot_confusion_matrix take necessary 3 parameters such as model_name, x_test, y_test. without this you will get error  
    return plot_confusion_matrix(model_id, x_test_id, y_test_id,cmap=cmap_id)