def cells():
    '''
    # 3/ Exercises solutions
    '''

    '''
    '''

    # helper code needed for running in colab
    if 'google.colab' in str(get_ipython()):
        print('Downloading plot_helpers.py to util/ (only neded for colab')
        !mkdir util; wget https://raw.githubusercontent.com/minireference/noBSLAnotebooks/master/util/plot_helpers.py -P util

    '''
    '''

    from sympy import *
    init_printing()
    
    %matplotlib inline
    import matplotlib.pyplot as mpl
    from util.plot_helpers import plot_augmat # helper function

    '''
    '''

    '''
    ## RREF exercises
    '''

    '''
    '''

    '''
    ### E3.1
    '''

    '''
    '''

    AUG = Matrix([
      [3,      3,  6],
      [2, S(3)/2,  5]])
    AUG

    '''
    '''

    AUG.rref()
    # solution is x=4, y=-2

    '''
    '''

    '''
    ### Verify the solution geometrically
    '''

    '''
    '''

    AUG = Matrix([
      [3,      3,   6],
      [2, S(3)/2,   5]])
    
    fig = mpl.figure()
    plot_augmat(AUG)
    # the solution (4,-2) is where the two lines intersect

    '''
    '''

    '''
    ### E3.2
    '''

    '''
    '''

    A = Matrix([
             [3,      3,   6],
             [2, S(3)/2,   5]])
    A

    '''
    '''

    # First row operation:  R1  <-- 1/3*R1
    A[0,:] = A[0,:]/3
    A

    '''
    '''

    # Second row operation:  R2  <-- R2 - 2*R1
    A[1,:] = A[1,:] - 2*A[0,:]
    A

    '''
    '''

    # Third row operation:  R2  <-- -2*R2
    A[1,:] = -2*A[1,:]
    A

    '''
    '''

    # Fourth row operation:  R1  <-- R1 - R2
    A[0,:] = A[0,:] - A[1,:]
    A

    '''
    '''

    '''
    ### E3.3
    '''

    '''
    '''

    AUGA = Matrix([
     [3, 3,   6],
     [1, 1,   5]])
    AUGA.rref()
    # no solutions since second row   0x+0y == 1  is impossible

    '''
    '''

    # verify geomtetrically
    AUGA = Matrix([
     [3, 3,   6],
     [1, 1,   5]])
    
    fig = mpl.figure()
    plot_augmat(AUGA)
    # no solution since lines two lines are parallel

    '''
    '''


    '''
    '''

    AUGB = Matrix([
      [3,      3,    6],
      [2, S(3)/2,    3]])
    AUGB.rref()
    # one solution x=0, y=2

    '''
    '''

    # verify geomtetrically
    AUGB = Matrix([
      [3,      3,   6],
      [2, S(3)/2,   3]])
    
    fig = mpl.figure()
    plot_augmat(AUGB)
    # the solution (0,2) is where the two lines intersect

    '''
    '''

    AUGC = Matrix([
      [3, 3,  6],
      [1, 1,  2]])
    AUGC.rref()
    # infinitely many soln's of the form  point + s*dir, for s in \mathbb{R}

    '''
    '''

    # to complete the solution,
    # observe the second column is a free varible y = s 
    # and thus we have these equations:
    #   x +  s = 2
    #  0x + 0s = 0   (trivial eqn.)
    #        y = s   (def'n of free variable)
    # thus solution is:
    #      [x,y]  =  [2-s,s]  =  [2,0] + s*[-1,1]     for s in \mathbb{R}

    '''
    '''

    # verify geomtetrically
    AUGC = Matrix([
      [3, 3,  6],
      [1, 1,  2]])
    
    fig = mpl.figure()
    plot_augmat(AUGC)
    # the solution is infinite since two lines are the same

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Matrix equations
    '''

    '''
    '''


    '''
    '''


    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Matrix product
    '''

    '''
    '''

    '''
    ### E3.5
    
    Compute the following matrix products:
    $$
    P = 
    \begin{bmatrix} 	1&2 \\   3&4  \end{bmatrix}
    \begin{bmatrix} 	5&6 \\   7&8  \end{bmatrix}
    \quad
    \textrm{and}
    \quad
    Q = 
    \begin{bmatrix}	
    3& 1 &  2&  2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}\!\!		% 
    \begin{bmatrix}
        -2 &  3 \\  
        \ \ 1 &  0 \\  
        -2 & \!\!-2 \\  
        \ \ 2 &  2 
      \end{bmatrix}\!.
    $$
    '''

    '''
    '''

    # define matrices
    P1 = Matrix([
        [1, 2],
        [3, 4]])
    P2 = Matrix([
        [5, 6],
        [7, 8]])
    
    # compute product
    P = P1*P2
    P

    '''
    '''

    # define matrices
    Q1 = Matrix([[3, 1,  2, 2],
                 [0, 2, -2, 1]])
    Q2 = Matrix([[-2,  3],
                 [ 1,  0],
                 [-2, -2],
                 [ 2,  2]])
    
    # compute product
    Q = Q1*Q2
    Q

    '''
    '''

    '''
    ## Determinants
    '''

    '''
    '''


    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Matrix inverse
    '''

    '''
    '''


    '''
    '''

