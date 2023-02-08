def get_normalize():
    df.iloc[:,1:3] = (df-df.min())/ (df.max() - df.min())
    return df.head()
get_normalize()