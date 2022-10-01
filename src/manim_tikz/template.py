from manim.utils.tex import TexTemplate
from typing import List


class TikzTemplate(TexTemplate):
    def __init__(
        self,
        packages: List[str] = [],
        libraries: List[str] = [],
        tikzset: List[str] = [],
        preamble: str = None,
        use_pdf=False,
        **kwargs
    ):
        super().__init__(
            tex_compiler="latex",
            documentclass="\\documentclass[preview, tikz]{standalone}",
            output_format=".pdf" if use_pdf else ".dvi",
            preamble=self.default_preamble
            + ("\n\\usepackage{" + ", ".join(packages) + "}\n" if packages else "")
            + (
                "\n\\usetikzlibrary{" + ", ".join(libraries) + "}\n"
                if libraries
                else ""
            )
            + ("\n\\tikzset{" + ",\n".join(tikzset) + "}\n" if tikzset else "")
            + ("\n" + preamble if preamble else ""),
            **kwargs
        )
