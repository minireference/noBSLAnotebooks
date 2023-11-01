def cells():
    '''
    # 7/ Exercises solutions
    '''

    '''
    '''

    # setup SymPy
    from sympy import *
    init_printing()

    '''
    '''

    '''
    ### E7.3
    '''

    '''
    '''

    # The external demand is
    d = Matrix(
        [100,   # arugula
         200,   # broccoli
         300])  # carrots (in tons)

    '''
    '''

    # The internal demands of production are describe by
    A = Matrix([
    [    0,   0.1,   0.1],
    [ 0.01,     0,  0.15],
    [ 0.01,  0.20,     0]])

    '''
    '''

    # The required production rates for both internal and external demands:
    x = (eye(3)-A).inv()*d
    x

    '''
    '''


    '''
    '''


    '''
    '''

