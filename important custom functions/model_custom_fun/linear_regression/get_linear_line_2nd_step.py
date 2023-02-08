def get_linear_line(xlbl,ylbl,title):
    x_max = np.max(X)+100
    x_min = np.min(X)-100
    #calculatING the line va;ue of x and y 
    #x_max is starting point and x_min is ending point number of items = 1000 or 100 or 50
    x = np.linspace(x_max, x_min, 1000)
    y = m*x + c 
    #this is for line
    plt.plot(x,y,color='red', label="RL")
    plt.scatter(X,Y,color='blue',label='scatter')
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.title(title)
    plt.legend()
    plt.show()