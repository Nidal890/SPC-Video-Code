from manim import *
    

'''The beginning of the 3rd scene'''

class Scene3(Scene):
    def construct(self):

        '''calling the images'''

        egncat = ImageMobject(filename_or_array="egncat").scale(0.5).to_corner(DL, buff=0.8)
        accelerator = ImageMobject(filename_or_array="accelerator").scale(0.5).to_corner(DR, buff=0.5)
        wafer = ImageMobject(filename_or_array="wafer").scale(0.7).to_corner(DR, buff=0.5)
        m3base = ImageMobject(filename_or_array="M3_base").to_corner(DR, buff=0.5)
        coll_pcore = ImageMobject(filename_or_array="coll_pcore").scale(0.4).to_corner(DR, buff=0.5)
        fpga_chart = ImageMobject(filename_or_array="fpga_sim_results").scale(1.0).to_edge(DOWN, buff=0.5)
        variationchart = ImageMobject(filename_or_array="variation").scale(2.0).to_edge(DOWN, buff=0.5)



        """Animating all the images with a fadein and then a fadetransform"""

        self.play(FadeIn(egncat))
        self.wait(6)

        self.play(FadeIn(accelerator))
        self.wait(3)

        self.play(FadeTransform(accelerator, wafer))
        self.wait(3)
        
        self.play(FadeTransform(wafer, m3base))
        self.wait(3)
        
        self.play(FadeTransform(m3base, coll_pcore))
        self.wait(3)

        self.play(FadeOut(egncat, coll_pcore))
        self.wait(3)

        ControlCharts = Title(r"Control Charts", include_underline=True)

        self.play(Write(ControlCharts))
        self.wait(3)

        self.play(FadeIn(variationchart))
        self.wait(5)

        self.play(FadeOut(variationchart))


        blist2 = Tex(r"\item graph of how a process or processes change over time", 
                     r"\item common in most fields of engineering", 
                     tex_environment="itemize", ).to_edge(LEFT, buff=0.5, )
        
        self.play(LaggedStart(Write(blist2), lag_ratio=0.25), )
        self.wait(3)

        self.play(FadeOut(ControlCharts, blist2))
        self.wait()


        self.play(FadeIn(egncat))
        self.wait(3)
        self.play(FadeOut(egncat))
        self.wait()

        what = Tex('What happens when something goes wong in the process?', tex_environment="minipage}{16cm}")
        betterq = Tex('What is the cause of failure?')

        Wrong = Title(r"Special vs Common Cause Variations", include_underline=True)

        self.play(Write(what))
        self.wait(5)

        self.play(ReplacementTransform(what, betterq))
        self.wait()

        self.play(FadeTransformPieces(betterq, Wrong))
        
        blist3 = BulletedList(
            "Special: external factors", "Common: things that happen in production environment. Internal factors", 
            font_size=36,
        ).to_edge(LEFT, buff=0.5).scale(1)

        self.play(Write(blist3))
        self.wait(5)

        self.play(FadeOut(blist3))
        self.wait()

        self.play(FadeIn(variationchart))
        self.wait(5)

        self.play(FadeTransform(variationchart, egncat))
        self.wait(5)

        self.play(FadeTransform(egncat,variationchart))
        self.wait(5)

        self.play(FadeOut(variationchart, Wrong))
        self.wait()

        types = Title("Different Types of Control Charts", include_underline=True)

        blist4 = BulletedList("Is the data discerete or continuous?", "Discrete: are we measuring defects?", "Continuous: How big is the sample size?", font_size=28, ).scale(1.2).to_edge(LEFT, buff=0.5)

        self.play(Write(types))
        self.wait(3)

        for line in blist4:
            self.play(Write(line))
            self.wait()

        self.wait(8)


        vgroup1 = VGroup(types, blist4)

        self.play(FadeOut(vgroup1))    

        contcontrolchart = Title("Continuous Control Charts")
        contblist = BulletedList("X-MR/IMR chart", 
                                 "Xbar R chart", 
                                 "Xbar S chart")

        disccontrolchart = Title("Discrete control charts")
        discblist = BulletedList("multiple defects per unit and constant sample size, use c-charts", 
                                 "multiple defects per unit and non-constant sample size, use u-charts", 
                                 "One defect per unit and constant sample size, use np-chart", 
                                 "One defect per unit and non-costant sample size, use p-chart").scale(0.8).to_edge(buff=0.5)
         
                                 
        self.play(Write(contcontrolchart))
        self.wait()
        self.play(Write(contblist))
        self.wait(6)

        self.play(FadeOut(contcontrolchart, contblist))
        self.wait()

        self.play(Write(disccontrolchart))
        self.wait()
        self.play(Write(discblist))
        self.wait(6)

        self.play(FadeOut(disccontrolchart, discblist))
        self.wait()

        self.play(FadeIn(egncat))
        self.wait(5)
        






        






      