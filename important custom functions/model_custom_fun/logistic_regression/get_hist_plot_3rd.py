def get_hist_plot(df_id, c_id, hue='gender', kde=True, line_kws = {'color':'red','linestyle': 'dashed'},pal="rocket",alpha=1.0):
    sns.histplot(data=df_id, x=c_id, hue=hue, kde=True, line_kws=line_kws,palette=pal,alpha=alpha,)