def cells():
    # setup SymPy
    from sympy import *
    init_printing()
    x, y, z, t = symbols('x y z t')
    alpha, beta = symbols('alpha beta')

    '''
    '''

    '''
    # Linearity
    '''

    '''
    '''

    b, m = symbols('b m')
    
    def f(x):
        return m*x

    '''
    '''

    f(1)

    '''
    '''

    f(2)

    '''
    '''

    f(1+2)

    '''
    '''

    f(1) + f(2)

    '''
    '''

    expand(f(x+y)) ==  f(x) + f(y)

    '''
    '''

    '''
    ## What about vector inputs?
    '''

    '''
    '''

    m_1, m_2 = symbols('m_1 m_2')
    
    def T(vec):
        """A function that takes a 2D vector and returns a number."""
        return m_1*vec[0] + m_2*vec[1]

    '''
    '''

    u_1, u_2 = symbols('u_1 u_2')
    u = Matrix([u_1,u_2])
    v_1, v_2 = symbols('v_1 v_2')
    v = Matrix([v_1,v_2])

    '''
    '''

    T(u)

    '''
    '''

    T(v)

    '''
    '''

    T(u) + T(v)

    '''
    '''

    expand( T(u+v) )

    '''
    '''

    simplify( T(alpha*u + beta*v) - alpha*T(u) - beta*T(v) )

    '''
    '''

    '''
    # Linear transformations
    '''

    '''
    '''

    '''
    A linear transformation is function that takes vectors as inputs, and produces vectors as outputs:
    
    $$
       T: \mathbb{R}^n \to \mathbb{R}^m.
    $$
    
    see page 116 in book
    '''

    '''
    '''

    m_11, m_12, m_21, m_22 = symbols('m_11 m_12 m_21 m_22')
    
    def T(vec):
        """A linear transformations R^2 --> R^2."""
        out_1 = m_11*vec[0] + m_12*vec[1]
        out_2 = m_21*vec[0] + m_22*vec[1]
        return Matrix([out_1, out_2])

    '''
    '''

    T(u)

    '''
    '''

    T(v)

    '''
    '''

    T(u+v)

    '''
    '''

    '''
    ## Linear transformations as matrix-vector products 
    '''

    '''
    '''

    '''
    see page 113
    '''

    '''
    '''

    def T_impl(vec):
        """A linear transformations implemented as matrix-vector product."""
        M_T = Matrix([[m_11, m_12], 
                      [m_21, m_22]])
        return M_T*vec

    '''
    '''

    T_impl(u)

    '''
    '''


    '''
    '''

