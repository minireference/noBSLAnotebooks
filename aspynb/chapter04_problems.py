def cells():

    '''
    '''

    from sympy import *
    init_printing()
    
    %matplotlib notebook
    import matplotlib.pyplot as mpl
    from util.plot_helpers import plot_augmat, plot_plane, plot_point, plot_line, plot_vec, plot_vecs
    
    Vector = Matrix  # define alias Vector so I don't have to explain this during video
    Point = Vector   # define alias Point for Vector since they're the same thing

    '''
    '''

    '''
    ## P4.11
    '''

    '''
    '''

    v = Vector([3, 4, 1])
    normal = Vector([2, -1, 4])
    
    vPperp = (normal.dot(v)/normal.norm()**2)*normal
    print('vPperp =', vPperp)
    vP = v - vPperp
    print('vP =', vP)
    
    plot_plane(normal, 0)            # plane P
    plot_vec(0.2*normal, color='r')  # its normal vec
    
    plot_vecs(v, vPperp, vP)

    '''
    '''

    v = Vector([3,   4,  1])
    normal = Vector([2,   -1,  4])
    D=4
    # point on P closest to the origin
    alpha = D/normal.norm()**2
    p_closest = alpha*normal
    # print('len normal', normal.norm())
    # print('p_closest', p_closest)
    assert p_closest.dot(normal) == 4
    
    
    vPperp = (normal.dot(v)/normal.norm()**2)*normal
    print('vPperp', vPperp)
    v_wrong = v - vPperp
    print('v_wrong', v_wrong)
    
    
    plot_plane(normal, D)                          # plane P
    plot_vec(0.2*normal, at=p_closest, color='r')  # its normal vec
    
    
    plot_vecs(v, vPperp, v_wrong)
    ax = mpl.gca()
    ax.grid(True,which='both')

    '''
    '''

    v = Vector([3,   4,  1])
    normal = Vector([2,   -1,  4])
    D=4
    
    # some point on P
    p0 = Point([2,0,0])
    
    u = v-p0  # vector from p0 to tip of v
    
    uPperp = (normal.dot(u)/normal.norm()**2)*normal
    print('uPperp', uPperp)
    uInP = u - uPperp
    
    proj_v_on_P = p0 + uInP
    print('proj_v_on_P', proj_v_on_P)
    
    
    plot_plane(normal, D)                          # plane P
    plot_vec(0.2*normal, at=p_closest, color='r')  # its normal vec
    
    plot_vec(v)
    plot_vec(u, at=p0, color='r')
    plot_vec(uPperp, at=p0, color='b')
    plot_vec(uInP, at=p0, color='g')
    plot_vec(proj_v_on_P, color='y')
    
    ax = mpl.gca()
    ax.grid(True,which='both')

    '''
    '''


    '''
    '''

