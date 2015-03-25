
"""
Demonstration module for quadratic interpolation.
Docstring updated for new points
Modified by: ** Srikanth Narayanan **
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

def poly_interp(xi,yi):
    """
    Interpolation implementation of polynomial.
    Compute the coefficients of the polynomial and returns and array c with the
    results.
    
    :param xi: a numpy array of length n
    :param yi: a numpy array of same length as xi
    """
    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message
    
    error_message = "xi and yi should have equal length"
    assert len(xi) == len(yi), error_message
    
    # Set up linear system to interpolate through data points:
    # co-efficient matrix for the system
    A = np.ones((len(xi),len(xi)))
    for i in range(1,len(xi)):
        A[:,i] = A[:,i] * (xi**i)
    b = yi
    
    ### compute c ###
    c = solve(A,b)
    
    return c
    
def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.

    """
    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:
    # co-efficient matrix for the system
    A = np.ones((3,3))
    A[:,1] = A[:,1] * xi
    A[:,2] = A[:,2] * (xi**2)
    b = yi
	
    ### compute c ###
    c= solve(A,b)

    return c

def plot_quad(xi, yi):
    """
    A function to calculate and plot the quadratic interpolation of give array xi and yi.
    Save the resulting plot in to quadratic.png.
    """
    # check inputs and print error message if not valid:
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message
    
    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message
    	
    # calculate the co-efficients of the polynomial
    c = quad_interp(xi,yi)
    
    # plot the resulting polynomial
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2
    
    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line
    
    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(yi.min() - 1,yi.max() + 1)         # set limits in y for plot
    
    plt.title("Data points and interpolating polynomial")
    
    plt.savefig('hw2b.png')   # save figure as .png file

def cubic_interp(xi,yi):
    """
    A method to perform cubic interpolation.
    Returns c, an array containing the coefficients of
    p(x) = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3
    
    :param xi: A numpy one dimensional array of length atleast 4
    :param yi: A numpy one dimentional array of length atleast 4
    """
    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message
    
    # Set up linear system to interpolate through data points:
    # co-efficient matrix for the system
    A = np.vstack([np.ones((4)), xi, xi**2, xi**3])
    b = yi
    
    ### compute c ###
    c = solve(A,b)
    
    return c

def plot_cubic(xi,yi):
    """
    This function accepts a set of xi and yi as input points to create a cubic
    spline and plots the image of the spline.
    
    :param xi: A numpy one dimensional array of length atleast 4
    :param yi: A numpy one dimentional array of length atleast 4
    """
    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message
    
    # calculate the co-efficients of the polynomial
    c = cubic_interp(xi,yi)
    print c
    
    # plot the resulting polynomial
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3
    
    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line
    
    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(yi.min() - 1,yi.max() + 1)         # set limits in y for plot
    
    plt.title("Data points and interpolating cubic polynomial")
    
    plt.savefig('cubic.png')   # save figure as .png file

def plot_poly(xi,yi):
    """
    This function accepts a set of xi and yi as input points to create a cubic
    spline and plots the image of the spline.
    
    :param xi: A numpy one dimensional array of length n
    :param yi: A numpy one dimentional array of length same as xi
    """
    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have equal length"
    assert len(xi) == len(yi), error_message
    
    # calculate the co-efficients of the polynomial
    c = poly_interp(xi,yi)
    print c
    
    # plot the resulting polynomial
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    #applying horners rule to get y value
    #http://www.math10.com/en/algebra/horner.html
    n = len(c)
    y = c[n-1]
    for j in range(n-1, 0, -1):
        y = y*x + c[j - 1]
    
    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line
    
    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(yi.min() - 1,yi.max() + 1)         # set limits in y for plot
    
    plt.title("Data points and interpolating polynomial")
    
    plt.savefig('polynomial.png')   # save figure as .png file

def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1.,  0.,  2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)
        
if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    test_quad1()

