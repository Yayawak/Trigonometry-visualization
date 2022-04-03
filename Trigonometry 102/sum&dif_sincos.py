from manim import *
class Sum(Scene):
    def construct(self):
        cir = Circle().scale(3)
        radius_cir = 3
        alpha = PI/6
        beta = PI/3
        a_point = cir.point_from_proportion(1/16)
        b_point = cir.point_from_proportion(3/16)
        a_dot = Dot(a_point)
        b_dot = Dot(b_point)
        axes = Axes(x_range=[-2,2],y_range=[-2,2])
        
        ref_l = Line(ORIGIN,RIGHT*radius_cir)
        def get_alpha_comp():
            a_rad = Line(ORIGIN,a_dot.get_center())
            a_ang = Angle(ref_l,a_rad,radius=.3*radius_cir,color=GREEN).set_fill(GREEN,opacity=.5)
            alpha_comp = VGroup(a_rad,a_ang)
            return alpha_comp
        
        def get_beta_comp():
            b_rad = Line(ORIGIN,b_dot.get_center())
            b_ang = Angle(ref_l,b_rad,radius=.4*radius_cir,color=BLUE).set_fill(opacity=.5)
            beta_comp = VGroup(b_rad,b_ang)
            return beta_comp
        
        def get_sum_comp():
            g_rad = Line(ORIGIN,a_dot.get_center())
            g_ang = Angle(ref_l,g_rad,radius=.5*radius_cir,color=YELLOW).set_fill(YELLOW,opacity=.5)
            gamma_comp = VGroup(g_rad,g_ang)
            return gamma_comp
        
        alpha_components = always_redraw(get_alpha_comp)
        beta_components = always_redraw(get_beta_comp)
        get_sum_components = always_redraw(get_sum_comp)
        components = VGroup(alpha_components,beta_components)
        
        
        # self.add(cir,alpha_components,beta_components,ref_l)
        self.play(Create(cir))
        self.play(Write(ref_l))
        self.play(Create(components),run_time=4)
        self.play(Create(get_sum_components))
        self.wait()
        
        # self.play(MoveAlongPath(a_dot,cir),run_time=4)
        
        self.wait()
        