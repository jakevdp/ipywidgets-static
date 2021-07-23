# Static Interactive Figures for Jupyter Notebooks

## [See HTML example here](https://semidanrobaina.com/staticInteract/)

## Install:

```
pip install staticinteract
```

I really liked the functionality provided by the, now abandoned, project [ipywidgets-static](https://github.com/jakevdp/ipywidgets-static). It's a pity that it was abandoned. Contrary to what it is stated in the original repo, iPython's ipywidgets do not provide the same functionality of ipywidgets-static (as far as I know, that is). Specifically, iPython's ipywigets, while very nice and useful, only work when the Jupyter kernel is active since they call your defined function everytime one interacts with the widget.

Hence, interactive figures generated this way do not work in situations where there is no access to python, such as when the notebook is seen as a plain webpage. While generally this is not a problem, there are certain occasions where being able to manipulate interactive figures without python calculating stuff is very useful. For instance, when the calculations needed to generate the images are too involved for them to be run on the fly, or, precisely when one wants to share the notebook as a plain webpage, inside a blog or something like that.

For the previous reasons, I started working on this project to add some new features. I ask for a pull request which was ignored, probably because the project is abandoned. So I decided to continue here. This code has been useful to me. I publish this in the hopes that it will be useful to someone else too!. Here are the main changes I have implemented:

1. First, I updated the code to be compatible with python 3 since I do not use python 2, and it's doomed to disappear anyways.
2. I added the possibility to store the generated images in a folder instead of embedding them in the notebook. Embedding the images within the notebook makes sense for small interactive plots, i.e., ones which do not generate many images. However, in larger ones the notebook gets soon saturated with embedded images, it's slow to load or simply won't load properly. To solve this issue, images can now be stored outside the notebook, as png files, and are imported to the notebook when called by the interactive plot.
3. In the previous version, StaticInteract would write the same JavaScript code to the notebook cell where it was called. I find this repetitive and unnecessary, moreover prone to errors due to declaring more than once the same JavaScript variables when multiple interactive plots are done in a single notebook. To solve this issue, this part of JavaScript code is now embedded in the notebook only at the beginning, when the module is imported.

__NOTE__: Note that the notebook needs to be trusted for this library to work, since untrusted notebooks do not run embedded JavaScript code. Once the Notebook is exported to HTML, the interactive figure will continue to work.
