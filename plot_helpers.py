
from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d

from sympy import Matrix, MatrixBase

# Helper functions for plotting vectors, lines, and planes using matplotlib
#
# Design
# ------
# We want to have functions `plot_vec`, `plot_line`, `plot_plane` that are easy
# to use and can handle both 2D and 3D SymPy Matrix inputs. 

def plot_vec(vec, at=[0,0,0], color='k'):
    """
    Plot the 2d or 3d vector `vec`, which can be a SymPy Matrix, a numpy array,
    or a python list.
    """
    # if isinstance(v,MatrixBase)
    if len(vec) == 3:
        ax = plt.gca(projection='3d')
        vec_x = float(vec[0])
        vec_y = float(vec[1])
        vec_z = float(vec[2])
        a = Arrow3D([at[0], vec_x],
                    [at[1], vec_y],
                    [at[2], vec_z],
                    mutation_scale=20,
                    lw=1,
                    arrowstyle="-|>",
                    color=color)
        ax.add_artist(a)
    elif len(vec) == 2:
        ax = plt.gca()
        vec_x = float(vec[0])
        vec_y = float(vec[1])
        a = Arrow2D([at[0], vec_x],
                    [at[1], vec_y],
                    mutation_scale=20,
                    lw=1,
                    arrowstyle="-|>",
                    color=color)
        ax.add_artist(a)
    else:
        print('Error: plot_vec supports only 2D and 3D vectors.')


def plot_vecs(*args):
    """Plot each of the vectors in the arugment list in a different color."""
    colors = ['k', 'b', 'g', 'r', 'c', 'm']
    for i, vec in enumerate(args):
        plot_vec(vec, color=colors[i%len(colors)])


def plot_line(dir_vec, point):
    """
    Plots the line with direction vector `dir_vec` passing though `point`.
    """
    pass


def plot_plane(normal, d):
    """
    Plots the plane whose general equation is normal . (x,y,z) = d.
    If normal is a 2-vector, plots a line (2D plot).
    """
    pass



# IMPLEMENTATION DETAILS
################################################################################

class Arrow3D(FancyArrowPatch):
    """A 3D arrow used to represent vectors in 3D."""
    
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


class Arrow2D(FancyArrowPatch):
    """A 2D arrow used to represent vectors in 2D."""
    
    def __init__(self, xs, ys, *args, **kwargs):
        self._verts2d = xs, ys
        FancyArrowPatch.__init__(self, (xs[0],ys[0]), (xs[1],ys[1]), *args, **kwargs)
    
    def draw(self, renderer):
        xs3d, ys3d = self._verts2d
        xs, ys = xs3d, ys3d
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


# HELPER FUNCTIONS
################################################################################
 
def autoscale_arrows(ax=None):
    """
    Custom auto-scaling method for Arrow3D objects.
    """
    if ax is None:
        ax = plt.gca()
    arrow3Ds = [ ch for ch in ax.get_children() if type(ch) == Arrow3D ]
    arrow2Ds = [ ch for ch in ax.get_children() if type(ch) == Arrow2D ]
    if arrow2Ds and arrow3Ds:
        print('Mixing Arrow2D and Arrow3D not supported') 
        return -1
    if arrow3Ds:
        all_xs, all_ys, all_zs = [], [], []
        for arrow in arrow3Ds:
            all_xs.append(arrow._verts3d[0][0])
            all_xs.append(arrow._verts3d[0][1])
            all_ys.append(arrow._verts3d[1][0])
            all_ys.append(arrow._verts3d[1][1])
            all_zs.append(arrow._verts3d[2][0])
            all_zs.append(arrow._verts3d[2][1])
        min_x, max_x = min(all_xs), max(all_xs)
        min_y, max_y = min(all_ys), max(all_ys)
        min_z, max_z = min(all_zs), max(all_zs)
        cube_side = max(max_x-min_x, max_y-min_y, max_z-min_z)
        ax.set_xlim(min_x, min_x + cube_side)
        ax.set_ylim(min_y, min_y + cube_side)
        ax.set_zlim(min_z, min_z + cube_side)
    if arrow2Ds:
        all_xs, all_ys = [], []
        for arrow in arrow2Ds:
            all_xs.append(arrow._verts2d[0][0])
            all_xs.append(arrow._verts2d[0][1])
            all_ys.append(arrow._verts2d[1][0])
            all_ys.append(arrow._verts2d[1][1])
        min_x, max_x = min(all_xs), max(all_xs)
        min_y, max_y = min(all_ys), max(all_ys)
        square_side = max(max_x-min_x, max_y-min_y)
        ax.set_xlim(min_x, min_x + square_side)
        ax.set_ylim(min_y, min_y + square_side)


