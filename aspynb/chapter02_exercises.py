def cells():
    '''
    # 2/ Intro to linear algebra
    '''

    '''
    '''

    # setup SymPy
    from sympy import *
    x, y, z, t = symbols('x y z t')
    init_printing()
    
    # setup plotting
    %matplotlib notebook
    import matplotlib.pyplot as mpl
    from util.plot_helpers import plot_vec, plot_vecs, autoscale_arrows
    from util.plot_helpers import plot_point, plot_line, plot_plane
    from util.plot_helpers import plot_augmat
    
    # define alias Vector for Matrix objects
    Vector = Matrix

    '''
    '''


    '''
    '''

    '''
    ## Definitions
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.1
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.2
    '''

    '''
    '''

    '''
    Given the matrices $A=\begin{pmatrix}1 & 3 \\ 4 & 5\end{pmatrix}$ and $B=\begin{pmatrix} -1 & 0 \\ 3 & 3 \end{pmatrix}$, 
    and the vectors $\vec{v}=\begin{pmatrix}1 \\  2\end{pmatrix}$ and $\vec{w}=\begin{pmatrix}-3 \\ -4\end{pmatrix}$,
    compute the following expressions.
    
    - a) $A\vec{v}$
    - b) $B\vec{v}$
    - c) $A(B\vec{v})$
    - d) $B(A\vec{v})$
    - e) $A\vec{w}$
    - f) $B\vec{w}$
    '''

    '''
    '''

    A = Matrix([[1,3],
                [4,5]])
    B = Matrix([[-1,0],
                [ 3,3]])
    v = Vector([[1,2]]).T

    '''
    '''

    # d)
    B*A*v

    '''
    '''

    '''
    ### E2.3
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Vector operations
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.4
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.5
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.6 
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Matrix operations
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.7
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.8
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.9
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ## Linearity
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.10
    '''

    '''
    '''


    '''
    '''


    '''
    '''

