def cells():
    '''
    # 2/ Definitions
    '''

    '''
    '''

    # helper code needed for running in colab
    if 'google.colab' in str(get_ipython()):
        print('Downloading plot_helpers.py to util/ (only neded for colab')
        !mkdir util; wget https://raw.githubusercontent.com/minireference/noBSLAnotebooks/master/util/plot_helpers.py -P util

    '''
    '''

    # setup SymPy
    from sympy import *
    x, y, z, t = symbols('x y z t')
    init_printing()
    
    # setup plotting
    %matplotlib inline
    import matplotlib.pyplot as mpl
    from util.plot_helpers import plot_vec, plot_vecs, autoscale_arrows

    '''
    '''

    '''
    ## SymPy Matrix objects
    '''

    '''
    '''

    v = Matrix([1,2,3])
    v

    '''
    '''

    # define symbolically
    v_1, v_2, v_3 = symbols('v_1 v_2 v_3')
    v = Matrix([v_1,v_2,v_3])

    '''
    '''

    v

    '''
    '''

    v.T

    '''
    '''

    A = Matrix(
        [   [1,7],
            [2,8], 
            [3,9]   ])
    A

    '''
    '''

    # define symbolically
    a_11, a_12, a_21, a_22, a_31, a_32 = symbols('a_11 a_12 a_21 a_22 a_31 a_32')
    A = Matrix([
            [a_11, a_12],
            [a_21, a_22], 
            [a_31, a_32]])

    '''
    '''

    A

    '''
    '''

    '''
    ## Vector operations
    '''

    '''
    '''

    u_1, u_2, u_3 = symbols('u_1 u_2 u_3')
    u = Matrix([u_1,u_2,u_3])
    v_1, v_2, v_3 = symbols('v_1 v_2 v_3')
    v = Matrix([v_1,v_2,v_3])
    alpha = symbols('alpha')
    
    u

    '''
    '''

    alpha*u

    '''
    '''

    u+v

    '''
    '''

    u.norm()

    '''
    '''

    uhat = u/u.norm()
    uhat

    '''
    '''

    u = Matrix([1.5,1])
    w = 2*u
    uhat = u/u.norm()
    
    fig = mpl.figure()
    plot_vecs(u, w, uhat)
    autoscale_arrows()

    '''
    '''

    '''
    ### Dot product
    '''

    '''
    '''

    u = Matrix([u_1,u_2,u_3])
    v = Matrix([v_1,v_2,v_3])
    
    u.dot(v)

    '''
    '''

    fig = mpl.figure()
    u = Matrix([1,1])
    v = Matrix([3,0])
    plot_vecs(u,v)
    autoscale_arrows()
    
    u_dot_v = u.dot(v)
    u_dot_v

    '''
    '''

    phi = acos( u.dot(v)/(u.norm()*v.norm()) )
    print('angle between u and v is', phi)
    u.norm()*v.norm()*cos(phi)

    '''
    '''

    '''
    ### Cross product
    '''

    '''
    '''

    u = Matrix([u_1,u_2,u_3])
    v = Matrix([v_1,v_2,v_3])
    
    u.cross(v)

    '''
    '''

    u = Matrix([1,0,0])
    v = Matrix([1,1,0])
    w = u.cross(v)      # a vector perpendicular to both u and v
    
    mpl.figure()
    plot_vecs(u, v, u.cross(v))

    '''
    '''

    print('length of cross product', w.norm())
    
    phi = acos( u.dot(v)/(u.norm()*v.norm()) )
    
    w.norm() == u.norm()*v.norm()*sin(phi)

    '''
    '''

    '''
    ## Projection operation
    '''

    '''
    '''

    def proj(vec, d):
        """Computes the projection of vector `vec` onto vector `d`."""
        return d.dot(vec)/d.norm() * d/d.norm()

    '''
    '''

    fig = mpl.figure()
    u = Matrix([1,1])
    v = Matrix([3,0])
    
    pu_on_v = proj(u,v)
    
    plot_vecs(u, v, pu_on_v)
    
    
    # autoscale_arrows()
    ax = mpl.gca()
    ax.set_xlim([-1,3])
    ax.set_ylim([-1,3])
    

    '''
    '''

    '''
    # Matrix operations
    '''

    '''
    '''

    a_11, a_12, a_21, a_22, a_31, a_32 = symbols('a_11 a_12 a_21 a_22 a_31 a_32')
    A = Matrix([
            [a_11, a_12],
            [a_21, a_22], 
            [a_31, a_32]])
    b_11, b_12, b_21, b_22, b_31, b_32 = symbols('b_11 b_12 b_21 b_22 b_31 b_32')
    B = Matrix([
            [b_11, b_12],
            [b_21, b_22], 
            [b_31, b_32]])
    alpha = symbols('alpha')

    '''
    '''

    A

    '''
    '''

    A + B

    '''
    '''

    alpha*A

    '''
    '''

    v_1, v_2 = symbols('v_1 v_2')
    v = Matrix([v_1,v_2])
    
    A*v

    '''
    '''

    A[:,0]*v[0] + A[:,1]*v[1]

    '''
    '''

    A = Matrix([
            [a_11, a_12],
            [a_21, a_22], 
            [a_31, a_32]])
    B = Matrix([
            [b_11, b_12],
            [b_21, b_22]])
    
    A*B

    '''
    '''

    A.T

    '''
    '''

    print('the shape of v is', v.shape)
    v

    '''
    '''

    print('the shape of v.T is', v.T.shape)
    v.T

    '''
    '''

    u = Matrix([u_1,u_2,u_3])
    v = Matrix([v_1,v_2,v_3])
    
    u.T*v

    '''
    '''

    u * v.T

    '''
    '''

    A = Matrix([
            [3,       3],
            [2,  S(3)/2]
    ])
    A

    '''
    '''

    A.inv()

    '''
    '''

    A * A.inv()

    '''
    '''

    A.inv() * A

    '''
    '''

    B = Matrix([
            [b_11, b_12],
            [b_21, b_22]])
    B

    '''
    '''

    B.trace()

    '''
    '''

    B.det()

    '''
    '''


    '''
    '''

