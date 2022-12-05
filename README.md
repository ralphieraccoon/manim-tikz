# Manim Tikz

Converts Tikz markup code into an `SVGMobject` for use in `manim`.

# Installation

`manim-tikz` requires `manim` version `0.17.0` and above, which uses the `svgelements` library for SVG rendering, as this changes how SVG images are rendered. `manim-tikz` be installed from PyPI using `pip`:

```py
pip install manim-tikz
```

# Usage

`manim-tikz` adds the subclass `Tikz` to the `manim` class `SVGMobject`, as well as the subclass `TikzTemplate` to the `manim` class `TexTemplate` behind the scenes for `Tikz` to use.

To convert Tikz markup code into an `SVGMobject`, import `Tikz` from the `manim-tikz` library:

```py
from manim import *
from manim-tikz import Tikz
```

Then when constructing a `Scene` in `manim`, define a `Tikz` object like so:

```py
tikz_image = Tikz(code, [packages], [libaries], [tikzset], preamble, use_pdf)
```

- **`code`**: The Tikz code to render, as a `string`.
- **`[packages]`** *(optional)*: A list of `string` for additional LaTeX packages to include in the preamble, added using the `\usepackage` command. For example, if you include any special fonts or symbols in your Tikz picture, like `marvosym`.
- **`[libraries]`** *(optional)*: A list of `string` for any Tikz libraries you require to render your Tikz picture, such as `positioning`, `arrows.meta` or `calc`. These will be added to the preamble using the `\usetikzlibrary` command.
- **`[tikzset]`** *(optional)*: A list of `string` for any style definitions and similar you want to define before the Tikz picture (see the Tikz/PGF package [manual](https://tikz.dev]) for further details). Added to the preamble using the `\tikzset` command.
- **`preamble`** *(optional)*: A `string` for any other commands you wish to add to the preamble, such as setting up package options. Be careful, making a mistake here can easily result in errors!
- **`use_pdf`** *(optional, `False` by default)*: By default, `manim-tikz` will render the Tikz markup to a DVI file, which is then imported into `manim`. However, some drawing commands generated by Tikz do not render properly in DVI and require postscript (PDF). Setting this option to `True` will render to a PDF file instead, so use this option if there are problems with the output.

# Example

```py
from manim import *
from manim_tikz import Tikz

class TikzScene(Scene):
    def construct(self):

        test_tex = Tikz(r"\draw[magenta, line width=10mm, fill=blue] (0,0) rectangle(1,1);", use_pdf=False)

        self.add(test_tex)
```

![manim-tikz](https://github.com/ralphieraccoon/manim-tikz/blob/master/media/images/example/TikzScene_ManimCE_v0.17.0.png?raw=true)

# Animation

Like any other `SVGMobject`, `manim` can animate these images using the same animation functions. You might get some rather bizarre results depending on how the drawing order has been interpreted, but they generally look nice. 

Future implementations of this plugin may try to include animated Tikz images using the `animate` library in Tikz, I'll have to look further into how `manim` handles animated SVG images.

# Issues

## Line Thickness

At the moment it seems that the default line thickness for TikZ is almost imperceptibly thin when rendered in `manim`. Not sure why this happens, but you may want to consider increasing `line width` in your Tikz images.

## Fadings, Gradients, Shadows etc.

I haven't yet tested the library using any of these Tikz features, so I don't know how well they will work in `manim`. I'll look at making some tests in the future.

