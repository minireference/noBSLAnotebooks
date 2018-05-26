def cells():
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
    ### E4.7
    '''

    '''
    '''

    p = Point([10,10,10])
    pL1 = Point([3,0,5])
    pL2 = Point([6,0,0])
    d = Vector([1,-2,0])
    
    # define a vector from a point on L1 to p:
    v1 = p - pL1
    # proj_{L1}(p) = proj_{L1}(v1) + pL1 
    p_proj_L1 = (d.dot(v1)/d.norm()**2)*d + pL1

    '''
    '''

    plot_line(d, pL1)
    plot_vec(d, at=pL1)
    plot_vec(v1, at=pL1)
    plot_vec((d.dot(v1)/d.norm()**2)*d, at=pL1)
    plot_vec(p_proj_L1)
    
    ax = mpl.gca()
    mpl.xlim([0,10])
    mpl.ylim([0,10])
    ax.set_zlim([0,10])
    ax.grid(True,which='both')

    '''
    '''


    '''
    '''

