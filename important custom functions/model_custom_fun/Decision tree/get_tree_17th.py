def get_tree():
    fn = ["Age Range", "Head Size(cm^3)","Brain Weight(grams)"]
    cln = ['male','female']
    fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (4,4), dpi = 500)
    tree.plot_tree(dt,
              feature_names = fn,
              class_names = cln,
              filled = True);
    fig.savefig('imagename.png')