def get_missing_values_col(list_col):
    not_missing_col_list = []
    missing_col_list = []
    for i in list_col:
        if df[i].isnull().sum() == 0:
            not_missing_col_list.append(i)
        if df[i].isnull().sum() != 0:
            missing_col_list.append(i)
    return print(f"This\These column(s) does\do not have missing value(s):\n {not_missing_col_list}\n\nThis\These column(s) do\does have some missing values:\n{missing_col_list}")

get_missing_values_col(['user_name', 'user_location', 'user_description', 'user_created','user_followers', 'user_friends', 
               'user_favourites', 'user_verified','date', 'text', 'hashtags', 'source', 'is_retweet'])


def get_dtpye_of_missing_values(col_list):
    list_dtype=[]
    for i in col_list:
        result = i,df[i].dtypes
        list_dtype.append(result)
    return list_dtype
get_dtpye_of_missing_values(missing_col_list)