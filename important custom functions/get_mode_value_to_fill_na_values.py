def get_mode_value_to_fill_na_values(col_list):
    global list_of_mode
    list_of_mode = []
    for i in col_list:
        result = df[i].mode()
        list_of_mode.append(result)
    #return list_of_mode
get_fill_missing_values(missing_col_list)