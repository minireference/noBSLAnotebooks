def cells():
    '''
    # 2/ Exercise solutions
    '''

    '''
    '''

    # setup SymPy
    from sympy import *
    x, y, z, t = symbols('x y z t')
    init_printing()

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
    ### E2.1
    
    Find the inverse matrix $A^{-1}$ for the matrix $A=\begin{bsmallmatrix}7 & 0 \\ 0 & 2\end{bsmallmatrix}$. Verify that $A^{-1}(A\vec{v})=\vec{v}$ for any vector $\vec{v} = \begin{bsmallmatrix} v_1 \\ v_2\end{bsmallmatrix}$. 
    
    #### Answer
    $A^{-1} = \begin{bsmallmatrix}\frac{1}{7} & 0 \\ 0 & \frac{1}{2}\end{bsmallmatrix}$.
    
    #### Solution
    To find $A^{-1}$ we must consider the action of $A=\begin{bsmallmatrix}7 & 0 \\ 0 & 2\end{bsmallmatrix}$ on an arbitrary vector $\vec{v}=\begin{bsmallmatrix}v_1 \\ v_2\end{bsmallmatrix}$, and perform the inverse action. Since $A$ multiplies the first component by $7$, $A^{-1}$ must divide the first component by $7$. Since $A$ multiplies the second component by $2$, $A^{-1}$ must divide the second component by $2$. Thus $A^{-1} = \begin{bsmallmatrix}\frac{1}{7} & 0 \\ 0 & \frac{1}{2}\end{bsmallmatrix}$. 
    '''

    '''
    '''

    A = ...

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
    Given the matrices $A=\begin{bsmallmatrix}1 & 3 \\ 4 & 5\end{bsmallmatrix}$ and $B=\begin{bsmallmatrix} -1 & 0 \\ 3 & 3 \end{bsmallmatrix}$, and the vectors $\vec{v}=\begin{bsmallmatrix}1 \\  2\end{bsmallmatrix}$ and $\vec{w}=\begin{bsmallmatrix}-3 \\ -4\end{bsmallmatrix}$, compute the following expressions. 
    
    
    - a) $A\vec{v}$
    - b) $B\vec{v}$
    - c) $A(B\vec{v})$
    - d) $B(A\vec{v})$
    - e) $A\vec{w}$
    - f) $B\vec{w}$
    '''

    '''
    '''

    # define the matrices A and B, and the vecs v and w
    A = Matrix([[1,3],    # 2x2 matrix A
                [4,5]])
    B = Matrix([[-1,0],   # 2x2 matrix B
                [ 3,3]])
    v = Matrix([1,2])     # 2x1 column vector v
    w = Matrix([-3,-4])   # 2x1 column vector w

    '''
    '''

    # a)
    A*v

    '''
    '''

    # b)
    B*v

    '''
    '''

    # c)
    A*B*v

    '''
    '''

    # d)
    B*A*v

    '''
    '''

    # e)
    A*w

    '''
    '''

    # f)
    B*w

    '''
    '''

    '''
    ### E2.3
    
    Find the components $v_1$ and $v_2$ of the vector $\vec{v} =\begin{bsmallmatrix}v_1 \\ v_2\end{bsmallmatrix}$ so that $E\vec{v} = 3 \vec{e}_2 - 2\vec{e}_1$, where $E$ is the following matrix:
    
    $$
      E
      =  \;
        \begin{bmatrix}
        | & | \\
        \vec{e}_1 & \vec{e}_2 \\
        | & | 
        \end{bmatrix}\!.
    $$
    
    
    #### Answer
    $v_1=-2$, $v_2=3$.
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
    ### E2.4
    
    Given the vectors $\vec{u}=(1,1,0)$ and $\vec{v}=(0,0,3)$, compute the following vector expressions: 
     **a)** $\vec{u}+\vec{v}$ **b)** $\vec{u}-\vec{v}$ **c)** $3\vec{u}+\vec{v}$ **d)** $\| \vec{u} \|$
    
    
    #### Answer
     **a)** $(1,1,3)$;  **b)** $(1,1,-3)$;  **c)** $(3,3,3)$;  **d)** $\sqrt{2}$.
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.5
    
    Given $\vec{v}= (1, 2, 3)$ and $\vec{w}=(0, 1, 1)$, compute the following vector products:
    
     - **a)** $\vec{v} \cdot \vec{w}$;
     - **b)** $\vec{v} \times \vec{w}$;
     - **c)** $\vec{w} \times \vec{v}$;
     - **d)** $\vec{w} \times \vec{w}$. 
    
    #### Answer
     **a)** $5$;  **b)** $(-1, -1, 1)$;  **c)** $(1,1,-1)$;  **d)** $(0, 0, 0)$.
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.6 
    
    
    For each of the following vectors, $\vec{v}_1 = 10\angle 10^{\circ}$, $\vec{v}_2 = 10\angle 30^{\circ}$, $\vec{v}_3 = 10\angle 60^{\circ}$, $\vec{v}_4 = 10\angle 120^{\circ}$,  complete the following tasks: 
    
     - a)  Draw the vector in a Cartesian plane. 
     - b)  Compute the vector's $x$- and $y$-coordinates. 
     - c)  Compute the projection of the vector in the direction $\hat{\imath}$. Your answer should be a vector quantity. 
     - d)  Compute the projection of the vector in the direction $\hat{\jmath}$. 
     - e)  Compute the projection of the vector in the direction $\vec{d}=(1,1)$, and find the length of the projection. 
    
    **Hint**:  Recall the formula for the projection of the vector $\vec{v}$ in the direction $\vec{d}$ is defined as $\Pi_{\vec{d}}(\vec{v}) = \Big(\frac{ \vec{d}\,\cdot \, \vec{v} }{ \|\vec{d}\|^2 } \Big) \vec{d}$. 
    
    #### Answer
    
    
     - a) This part has been omitted for brevity. 
     - b) $\vec{v}_1 = (9.848, 1.736)$; $\vec{v}_2 = (8.66, 5)$; $\vec{v}_3 = (5, 8.66)$; $\vec{v}_4 = (-5, 8.66)$. 
     - c) $\Pi_{\hat{\imath}}(\vec{v}_1) = 9.848$; $\Pi_{\hat{\imath}}(\vec{v}_2) = 8.66$; $\Pi_{\hat{\imath}}(\vec{v}_3) = 5$; $\Pi_{\hat{\imath}}(\vec{v}_4) = -5$. 
     - d) $\Pi_{\hat{\jmath}}(\vec{v}_1) = 1.736$; $\Pi_{\hat{\jmath}}(\vec{v}_2) = 5$; $\Pi_{\hat{\jmath}}(\vec{v}_3) = 8.66$; $\Pi_{\hat{\jmath}}(\vec{v}_4) = 8.66$. 
     - e) $\Pi_{\vec{d}}(\vec{v}_1) = (5.79, 5.79)$ and $\| \Pi_{\vec{d}}(\vec{v}_1) \| = 8.19$; $\Pi_{\vec{d}}(\vec{v}_2) = (6.83,6.83)$ and $\| \Pi_{\vec{d}}(\vec{v}_2) \| = 9.66$; $\Pi_{\vec{d}}(\vec{v}_3) = (6.83,6.83)$ and $\| \Pi_{\vec{d}}(\vec{v}_3) \| = 9.66$; $\Pi_{\vec{d}}(\vec{v}_4) = (1.83,1.83)$ and $\| \Pi_{\vec{d}}(\vec{v}_4) \| = 2.59$. 
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
    ### E2.7
    
    
    Given the matrices $A = \begin{bsmallmatrix} 3 & 4 \\ 2 & 1 \end{bsmallmatrix}$, $B = \begin{bsmallmatrix} -1 & 0 & 1 & 2 \\ 4 & 3 & 2 & 1 \end{bsmallmatrix}$, and $C = \begin{bsmallmatrix}  -2 & 3 & \,0 \\ 2 & \!-2 & \,1\end{bsmallmatrix}$, compute the expressions. 
    
     - a) $A^{\mathsf{T}}$
     - b) $C^{\mathsf{T}}$
     - c) $A^2$
     - d) $AB$
     - e) $AC$
     - f) $BA$
     - g) $C^{\mathsf{T}} \!A$
     - h) $\det(A)$
     - i) $\det(B)$
     - j) $\det(C)$
     - k) $\det(A^{\mathsf{T}})$
     - l) $\det(AA^{-1})$
     - m) $\textup{Tr}(A)$
     - n) $\textup{Tr}(A^{\mathsf{T}})$
    
    **Hint**:  Some of these expressions may not exist. 
    
    #### Answer
    
    
     - a) $\begin{bsmallmatrix}3 & 2\\ 4 & 1\end{bsmallmatrix}$; 
     - b) $\begin{bsmallmatrix}-2 & 2\\3 & -2\\0 & 1\end{bsmallmatrix}$; 
     - c) $\begin{bsmallmatrix}17 & 16\\8 & 9\end{bsmallmatrix}$; 
     - d) $\begin{bsmallmatrix}13 & 12 & 11 & 10\\2 & 3 & 4 & 5\end{bsmallmatrix}$; 
     - e) $\begin{bsmallmatrix}2 & 1 & 4\\-2 & 4 & 1\end{bsmallmatrix}$; 
     - f)  Doesn't exist; 
     - g) $\begin{bsmallmatrix}-2 & -6\\5 & 10\\2 & 1\end{bsmallmatrix}$; 
     - h) $-5$; 
     - i)  Doesn't exist; 
     - j)  Doesn't exist; 
     - k) $-5$; 
     - l) $1$; 
     - m) $4$; 
     - n) $4$. 
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.8
    
    Given the $1\times 3$ matrices (row vectors) $\vec{u} = (1,2,3)$ and $\vec{v} = (2,-1,0)$, compute the following products: 
    
     - a) $\vec{u}\,\vec{u}^{\mathsf{T}}$
     - b) $\vec{v}\,\vec{v}^{\mathsf{T}}$
     - c) $\vec{u}\,\vec{v}^{\mathsf{T}}$
     - d) $\vec{u}^{\mathsf{T}} \vec{u}$
     - e) $\vec{v}^{\mathsf{T}} \vec{v}$
     - f) $\vec{u}^{\mathsf{T}} \vec{v}$
    
    **Hint**:  The transpose of a $1 \times 3$ row vector is a $3\times 1$ column vector. 
    
    #### Answer
    
    
     - a) $14$; 
     - b) $5$; 
     - c) $0$; 
     - d) $\begin{bsmallmatrix}1 & 2 & 3\\2 & 4 & 6\\3 & 6 & 9\end{bsmallmatrix}$; 
     - e) $\begin{bsmallmatrix}4 & -2 & 0\\-2 & 1 & 0\\0 & 0 & 0\end{bsmallmatrix}$; 
     - f) $\begin{bsmallmatrix}2 & -1 & 0\\4 & -2 & 0\\6 & -3 & 0\end{bsmallmatrix}$. 
    '''

    '''
    '''


    '''
    '''


    '''
    '''

    '''
    ### E2.9
    
    Find the unknowns $\alpha$ and $\beta$ in the equation $\begin{bsmallmatrix}2 & \alpha \\ \beta & -3\end{bsmallmatrix}
    \begin{bsmallmatrix}1 \\[0.5mm] 4\end{bsmallmatrix}=\begin{bsmallmatrix}0 \\[0.5mm] 0\end{bsmallmatrix}$. 
    
    #### Answer
    $\alpha=-\frac{1}{2}$and $\beta = 12$.
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
    ### E2.10
    
    Are these expressions linear in the variables $x$, $y$, and $z$?
    
    - a) $2x+5y + \sqrt{m}z$
    - b) $10\sqrt{x} + 2(y+z)$
    - c) $42x + a^2\sin(\frac{\pi}{3})y + z\cos(\frac{\pi}{3})$
    
    #### Answer
    
    
     - a) Yes; 
     - b)  No; 
     - c)  Yes. 
    
    #### Solution
    An expression is linear in the variable $v$ if it contains $v$ raised only to the first power. This is the case for the first and third expressions but not the second, since it contains $\sqrt{x} = x^{\frac{1}{2}}$. 
    '''

    '''
    '''

    x, y, z, m, a = symbols('x y z m a')
    alpha, beta, gamma = symbols(r'\alpha \beta \gamma')

    '''
    '''

    # a)
    expra = 2*x + 5*y + sqrt(m)*z
    expra.subs({"x":alpha*x, "y":0, "z":0}) == alpha*expra.subs({"x":x, "y":0, "z":0})

    '''
    '''

    '''
    So `expra` is linear in $x$.
    '''

    '''
    '''

    expra.subs({"x":0, "y":beta*y, "z":0}) == beta * expra.subs({"x":0, "y":y, "z":0})

    '''
    '''

    ...

    '''
    '''


    '''
    '''

