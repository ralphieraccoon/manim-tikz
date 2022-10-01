from manim import *
from manim_tikz import Tikz

class TikzScene(Scene):
    def construct(self):

        test_tex = Tikz(r"\draw[magenta, line width=10mm, fill=blue] (0,0) rectangle(1,1);", use_pdf=False)

        self.add(test_tex)

