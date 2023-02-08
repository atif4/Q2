#if required
def get_replace_col_values(col_id,val1,val2):
    df[col_id].replace({val1:'male', val2:'female'},inplace=True)