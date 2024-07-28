from manim import *
import math   

#Defining what the actual heck the normal distribution is

def PDF_normal(x, mu, sigma):
    '''
    General form of probability density function of univariate normal distribution
    '''
    return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))


class Scene2(Scene):
    def construct(self):

        CTLTitle = Title("Central Limit Theorem", include_underline= True)

        ax1 = Axes(
            x_range=[-5,5,1],
            y_range=[0,1,1], 
            axis_config={"include_numbers": False}
        )

        curve = always_redraw(lambda:
                              ax1.plot(lambda x:PDF_normal(x, 0, 1), color=YELLOW))
        
        self.play(Write(CTLTitle))
        self.wait

        self.play(Create(ax1))
        self.wait()

        self.play(Create(curve))
        self.wait(3)

        self.play(Uncreate(curve))
        self.wait()

        Group2 = VGroup(CTLTitle, ax1)
        self.play(FadeOut(Group2))

        