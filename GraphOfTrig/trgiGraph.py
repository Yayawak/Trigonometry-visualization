from manim import *


class WaveComponents(Scene):
    
    def sin_wave(self,dx=0,Amp=1,T=1):
        return FunctionGraph(
            lambda x: Amp*np.sin((x+dx)*T),
            x_range=(-5,5)
        )

    def construct(self):
        sin_func = self.sin_wave()
        d_theta = ValueTracker()
        amplitude = ValueTracker(1)
        period = ValueTracker(1)
        def update_wave(func):
            func.become(
                self.sin_wave(dx=d_theta.get_value(),Amp=amplitude.get_value()
                            ,T=period.get_value())
            )
            return func
        
        # text describtion
        txt = VGroup(
            Text('Sine funtion'),
        ).to_corner(UL)
        amp_txt = VGroup(
            Text('Amplitude = '),
            DecimalNumber(amplitude.get_value())
        ).arrange(RIGHT).to_edge(UR)
        period_txt = VGroup(
            Text('Period = '),
            DecimalNumber(period.get_value())
        ).arrange(RIGHT).to_edge(DL)
        amp_txt[1].add_updater(lambda num: num.set_value(amplitude.get_value()))
        period_txt[1].add_updater(lambda num: num.set_value(period.get_value()))
                
        sin_func.add_updater(update_wave)
        self.play(Create(sin_func,),Create(txt)
                )
        self.play(d_theta.animate.increment_value(4*PI),rate_func=smooth,run_time=4)
        
        # change amp animation
        self.play(
            AnimationGroup(Write(amp_txt)),rate_func=smooth,run_time=1)
        
        self.wait()
        self.play(AnimationGroup(amplitude.animate.increment_value(4),run_time=4),
        )
        self.play(amplitude.animate.increment_value(-10),run_time=2)
        self.wait()
        
        
        self.play(Create(period_txt))
        self.play(period.animate.increment_value(6),run_time=3,
                rate_func=rate_functions.double_smooth)
        self.wait()