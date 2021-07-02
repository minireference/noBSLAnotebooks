def cells():
    '''
    # 3/ Problem solutions
    '''

    '''
    '''

    from sympy import *
    init_printing()

    '''
    '''


    '''
    '''

    '''
    ## P3.1
    '''

    '''
    '''

    AUG = Matrix([
        [1, 5,   25],
        [2, 1,   32]])
    AUG

    '''
    '''

    AUG.rref()

    '''
    '''


    '''
    '''

    '''
    ## P3.2
    
    In the above solution we showed how to build `AUG` matrix directly.
    This time, we'll build `AUG` by row-joining (`row_join`) a matrix of coefficients and a vector of constants.
    '''

    '''
    '''

    A = Matrix([
        [3,       3],
        [2,  S(3)/2]])
    A

    '''
    '''

    b = Matrix([6,5])  # b is a column vector
    b

    '''
    '''

    # row-join A and b to obtain the augmented matrix
    AUG = A.row_join(b)
    AUG

    '''
    '''

    '''
    ### a) Alice
    
    Let's obtain the matrix `AUGA` which is the result after Alice's row operation.
    '''

    '''
    '''

    AUGA = AUG.copy()  # make a copy of AUG
    AUGA[0,:] = AUGA[0,:]/3
    AUGA

    '''
    '''

    AUGA[1,:] = AUGA[1,:] - 2*AUGA[0,:]
    AUGA

    '''
    '''

    AUGA[1,:] = -2*AUGA[1,:]
    AUGA

    '''
    '''

    AUGA[0,:] = AUGA[0,:] - AUGA[1,:]
    AUGA

    '''
    '''

    '''
    ### b) Bob
    '''

    '''
    '''

    AUGB = AUG.copy()
    AUGB[0,:] = AUGB[0,:] - AUGB[1,:]
    AUGB

    '''
    '''

    AUGB[1,:] = AUGB[1,:] - 2*AUGB[0,:]
    AUGB

    '''
    '''

    AUGB[1,:] = -1*S(2)/3*AUGB[1,:]
    AUGB

    '''
    '''

    AUGB[0,:] = AUGB[0,:] - S(3)/2*AUGB[1,:]
    AUGB

    '''
    '''


    '''
    '''

    '''
    ### c) Charlotte
    '''

    '''
    '''

    AUGC = AUG.copy()
    AUGC[0,:], AUGC[1,:] = AUGC[1,:], AUGC[0,:]
    AUGC

    '''
    '''

    AUGC[0,:] = AUGC[0,:]/2
    AUGC

    '''
    '''

    AUGC[1,:] = AUGC[1,:] - 3*AUGC[0,:]
    AUGC

    '''
    '''

    AUGC[1,:] = S(4)/3*AUGC[1,:]
    AUGC

    '''
    '''

    AUGC[0,:] = AUGC[0,:] - S(3)/4*AUGC[1,:]
    AUGC

    '''
    '''


    '''
    '''

    '''
    ## P3.3
    '''

    '''
    '''

    # define agmented matrices for three systems of eqns. with unique sol'ns
    AUGA = Matrix([
            [ -1, -2, -2],
            [  3, 3, 0]])
    
    AUGB = Matrix([
            [ 1, -1, -2,  1],
            [-2,  3,  3, -1],
            [-1,  0,  1,  2]])
    
    AUGC = Matrix([
            [ 2, -2,  3, 2],
            [ 1, -2, -1, 0],
            [-2,  2,  2, 1]])

    '''
    '''

    AUGA

    '''
    '''

    AUGA.rref()

    '''
    '''

    AUGB

    '''
    '''

    AUGB.rref()

    '''
    '''

    AUGC

    '''
    '''

    AUGC.rref()

    '''
    '''


    '''
    '''

    '''
    ## P3.4
    
    These three systems of equations have infinitely many solutions.
    '''

    '''
    '''

    '''
    ### P3.4 a)
    '''

    '''
    '''

    AUGA = Matrix([
        [ -1, -2,  -2],
        [  3,  6,   6]])
    AUGA

    '''
    '''

    AUGA.rref()

    '''
    '''

    AUGA[0:2,0:2].nullspace()

    '''
    '''

    # the solutions to the sytem of equations represented by AUGA
    # is of the form    point + nullspace
    point = AUGA.rref()[0][:,2]
    nullspace = AUGA[0:2,0:2].nullspace()

    '''
    '''

    # the point is also called he particular solution
    point

    '''
    '''

    # if the augmented matrix AUGA is [A|b], then the point satisfies A*point = b
    print( AUGA[0:2,0:2]*point == AUGA[:,2] )
    AUGA[0:2,0:2]*point

    '''
    '''

    '''
    #### Finding the null space
    '''

    '''
    '''

    # the nullspace of A is one dimensional and spanned by
    n = nullspace[0]
    n
    # every vector n in the nullspace of A satisfies  A*n=0

    '''
    '''

    # so solution to A*x=b is any (point+s*n) where s is any real number
    # since  A*(point+s*n) = A*point + sA*n = A*point + 0 = b.
    # Let's verify claim for values of s in the range -5,-4,-3,-2,-1,0,1,2,3,4,5
    for s in range(-5,6):
        print( AUGA[0:2,0:2]*(point + s*n), 
               AUGA[0:2,0:2]*(point + s*n) == AUGA[:,2] )

    '''
    '''

    '''
    ### P3.4 b)
    '''

    '''
    '''

    AUGB = Matrix([
            [ 1, -1, -2,   1],
            [-2,  3,  3,  -1],
            [-1,  2,  1,   0]])
    AUGB

    '''
    '''

    AUGB.rref()

    '''
    '''

    point_B = AUGB.rref()[0][:,3]
    nullspace_B = AUGB[0:3,0:3].nullspace()[0]
    s = symbols('s')
    point_B + s*nullspace_B

    '''
    '''

    '''
    ### P3.4 c)
    '''

    '''
    '''

    AUGC = Matrix([
            [ 2, -2, 3,  2],
            [ 0,  0, 5,  3],
            [-2,  2, 2,  1]])
    AUGC

    '''
    '''

    AUGC.rref()

    '''
    '''

    constants = AUGC.rref()[0][:,3]
    
    # construct point_C by placing the constants into the location of the pivots
    pivots = AUGC.rref()[1]
    point_C = zeros(3,1)
    for idx, pivot in enumerate(pivots):
        point_C[pivot] = constants[idx]
    
    nullspace_C = AUGC[0:3,0:3].nullspace()[0]
    s = symbols('s')
    point_C + s*nullspace_C

    '''
    '''


    '''
    '''

