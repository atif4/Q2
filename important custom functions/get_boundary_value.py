def get_boundary_value(list_c_ids):
    for list_c_id in list_c_ids:
        print('\n',list_c_id.upper())
        global  upper_limmite, lower_limmite
        upper_limmite = df[list_c_id].mean() + 3*df[list_c_id].std()
        lower_limmite = df[list_c_id].mean() - 3*df[list_c_id].std()
        print('Highest Allow',list_c_id.upper(),upper_limmite)
        print('Lowest Allow',list_c_id.upper(),lower_limmite)