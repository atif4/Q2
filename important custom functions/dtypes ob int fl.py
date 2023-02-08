def get_each_dtpyes(col_list):
    ob = []
    integer = []
    fl = []
    data_time = []
    for i in col_list:
        if df[i].dtypes == 'object':
            ob.append(i)
        if df[i].dtypes == 'int64':
            integer.append(i)
        if  df[i].dtypes == 'float64':
            fl.append(i)
        if df[i].dtypes == 'datetime64[ns]':
            data_time.append(i)
    return print(f"list of object dtpyes:\n{ob}\n\nlist of integers dtypes:\n{integer}\n\nlist of float dtypes:\n{fl}\n\nlist of datatime dtype:\n{data_time}")
get_each_dtpyes(['user_name', 'user_location', 'user_description', 'user_created','user_followers', 'user_friends',
                 'user_favourites', 'user_verified', 'date', 'text', 'hashtags', 'source', 'is_retweet'])