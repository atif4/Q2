def get_replace_col_values(col_id,val1,val2):
    df[col_id].replace({val1:1, val2:0},inplace=True)