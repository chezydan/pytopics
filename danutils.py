import matplotlib.pyplot as plt

def generic(x):
    return 3 * x


def tableArrays (X,Y):
    '''show x and y arrays on a table'''
    DEFAULTVALUE=-9999.9999
    intercept,y0at= [DEFAULTVALUE ]*2
    row_format= "{:>6}{:>6}"
    print(row_format.format("X","Y"))
    for x,y in zip(X,Y):
        if x ==0:
            intercept= y
        if y ==0:
            y0at= x
        
        print(row_format.format(x,y  ))
        
    if intercept != DEFAULTVALUE:
        print("intercept: {:}".format(intercept))
    minX= min(X)
    print(min(X))
        

def plotFunc(X,Y,adjust=True):
    '''plots function assumes len(X) == len(Y)'''
   
    plt.figure(figsize=(8,4))
    plt.plot(X,Y)
    if adjust:
        plt.axis( [min(min(Y),min(X)),max(max(Y),max(X)) ,min(min(Y),min(X)),max(max(Y),max(X))])

    plt.axhline(color='gray')
    plt.axvline(color='gray')
    
    plt.show()
        
        
def genX (start=-10,stop=10,step=1):
    '''generates a list for an X'''
    return [x for x in range (start,stop,step)]    
    