#viz
def get_countplot(col_id, df_id,hu= "gender",pal="mako_r",figsize=(6,4)):
    #the parameter in which values are can be change at any time
    plt.figure(figsize=figsize)
    sns.countplot(x=col_id, data=df_id,hue=df_id[hu].sort_values(),palette=pal)
    plt.show()