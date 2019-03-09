from collections import OrderedDict
import itertools
import matplotlib.pyplot as plt
from IPython import get_ipython
import base64
import sys

if sys.version_info.major > 2:
    dict_items = 'items'
else:
    dict_items = 'iteritems'

def _get_html(obj):
    """Get the HTML representation of an object"""
    # TODO: use displaypub to make this more general
    ip = get_ipython()
    png_rep = ip.display_formatter.formatters['image/png'](obj)

    if png_rep is not None:
        if isinstance(obj, plt.Figure):
            plt.close(obj)  # keep from displaying twice
        # return ('<img src="data:image/png;'
                # 'base64,{0}">'.format(png_rep.encode('base64'))) # fails in Python3
        img_elem = ('<img src="data:image/png;base64, '
                    + base64.b64encode(png_rep).decode() + '"/>')
        return (img_elem)
    else:
        return "<p> {0} </p>".format(str(obj))

    rep = ip.display_formatter.formatters['text/html'](obj)

    if rep is not None:
        return rep
    elif hasattr(obj, '_repr_html_'):
        return obj._repr_html_()


class StaticInteract(object):
    """Static Interact Object"""

    template = """
    <script type="text/javascript">
      let mergeNodes = function(a, b) {{
        return [].slice.call(a).concat([].slice.call(b));
      }}; // http://stackoverflow.com/questions/914783/javascript-nodelist/17262552#17262552

      let div = document.getElementById("static_widget");
      let range_labels = div.getElementsByTagName("label");
      if(range_labels.length > 0) {{
          for(label of range_labels) {{
             let input = document.getElementById(label.htmlFor)
             let input_value = input.value;
             label.innerHTML = input_value;
          }} // assign default value to range label
      }}

      function interactUpdate(elem){{
         let div = elem.parentNode;

         if(elem.type === "range") {{
            let label = document.getElementById(elem.id + "_label");
            label.innerHTML = elem.value; // update label with input value
         }}

         let outputs = div.getElementsByTagName("div");
         //let controls = div.getElementsByTagName("input");
         let controls = mergeNodes(div.getElementsByTagName("input"), div.getElementsByTagName("select"));
         function nameCompare(a,b) {{
            return a.getAttribute("name").localeCompare(b.getAttribute("name"));
         }}
         controls.sort(nameCompare);

         let value = "";
         for(i=0; i<controls.length; i++){{
           if((controls[i].type == "range") || controls[i].checked){{
             value = value + controls[i].getAttribute("name") + controls[i].value;
           }}
           if(controls[i].type == "select-one"){{
             value = value + controls[i].getAttribute("name") + controls[i][controls[i].selectedIndex].value;
           }}
         }}

         for(i=0; i<outputs.length; i++){{
           let name = outputs[i].getAttribute("name");
           if(name == value){{
              outputs[i].style.display = 'block';
           }} else if(name != "controls"){{
              outputs[i].style.display = 'none';
           }}
         }}
      }}
    </script>

    <div id="static_widget">
      {widgets} <!--Same order as ipywidgets-->
      {outputs}
    </div>
    """

    subdiv_template = """
    <div name="{name}" style="display:{display}">
      {content}
    </div>
    """

    @staticmethod
    def _get_strrep(val):
        """Need to match javascript string rep"""
        # TODO: is there a better way to do this?
        if isinstance(val, str):
            return val
        elif val % 1 == 0:
            return str(int(val))
        else:
            return str(val)

    def __init__(self, function, **kwargs):
        # TODO: implement *args (difficult because of the name thing)
        # update names
        # TODO: causes widget names to equal argument names,
        #  overriding user widget name.
        for name in kwargs:
            kwargs[name] = kwargs[name].renamed(name)

        self.widgets = OrderedDict(kwargs)
        self.function = function

    def _output_html(self):
        names = [name for name in self.widgets]
        values = [widget.values() for widget in self.widgets.values()]
        defaults = tuple([widget.default for widget in self.widgets.values()])

        #Now reorder alphabetically by names so divnames match javascript
        names,values,defaults = zip(*sorted(zip(names,values,defaults)))

        results = [self.function(**dict(zip(names, vals)))
                   for vals in itertools.product(*values)]

        divnames = [''.join(['{0}{1}'.format(n, self._get_strrep(v))
                             for n, v in zip(names, vals)])
                    for vals in itertools.product(*values)]
        display = [vals == defaults for vals in itertools.product(*values)]

        tmplt = self.subdiv_template
        return "".join(tmplt.format(name=divname,
                                    display="block" if disp else "none",
                                    content=_get_html(result))
                       for divname, result, disp in zip(divnames,
                                                        results,
                                                        display))


    def _widget_html(self):
        return "\n<br>\n".join([widget.html()
                                for name, widget in sorted(
                                    getattr(self.widgets, dict_items)())]) # Python 2-3

    def html(self):
        return self.template.format(outputs=self._output_html(),
                                    widgets=self._widget_html())

    def _repr_html_(self):
        return self.html()
