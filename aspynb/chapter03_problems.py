def cells():
    '''
    ## Chapter 3 problems
    '''

    '''
    '''

    from sympy import *
    init_printing()

    '''
    '''


    '''
    '''

    A = Matrix([
    [3,     3],
    [2, S(3)/2]])
    A

    '''
    '''

    b = Matrix([6,5])

    '''
    '''

    AUG = A.row_join(b)
    AUG # the augmented matrix

    '''
    '''

    '''
    ### Alice
    '''

    '''
    '''

    AUGA = AUG.copy()
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
    ### Bob
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
    ### Charlotte
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
    ### P3.3
    '''

    '''
    '''

    # define agmented matrices for three systems of eqns. with unique sol'ns
    A = Matrix([
            [ -1, -2, -2],
            [  3, 3, 0]])
            
    B = Matrix([
            [ 1, -1, -2,  1],
            [-2,  3,  3, -1],
            [-1,  0,  1,  2]])
    
    C = Matrix([
            [ 2, -2,  3, 2],
            [ 1, -2, -1, 0],
            [-2,  2,  2, 1]])

    '''
    '''

    A

    '''
    '''

    A.rref()

    '''
    '''

    B

    '''
    '''

    B.rref()

    '''
    '''

    C

    '''
    '''

    C.rref()

    '''
    '''

    '''
    ### P3.4
    '''

    '''
    '''

    # now for three systems of eqns. with infinitely many sol'ns
    D = Matrix([
            [ -1, -2, -2],
            [  3, 6,   6]])
            
    E = Matrix([
            [ 1, -1, -2,  1],
            [-2,  3,  3, -1],
            [-1,  2,  1,  0]])
    
    F = Matrix([
            [ 2, -2, 3, 2],
            [ 0,  0, 5, 3],
            [-2,  2, 2, 1]])

    '''
    '''

    '''
    ### Solving d)
    '''

    '''
    '''

    D

    '''
    '''

    D.rref()

    '''
    '''

    D[0:2,0:2].nullspace()

    '''
    '''

    # the solutions to the sytem of equations represented by D
    # is of the form    point + nullspace
    point = D.rref()[0][:,2]
    nullspace = D[0:2,0:2].nullspace()

    '''
    '''

    # the point is also called he particular solution
    point

    '''
    '''

    # if A aug matrix is [A|b], then the point satisfies A*point = b.
    print( D[0:2,0:2]*point == D[:,2] )
    D[0:2,0:2]*point

    '''
    '''

    '''
    ### Null space
    '''

    '''
    '''

    # the nullspace of A in aug. matrix [A|b] is one dimensional and spanned by
    n = nullspace[0]
    n
    # every vector n in the nullspace of A satisfies  A*n=0

    '''
    '''

    # so solution to A*x=b is any (point+s*n) where s is any real number
    # since  A*(point +s*n) = A*point + sA*n = A*point + 0 = b.
    # verify claim for 20 values of s in range -5,-4,-3,-2,-1,0,1,2,3,4,5
    for s in range(-5,6):
        print( D[0:2,0:2]*(point + s*n), 
               D[0:2,0:2]*(point + s*n) == D[:,2] )

    '''
    '''

    '''
    ### Solving e)
    '''

    '''
    '''

    E

    '''
    '''

    E.rref()

    '''
    '''

    point_E = E.rref()[0][:,3]
    nullspace_E = E[0:3,0:3].nullspace()[0]
    s = symbols('s')
    point_E + s*nullspace_E

    '''
    '''

    '''
    ### Solving f)
    '''

    '''
    '''

    F

    '''
    '''

    F.rref()

    '''
    '''

    point_F = F.rref()[0][:,3]
    nullspace_F = F[0:3,0:3].nullspace()[0]
    s = symbols('s')
    point_F + s*nullspace_F

    '''
    '''


    '''
    '''

