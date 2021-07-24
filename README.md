# Static Interactive Figures for Jupyter Notebooks

## [See HTML example here](https://semidanrobaina.com/staticInteract/)

## Install:

```
pip install staticinteract
```

I really liked the functionality provided by the, now abandoned, project [ipywidgets-static](https://github.com/jakevdp/ipywidgets-static). Contrary to what it is stated in the original repo, iPython's ipywidgets do not provide the same functionality of ipywidgets-static (as far as I know, that is). Specifically, iPython's ipywigets depend on an active Jupyter kernel to work. Thus, interactive figures do not work in situations where there isn't any kernel to support them, such as when displaying the notebook as a webpage after converting it to HTML.

I find it very useful to be able to maintain interactivity of figures in HTML-displayed notebooks. For instance, to share scientific results with colleagues. For this reason I have added some new features to the original project and made it into this package so it's easier to install.

These are  the main additions:

1. First, I updated the code to be compatible with python 3 since I do not use python 2, and it's doomed to disappear anyways.
2. I added the possibility to store the generated images in a folder instead of embedding them in the notebook. Embedding the images within the notebook makes sense for small interactive plots, i.e., ones which do not generate many images. However, in larger ones the notebook gets soon saturated with embedded images, it's slow to load or simply won't load properly. To solve this issue, images can now be stored outside the notebook, as png files, and are imported to the notebook when called by the interactive plot.
3. In the previous version, StaticInteract would write the same JavaScript code to the notebook cell where it was called. I find this repetitive and unnecessary, moreover prone to errors due to declaring more than once the same JavaScript variables when multiple interactive plots are done in a single notebook. To solve this issue, this part of JavaScript code is now embedded in the notebook only at the beginning, when the module is imported.

__NOTE__: The notebook needs to be trusted for interactive figures to work, since untrusted notebooks do not run embedded JavaScript code. Once the Notebook is exported to HTML, interactive figures will continue to work.
