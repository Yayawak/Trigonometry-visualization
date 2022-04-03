from manim import *
from manim.utils import sounds
from numpy import angle
import random

class PiOver4(MovingCameraScene):
    def construct(self):
        self.camera.frame.width *= .75
        cir = Circle(color=BLUE)
        plane = NumberPlane()
        
        self.play(Write(plane))
        # coordinate of P(PI/4)
        
        dots = []
        for i in range(1,5):
            dot = Dot(cir.point_from_proportion((12.5*((2*i)-1))/100),)
            dot.z_index = 5
            dots.append(dot)
        dots = VGroup(*dots)
        print(dots)
        print(len(dots))
        # dots = [ Dot(cir.point_from_proportion((12.5*(2*i-1))/100) for i in range(1,5))]
        
        self.play(Create(cir))
        self.wait()
        # show 4 dots in 45 degree
        for i in range(len(dots)):
            self.play(
                Write(dots[i]),
                dots[i].animate.set_color(YELLOW)
                ,run_time=.2
            )
            # self.wait()
            self.add_sound('mixkit-bonus-earned-in-video-game-2058')
            self.wait()
            
            
        # show arc length of 4 points
        for i in range(4):
            arc_ = Arc(arc_center=cir.get_center(),
                        start_angle=0,
                        radius=cir.radius,
                        angle=PI/4+i*(PI/2),
                        color=ORANGE).set_stroke(width=8)
            arc_.set_z_index(3)
            # arc_.set_fill(opacity=1)
            arc_.set_stroke(opacity=1)
            
            # redian text
            pre_num = 2*(i+1)-1
            dist_rad_txt = MathTex('%d\\pi\\over4'%(pre_num))
            direction = [UP,UP,DOWN,DOWN]
            dist_rad_txt.next_to(dots[i],direction=direction[i])
            self.play(
                AnimationGroup(
                    Write(arc_,),
                    rate_func=double_smooth,
                ),
                AnimationGroup(
                    FadeIn(dist_rad_txt)
                ),
                run_time=2
            )
            self.play(Flash(dots[i]),rate_func=smooth,run_time=.5)
            self.play(Uncreate(arc_),FadeOut(dist_rad_txt),run_time=.5)
            self.wait()
        self.wait()
            
        self.wait()
        
class RadianDistance(MovingCameraScene):
    def construct(self):
        plane = NumberPlane()
        self.camera.frame.width *= .5
        
        circ = Circle() 
        angle_arc = ValueTracker(0)
        angle_rad_txt = DecimalNumber(0)
        rad_txt = Text('Radian =')
        label_rad = VGroup(rad_txt,angle_rad_txt).arrange()
        label_rad.next_to(circ,DOWN,buff=MED_SMALL_BUFF)
        
        f_always(angle_rad_txt.set_value,angle_arc.get_value)
        radi =ValueTracker(1)
        arc = Arc()
        arc.add_updater(lambda ac : ac.become(Arc(radius=radi.get_value(),start_angle=0,
                                                angle=angle_arc.get_value(),).set_stroke(width=8).set_color(ORANGE)
                                            
                                            ))
        label_rad.match_color(arc)
        self.play(Create(circ),Write(label_rad))
        self.add(arc)
        for i in range(8):
            bias = np.random.uniform(-2,2)
            self.play(
                angle_arc.animate.set_value(bias*PI),rate_func=double_smooth,
                run_time=3
            )
            self.play(
                angle_arc.animate.set_value(0),run_time=.5
            )
        # self.play(
        #     angle_arc.animate.set_value(PI),run_time=4,rate_func=double_smooth
        # )
        # self.play(angle_arc.animate.set_value(PI/2),run)
        self.wait()