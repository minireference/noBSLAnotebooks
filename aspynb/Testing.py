def cells():
    '''
    # Testing SymPy and plot helpers are working
    '''

    '''
    '''

    # setup SymPy
    from sympy import *
    x, y, z, t = symbols('x y z t')
    init_printing()
    
    # download plot_helpers.py for use in colab
    if 'google.colab' in str(get_ipython()):
        print('Downloading plot_helpers.py to util/ (only neded for colab')
        !mkdir util; wget https://raw.githubusercontent.com/minireference/noBSLAnotebooks/master/util/plot_helpers.py -P util
    
    # setup plotting
    %matplotlib inline
    import matplotlib.pyplot as mpl
    from util.plot_helpers import plot_vec, plot_vecs, autoscale_arrows

    '''
    '''

    # check if SymPy knows how to simplify trig expressions
    simplify(sin(2*x)*cos(2*x))

    '''
    '''

    # define a column vector a
    a = Matrix([1,1,1])
    a

    '''
    '''

    # BAD define the floating point number approximation 1/3
    1/3

    '''
    '''

    # define the fraction 1/3 (an exact rational number)
    S(1)/3

    '''
    '''

    # The S()-stuff is necessary to avoid Python behaviour,
    # which is to treat 1/3 as a floating point number:
    type(1/3)

    '''
    '''

    type(S(1)/3)

    '''
    '''


    '''
    '''

    # obtain numeric approximation (as a float)
    N(S(1)/3)

    '''
    '''

    # N, .n(), and .evalf() are equivalent ways to obtain numeric approx:
    N((S(1)/3)), (S(1)/3).n(), (S(1)/3).evalf()

    '''
    '''

    # the .n() method allows for arbitrary level precisions
    pi.n(100)

    '''
    '''

    # Euler's constant
    E

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Plot helpers
    '''

    '''
    '''

    # vector defined as a Python list
    u = [1,2]
    plot_vec(u)
    autoscale_arrows()

    '''
    '''

    # vector defined as a SymPy 2x1 Matrix (a column vector)
    v = Matrix([1,2])
    plot_vec(v)
    autoscale_arrows()

    '''
    '''


    '''
    '''

