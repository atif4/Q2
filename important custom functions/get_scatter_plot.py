def get_scatter_plot(x, y, xlabel, ylabel, title):
    df.plot(kind = 'scatter',x = x, y = y,alpha = 0.5, color = 'red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)