from manim import *
import math 

class Scene1_redo(Scene):

    def construct(self):

        # making the different text for animation
        t1 = Text("Statistical Process Control").scale(1.5)
        t2 = Text("SPC").scale(2.0)

        #animating the text

        self.play(Write (t1))

        self.wait(1)
        self.play(ReplacementTransform(t1, t2), )
        self.wait(1)

        self.play(FadeOut(t2))

        title1 = Title("Statistical Process Control (SPC):", include_underline= True,)


        '''tex_environment param formatted like so due to a bug in manim 18.1 currently'''
        blist1 = Tex(r"""
                    \begin{itemize}
                    \item the use of statistical techniques to control a process or production method
                    \item ensure top quality
                    \item maximize efficiency
                    \item reduce downtime and costs
                    \end{itemize}
                    """, tex_environment="minipage}{16em}").to_edge(LEFT)
        


        self.play(Write(title1))

        self.play(Write(blist1))

        self.wait(5)

        deflist = Group(title1, blist1)
        
        self.play(FadeOut(deflist))

