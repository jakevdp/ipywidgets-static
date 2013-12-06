# To Do
There are various issues here...

## Output CSS Tags
The widgets should have css attributes that allow their style to be tweaked.
Also, we need better labeling options for the widgets.

## HTML renderings
Currently the HTML rendering of arbitrary objects uses either the raw text
format or the png format.  It should be possible to use the standard
IPython display tools to do this the right way.  According to @minrk and
@ellisonbg via the IPython dev hipchat:

> if you just call OutputArea.append_mime_type(json, your_element, true), you should get back `your_element` with the rendered output attached.
> Or if you instantiate OutputArea and pass it the div you want output in you can just call the top level handle output with the JSON
> you could easily build that JSON from the display_formatter JSON
> The message spec docs would show you how to build that
> http://ipython.org/ipython-doc/dev/development/messaging.html#display-data
>
> Basically it is just a matter of top level content attribute with data
> and metadata subattributes that contain the display JSON
>
> I think all you need is the publish method of displaypub:
> https://github.com/ipython/ipython/blob/master/IPython/kernel/zmq/zmqshell.py#L77
> (data, metadata) is what formatter.format(obj) returns
>


## Working with float-values
Widgets with floating-point values don't always work, because of the differences
in the way Python and Javascript represent floats.

## Other widgets
Currently only radio buttons and sliders are implemented. Are there other
widgets that should be included?

## Animations
This is a much better approach than that used in the ``JSAnimation`` library.
It would be nice to re-build those animation tools in the style used here, and
to include animations in this library

## Compression
These things can get really big really fast.  Implementing some sort of image
compression into this would be really, really useful.
