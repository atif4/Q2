def get_pair_plot(df_id,hue_id):
    sns.pairplot(data= df_id,hue=hue_id)
    plt.show()