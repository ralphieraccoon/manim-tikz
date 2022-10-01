from .template import TikzTemplate

from typing import List
from manim.mobject.svg.svg_mobject import SVGMobject
from manim.utils.tex_file_writing import tex_to_svg_file


class Tikz(SVGMobject):
    """Converts Tikz markup into an SVG object which is then imported into manim.
    
    Parameters
    ----------
    code
        The Tikz markup code to be converted.
    packages
        A list of additional packages that are required for the Tikz image, will be included in the latex preamble in the format :code:`\\addpackage{package1,package2,...}`.
    libraries
        A list of Tikz libraries that are required for the Tikz image, will be included in the latex preamble in the format :code:`\usetikzlibrary{library1,library2,...}`.
    tikzset
        Use this to define any custom Tikz styles, among other things (see the Tikz manual for more detail), will be included in the preamble in the format :code:`\\tikzset{command1,command2,...}`.
    preamble
        Use this to add any additional commands to the preamble, such as setting up package options.
    use_pdf
        By default, the latex compiler in manim outputs to .dvi. This can be incompatible with some of the drawing commands Tikz commands get translated to, which only work in postscript. Set this to :code:`True` if you experience rendering issues.
    kwargs : Any
            Additional arguments to be passed to :class:`SVGMobject`.

    Examples
    -------- 

    .. manim:: ManimTikzExample
        :save_last_frame:

        class ManimTikzExample(Scene):
            def construct(self):

                tikz_example = Tikz(r"\draw[magenta, fill=blue] (0,0) rectangle(1,1);", use_pdf=False)

                self.add(tikz_example)

    
    """
    def __init__(
        self,
        code: str,
        packages: List[str] = [],
        libraries: List[str] = [],
        tikzset: List[str] = [],
        preamble: str = None,
        use_pdf=False,
        **kwargs,
    ):
        file_name = self.convert(code, packages, libraries, tikzset, preamble, use_pdf)
        super().__init__(
            file_name,
            **kwargs,
        )

    def convert(self, code, packages, libraries, tikzset, preamble, use_pdf) -> str:
        return tex_to_svg_file(
            code,
            environment="tikzpicture",
            tex_template=TikzTemplate(packages, libraries, tikzset, preamble, use_pdf),
        )
