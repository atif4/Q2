#Separate Feature and Target Matrix
def get_seprate_features(df_id,col_id):
    #col_id is special col or target col b/c this the whole model is going to be created 
    global X, y
    X = df_id.drop(col_id,axis = 1) 
    y = df_id[col_id]