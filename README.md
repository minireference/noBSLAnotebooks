
[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/minireference/noBSLAnotebooks/HEAD)


No bullshit guide to linear algebra notebooks
=============================================
Jupyter notebooks with exercises for the **No Bullshit Guide to Linear Algebra**
by Ivan Savov (Minireference Co.,  v2.2 2021, ISBN 0992001021).
The book is available in both print and digital formats:
 • softcover print from lulu.com [bit.ly/noBSLA-sc](https://bit.ly/noBSLA-sc)
 • hardcover print from lulu.com [bit.ly/noBSLA-hc](https://bit.ly/noBSLA-hc)
 • softcover print from amazon: [amazon.com/dp/0992001021](https://amazon.com/dp/0992001021)
 • digital download from gumroad: [gum.co/noBSLA](https://gum.co/noBSLA).
For more info, visit the book’s website [minireference.com](https://minireference.com).


### Abstract
Linear algebra is the foundation of science and engineering.
Knowledge of linear algebra is a prerequisite for studying statistics,
machine learning, computer graphics, signal processing, chemistry, economics,
quantum mechanics, and countless other applications.
Indeed, linear algebra offers a powerful toolbox for modelling the real world.
Readers can build up their understanding of linear algebra by solving exercises
and practice problems using the computer algebra system `SymPy` to speed up
tedious matrix arithmetic tasks, as illustrated in the following notebooks.


Contents
========
Follow the video links to watch the tutorials or click the "Open in Colab" links
to play explore the linear algebra notebooks interactively on your own. See the
section [Local installation](https://github.com/minireference/noBSLAnotebooks#local-installation)
below for instructions how to install and run the notebooks locally on your computer.


## Chapters overview
This video and the associated notebook provide a bird's eye view of the whole book.
- Video: https://www.youtube.com/watch?v=2G3PmEZI6n8
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/Linear_algebra_chapters_overview.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/Linear_algebra_chapters_overview.ipynb) (read-only).



## Chapter 2: Intro to linear algebra

### Definitions of vectors and matrices
- Video: https://www.youtube.com/watch?v=5ohBydRZvIU
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter02_definitions.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter02_definitions.ipynb) (read-only).

### Linearity intuition
- Video: https://www.youtube.com/watch?v=WfrwVMTgrfc
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter02_linearity_intuition.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter02_linearity_intuition.ipynb) (read-only).



## Chapter 3: Computational linear algebra

### Exercises on Gauss-Jordan elimination
- Video: https://www.youtube.com/watch?v=Lfz27_MK-5M
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter03_exercises.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter03_exercises.ipynb) (read-only).


### Problems
- Video not ready yet.
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter03_problems.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter03_problems.ipynb) (read-only).



## Chapter 4: Geometric aspects of linear algebra

### Exercises
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter04_exercises.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter04_exercises.ipynb) (read-only).


### Problems
- Notebook: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/minireference/noBSLAnotebooks/blob/master/chapter04_problems.ipynb) (interactive) or [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/minireference/noBSLAnotebooks/blob/master/chapter04_problems.ipynb) (read-only).





Local installation
------------------
The Colab links provided above allow you to run the notebooks in the cloud,
which is very useful (you don't need to install anything on your computer).
For an even better interactive experience, you can install the jupyter notebook
software on your computer and run the notebooks locally.

**Prerequisites**: before you begin, make sure you have required software:
- You'll need to have Python 3 installed on your computer. You can check this is
  the case by opening a command prompt (terminal) an typing in `python --version`
  and making sure something like `Python 3.x.y` gets printed.
  If you get an old version of Python, e.g. `2.7.9`, you can try running the 
  command `python3 --version` instead, or else you can [download](https://www.python.org/downloads/)
  and install a new version.
- You'll also need to [download and install git](https://git-scm.com/downloads).



### Step 1. Use git to clone the repository
Open a command prompt and issue the following command to "clone" all the notebook
files from the github repo and make a local copy of them on your computer:

```bash
git clone https://github.com/minireference/noBSLAnotebooks.git
```

After a few seconds you should be able to see the `.ipynb` files created in the
folder `noBSLAnotebooks`. You can inspect the files are present, but don't try to
open them just yet—you need to install [jupyter](https://jupyter.org/) to run them.



### Step 2. Install the required Python libraries
The next will be to change directory (`cd`) to the `noBSLAnotebooks` folder and
install the Python packages listed in the file `requirements.txt`:

```bash
cd noBSLAnotebooks
python -m pip install -r requirements.txt
```

This command will take a few minutes to run and in the process install jupyter notebook
software and all the other libraries we'll use in the notebooks.



### Step 3. Running the notebooks
You can start the jupyter notebook server using the command

```bash
jupyter notebook
```

then click on the link printed in the terminal to open access the notebook interface
in your web browser (your browser might open automatically when you run the command).


**Note**: It's important to keep the notebooks in their current location because
they make use of the plotting helper functions in `util/plot_helpers.py`.



Links
-----
Here are some additional links to learning resources on linear algebra and `SymPy`
that you might find helpful for your studies:

- Book preview PDF: https://minireference.com/static/excerpts/noBSLA_v2_preview.pdf
- Concept maps: https://minireference.com/static/conceptmaps/linear_algebra_concepts.pdf
- SymPy tutorial: https://minireference.com/static/tutorials/sympy_tutorial.pdf
- Linear algebra tutorial: https://minireference.com/static/tutorials/linear_algebra_in_4_pages.pdf
- *Essence of linear algebra* by 3Blue1Brown https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- Video lectures of Gilbert Strang: http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010
- Khan Academy LA course: https://www.khanacademy.org/math/linear-algebra
- *Immersive linear algebra* by Ström, Åström, and Akenine-Möller: http://immersivemath.com/ila/index.html
- Linear algebra wikibook: https://en.wikibooks.org/wiki/Linear_Algebra


Contributing
------------
To contribute to the `noBSLAnotebooks` project, you can open a pull request with
your additions (typo fixes, adding solutions to exercises or problems, or new notebooks).
Feel free to reach out to me (`firstname @ publishername dot com`) if you need
some help getting started. It will be a pleasure for me to "show you around" and
the automated scripts[[1](https://github.com/minireference/noBSLAnotebooks/blob/master/util/makepynb.sh),[2](https://github.com/minireference/noBSLAnotebooks/blob/master/util/pre-commit-hook.sh)] I've developed for the project.
