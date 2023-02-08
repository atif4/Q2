class Viz_data():
    def __init__(self, df):
        """Initialize name and age attributes."""
        self.df = pd.read_csv(df)
        
    def get_drop_col(self,c_id):
        self.df.drop([c_id],axis=1,inplace=True)
        
    def get_graph(self,title,f_name):
        # a scatter plot comparing num_children and num_pets
        plt.figure(figsize=(10,7))
        plt.xticks(rotation =45)
        plt.title(title)
        plot_info = sns.barplot(x = 'Data' , y = 'score' ,data = self.df)
        #dots per inch = dpi
        """The keyword argument dpi= specifies how many dots per inch (image resolution) are in the saved image. 
        dpi=72 is fine for web images.dpi=300 is better for an image designed to go in a written report or .pdf document
        The keyword argument bbox_inches='tight' is optional. If the axis labels in the plot are cut off in the saved image,
        set bbox_inches='tight'"""
        plt.savefig(f_name, dpi=300, bbox_inches='tight')
        plt.show()