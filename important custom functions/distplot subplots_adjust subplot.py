plt.figure(1 , figsize = (15 , 3))
n = 0 
for x in ['Store_Area', 'Items_Available', 'Daily_Customer_Count','Store_Sales']:
    n += 1
    plt.subplot(1 , 4 , n)
    plt.subplots_adjust(hspace =0.4 , wspace = 0.4)
    sns.distplot(df[x] , bins = 20)
    plt.title('Distplot of {}'.format(x))
plt.show()