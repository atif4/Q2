def get_dummies(df_id,c_id,new_df_id):
    new_df_id = pd.get_dummies(df_id[c_id],drop_first=True)
    return new_df_id
#this is example , in this way you can get your dummies dataset 
""""
race = get_dummies(df,'race/ethnicity',new_df_id="race")
race.head()
"""