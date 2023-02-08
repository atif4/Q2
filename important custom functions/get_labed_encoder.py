from sklearn.preprocessing import LabelEncoder
def get_labed_encoder(col_ids_list):
    global new_df
    for col_id_list in col_ids_list:
        df[col_id_list] = df[col_id_list].apply(LabelEncoder().fit_transform)
        new_df = df.copy()
get_labed_encoder([['gender','race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']])