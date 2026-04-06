from manim import *
import numpy as np
import random as rand
class TitleScreen(Scene):
    def construct(self):
#========================================scene0/1:introduction========================================#
        quote0 = Text("Mathematics is the language in which God has written the universe.",t2c={'Mathematics':GREEN,'universe':YELLOW}).scale(0.6).shift(UP*3)
        author0 = Text("—Galileo Galilei", color = BLUE, font = "Times New Roman").scale(0.7)
        quote1 = Text("数学是上帝在宇宙中书写的语言。",t2c={'数学':GREEN,'宇宙':YELLOW}).shift(DOWN)
        author1 = Text("—伽利略", color = BLUE)
        author0.next_to(quote0.get_corner(DOWN + RIGHT), DOWN*2 + LEFT)
        author1.next_to(quote1.get_corner(DOWN + RIGHT), DOWN*2 + LEFT)
        self.play(Write(quote0),Write(quote1), runtime = 3)
        self.play(Write(author0),Write(author1))
        self.wait()
        self.play(FadeOut(quote0,quote1,author0,author1))
        self.wait()
        me=[MathTex(r'\int \space ?'),
            Arrow(start=RIGHT*0.25,end=RIGHT*2),
            MathTex(r'(\times)',color=RED).shift(RIGHT*2.5),
            Rectangle()
            ]
        group=VGroup()
        group.add(*[MathTex(n).shift(DOWN*n*0.5) for n in range(0,40)])
        self.play(Write(me[0]))
        self.wait(0.5)
        self.play(FadeOut(me[0]))
        self.play(FadeIn(group.shift(DOWN*5)),group.animate.shift(UP*13),run_time=5)
        self.play(GrowArrow(me[1]),Write(me[2]))
        self.wait(3)
        self.play(FadeOut(group,me[1],me[2]))
        self.play(Flash(me[3],line_length=5,num_lines=20,color=YELLOW,run_time=1))
        self.wait(1.5)
        phy=MathTex('physics?')
        self.play(Write(phy))
        self.wait(2)
        self.play(FadeOut(phy))
        self.wait(2)

#========================================scene0/2:introduction========================================#
        explanation=Text("\t\tThis is an example problem extracted from Little Cloth Shoe's book 微积分, \nwhich was published by Shanghai Jiaotong University, High level Education Press \nin 2008 on p.275, e.g.5.94.",
                         t2c={"Little Cloth Shoe":BLUE,
                              "Shanghai Jiaotong University":GREEN,
                              "High level Education Press":GOLD},
                        t2s={'微积分':ITALIC,
                             'Shanghai Jiaotong University':ITALIC,
                             'High level Education Press':ITALIC},
                        line_spacing=1.5,
                        font_size=27
                        ).shift(UP*2)
        Copyright=Text('Copyright @JTST on www.bilibili.com',color=GRAY,
                       t2c={'JTST':WHITE},t2s={'www.bilibili.com':ITALIC},
                       t2w={'JTST':BOLD},font_size=25
                       ).shift(DOWN*3)
        self.play(FadeIn(explanation,Copyright))
        self.wait(0.5)
        self.play(FadeOut(Copyright,explanation))
        self.wait(0.5)


#========================================scene1:problem========================================#
        prob=Text('We consider this situation: \nThere is a long stick nearby a massive point, which the point is on the perpendicular \nbisector of the stick or the same straight line where the stick is at. How much is \nthe gravitational force acting on the massive point, according to the long stick?',
                  t2c={'gravitational force':GOLD,
                       'long stick':RED,
                       'massive point':RED,
                       'the perpendicular':BLUE,
                       'bisector':BLUE,
                       'the same straight line':BLUE
                       },
                    line_spacing=1.5,
                    font_size=25
                    ).shift(UP*2)
        self.play(Write(prob),run_time=20)
        ppdbs=[DashedLine(start=LEFT*4.0,end=DOWN*4.0+LEFT*4.0,
                          color=GREY,stroke_width=3),
               DashedLine(start=DOWN*2,end=DOWN*2+RIGHT*7,
                          color=GREY,stroke_width=3)
                ]
        stick=[Line(start=LEFT*5.5+DOWN*3.2,end=LEFT*2.5+DOWN*3.2,
                    color=BLUE_E,stroke_width=25),
               Line(start=RIGHT*6.0+DOWN*2.0,end=RIGHT*3.0+DOWN*2.0,
                    color=BLUE_E,stroke_width=25)
                ]
        self.wait(2)
        self.play(FadeIn(ppdbs[0],ppdbs[1]),Create(stick[0]),Create(stick[1]))
        self.wait(0.2)
        msvpt=[Dot(point=DOWN*1.5+LEFT*4,
                   color=BLUE_E),
               Dot(point=DOWN*2+RIGHT*2,
                   color=BLUE_E)
                ]
        arrow=[
                [Arrow(start=DOWN*1.51+LEFT*4,end=LEFT*5.5+DOWN*3.19,color=WHITE,stroke_width=3),
                 Arrow(start=DOWN*1.51+LEFT*4,end=LEFT*2.5+DOWN*3.19,color=WHITE,stroke_width=3),
                 Arrow(start=DOWN*1.51+LEFT*4,end=LEFT*5.5+DOWN*3.19,color=WHITE,stroke_width=3)
                 ],
                [Arrow(start=DOWN*2+RIGHT*2.01,end=RIGHT*6+DOWN*2,color=WHITE,stroke_width=3),
                 Arrow(start=DOWN*2+RIGHT*2.01,end=RIGHT*3+DOWN*2,color=WHITE,stroke_width=3)
                 ]
                 ]
        self.play(Create(msvpt[0]),Create(msvpt[1]),GrowArrow(arrow[0][0]))
        self.play(ReplacementTransform(arrow[0][0],arrow[0][1]))
        self.play(ReplacementTransform(arrow[0][1],arrow[0][2]))
        self.play(GrowArrow(arrow[1][0]),FadeOut(arrow[0][2]))
        self.play(ReplacementTransform(arrow[1][0],arrow[1][1]))
        self.wait(2)
        self.play(FadeOut(prob,stick[0],stick[1]),FadeOut(ppdbs[0],ppdbs[1]),FadeOut(msvpt[0],msvpt[1]),FadeOut(arrow[1][1]))
        self.wait(2)


#========================================scene2:invitation========================================#
        gvt_ty=Text('gravitational theory',t2s={'gravitational theory':ITALIC})
        dms_ball=[Dot(point=UP*2+LEFT*2,color=RED_C).scale(2),
                  Dot(point=UP*2+RIGHT*2,color=GREEN_C).scale(2),
                  Square(color=GREEN_C).scale(0.2).shift(UP*2+RIGHT*2)
                  ]
        dms_arrow=[DoubleArrow(UP*2+LEFT*2,UP*2+RIGHT*2,color=BLUE),
                   DoubleArrow(UP*2+LEFT*3,UP*2+RIGHT*3,color=BLUE_E),
                   DoubleArrow(UP*2+LEFT*2,UP*2+RIGHT*2,color=BLUE),
                   MathTex('r').shift(UP*2.3)
                   ]
        self.play(Write(gvt_ty))
        self.wait()
        self.play(FadeOut(gvt_ty))
        self.wait()
        self.play(Create(dms_ball[0]))
        self.wait()
        self.play(Create(dms_ball[1]))
        self.wait()
        self.play(GrowFromCenter(dms_arrow[0]))
        self.wait()
        self.play(Create(dms_arrow[3]))
        self.wait()
        dms_ball_mass=[MathTex('m_1').shift(UP*1.3+LEFT*2),
                       MathTex('m_2').shift(UP*1.3+RIGHT*2)
                        ]
        self.play(Write(dms_ball_mass[0]))
        self.wait()
        self.play(Write(dms_ball_mass[1]))
        self.wait(3)
        gvt_fml=MathTex('F= G \\frac{m_1 m_2}{r^2}')
        self.play(Write(gvt_fml),run_time=10)
        self.wait()
        #introduce gravatational formula
        self.wait(2)
        self.play(dms_ball[0].animate.shift(LEFT),
                  dms_ball_mass[0].animate.shift(LEFT),
                  dms_ball_mass[1].animate.shift(RIGHT),
                  dms_ball[1].animate.shift(RIGHT),
                  ReplacementTransform(dms_arrow[0],dms_arrow[1]))
        self.wait(0.2)
        self.play(dms_ball[1].animate.shift(LEFT),
                  dms_ball_mass[1].animate.shift(LEFT),
                  dms_ball_mass[0].animate.shift(RIGHT),
                  dms_ball[0].animate.shift(RIGHT),
                  ReplacementTransform(dms_arrow[1],dms_arrow[2]))
        self.play(Circumscribe(gvt_fml))
        wh=MathTex('?').shift(UP*2+RIGHT*3)
        self.wait()
        self.play(Write(wh))
        self.wait()
        self.play(FadeOut(wh))
        self.wait()
        #inttoduce distance exchange
        self.play(FadeOut(dms_arrow[2],dms_arrow[3],gvt_fml),
                  dms_ball_mass[1].animate.shift(DOWN*0.1),
                  ReplacementTransform(dms_ball[1],dms_ball[2]))
        self.wait()
        mt=Text('乁( ˙ω˙ )厂')
        self.play(FadeIn(mt))
        self.wait()
        self.play(FadeOut(mt))
        self.wait()
        self.play(dms_ball_mass[1].animate.shift(DOWN*0.25),ScaleInPlace(dms_ball[2],2))
        self.play(dms_ball_mass[1].animate.shift(DOWN*0.5),ScaleInPlace(dms_ball[2],2))
        self.wait()
        self.play(dms_ball_mass[1].animate.shift(DOWN),ScaleInPlace(dms_ball[2],2))
        self.wait()
        intro_inter=[MathTex('Intergration'),            #title
                     MathTex(r'\lim_{\delta x \to 0}\sum_{x=a}^{b} f(x+\frac{\delta x}{2})\delta x')    #formula
                     ]
        self.play(Write(intro_inter[0]),FadeOut(dms_ball_mass[1],dms_ball[2],dms_ball[0],dms_ball_mass[0]))
        self.wait()
        self.play(ReplacementTransform(intro_inter[0],intro_inter[1]))
        self.wait(2)
        #introduce neccesity for intergration
        self.play(FadeOut(intro_inter[1]))
        self.wait()


#========================================scene3:preparation========================================#
        stk=Line(start=LEFT*5.5,end=RIGHT*5.5,color=BLUE_E,stroke_width=25)
        mv_stk=[Line(start=LEFT*5.5,end=LEFT*5.4,color=BLUE,stroke_width=25),#0           delta stk
                Line(start=LEFT*5.5+UP*0.2,end=LEFT*5.5+DOWN*0.2,color=WHITE),#1          delta left edge
                Line(start=LEFT*5.4+UP*0.2,end=LEFT*5.4+DOWN*0.2,color=WHITE),#2          delta right edge
                ]        
        self.play(Create(stk),Create(mv_stk[0]),Create(mv_stk[1]),Create(mv_stk[2]))
        self.wait()
        self.play(mv_stk[0].animate.shift(RIGHT*10.9),mv_stk[1].animate.shift(RIGHT*10.9),mv_stk[2].animate.shift(RIGHT*10.9))
        self.wait(0.2)
        self.play(mv_stk[0].animate.shift(LEFT*5.9),mv_stk[1].animate.shift(LEFT*5.9),mv_stk[2].animate.shift(LEFT*5.9))
        self.wait(0.2)
        self.play(mv_stk[0].animate.shift(RIGHT*5.9),mv_stk[1].animate.shift(RIGHT*5.9),mv_stk[2].animate.shift(RIGHT*5.9))
        self.wait()
        self.play(FadeOut(mv_stk[0],mv_stk[1],mv_stk[2],stk))
        intro_inter.append(MathTex(r'\sum'))
        intro_inter.append(MathTex(r'\sum F'))
        intro_inter.append(MathTex(r'\sum F \to accuracy'))
        self.play(Write(intro_inter[2]))
        self.play(ReplacementTransform(intro_inter[2],intro_inter[3]))
        self.wait(0.2)
        self.play(ReplacementTransform(intro_inter[3],intro_inter[4]))
        self.wait()
        self.play(FadeOut(intro_inter[4]))


#========================================scene4:intergration========================================#
        mv_stk.append(Line(start=LEFT*0.01,end=RIGHT*0.01,color=WHITE,stroke_width=25))#3
        mv_stk.append(Line(start=LEFT*55,end=RIGHT*55,color=BLUE_E,stroke_width=250))#4
        mv_stk.append(Line(start=LEFT*0.1,end=RIGHT*0.1,color=WHITE,stroke_width=250))#5
        mv_stk.append(Line(start=LEFT*5.5,end=RIGHT*5.5,color=BLUE_E,stroke_width=25))#6
        mv_stk.append(Line(start=LEFT*0.01,end=RIGHT*0.01,color=WHITE,stroke_width=25))#7
        self.play(Create(stk),Create(mv_stk[3]))
        self.wait(2)
        self.play(ReplacementTransform(mv_stk[3],mv_stk[5]),ReplacementTransform(stk,mv_stk[4]))
        self.play(Write(gvt_fml.shift(DOWN*2).scale(0.7)))
        self.play(FadeOut(gvt_fml))
        self.play(ReplacementTransform(mv_stk[4],mv_stk[6]),ReplacementTransform(mv_stk[5],mv_stk[7]))
        dms_ball_mass.append(MathTex('m').shift(UP*2))#2
        self.play(Write(dms_ball_mass[2]))
        self.wait(2)
        dms_ball_mass.append(MathTex('M').shift(UP))#3
        self.play(FadeOut(dms_ball_mass[2]),Write(dms_ball_mass[3]))
        pointer=[Arrow(start=DOWN*0.1,end=DOWN*1,stroke_width=10),
                    MathTex('d','x').shift(DOWN*1.1)
                    ]
        self.play(GrowArrow(pointer[0]),Write(pointer[1]))
        self.wait()
        self.play(Indicate(pointer[1][0]))
        self.wait(1.5)
        self.play(Indicate(pointer[1][1]))
        self.wait()
        self.play(FadeOut(pointer[1],pointer[0],dms_ball_mass[3],mv_stk[6],mv_stk[7]))
        self.wait()


#========================================scene5:problem 2========================================#
        prob_2=Text('Second situation')
        self.play(Write(prob_2))
        self.wait()#TITLE
        stk_2=Line(start=LEFT*2,end=RIGHT*4,
                color=BLUE_E,stroke_width=25)
        pnt_2=Dot(point=LEFT*4,
                color=BLUE_E,radius=0.13)
        pds_2=DashedLine(start=LEFT*5,end=RIGHT*5)
        self.play(FadeOut(prob_2))
        self.play(Create(pds_2),
                Create(stk_2),
                Create(pnt_2))
        drt=[Arrow(start=UP*2+LEFT*1,end=UP*2+LEFT*5)]
        left=Text('Left').shift(UP*3+LEFT*3)
        self.wait()
        self.play(GrowArrow(drt[0]),Write(left))
        self.play(FadeOut(left,drt[0]))
        self.wait(2)
        x_axs_2=[Arrow(start=LEFT*6,end=RIGHT*6),
                MathTex('x').shift(UP*0.5+RIGHT*5)
                ]
        self.play(GrowArrow(x_axs_2[0]),Write(x_axs_2[1]))
        org=[Dot(point=LEFT*4+DOWN*1.5),
             MathTex('O').shift(LEFT*4+DOWN*2)
             ]
        drt.append(Arrow(start=LEFT*4,end=LEFT*4+DOWN*1.5))
        self.wait()
        self.play(x_axs_2[0].animate.shift(DOWN*1.5),
                x_axs_2[1].animate.shift(DOWN*1.5))
        self.wait(3)
        self.play(Create(org[0]),Write(org[1]),GrowArrow(drt[1]))
        self.wait()
        self.play(FadeOut(drt[1]))
        Dts_2=[Line(start=LEFT*4,end=LEFT*2)]
        Dts_2.append(Brace(Dts_2[0]))#1
        Dts_2.append(Dts_2[1].get_tex('a'))#2
        self.play(FadeIn(Dts_2[1]),Write(Dts_2[2]))
        self.wait(0.2)
        Dts_2.append(Brace(stk_2))#3
        Dts_2.append(Dts_2[3].get_tex('l'))#4
        self.play(FadeOut(Dts_2[1],Dts_2[2]),
                FadeIn(Dts_2[3]),Write(Dts_2[4]))
        self.wait(0.2)
        length=MathTex('a+l').shift(RIGHT*4+UP*0.5)
        self.play(FadeOut(Dts_2[3],Dts_2[4]))
        self.play(Write(length))
        self.wait()
        self.play(FadeOut(length))
        delta_2=[Line(start=LEFT*0.01,end=RIGHT*0.01,stroke_width=25),
                Line(start=LEFT*0.1,end=RIGHT*0.1,stroke_width=250)
                ]
        big_stk2=Line(start=LEFT*10,end=RIGHT*10,color=BLUE_E,stroke_width=250)
        self.play(FadeOut(org[0],org[1],pnt_2,pds_2,x_axs_2[0],x_axs_2[1]),FadeIn(delta_2[0]))
        self.wait()
        self.play(ReplacementTransform(delta_2[0],delta_2[1]),
                  ReplacementTransform(stk_2,big_stk2))
        delta_2.append(Brace(Line(start=LEFT*0.1+DOWN*1.3,end=RIGHT*0.1+DOWN*1.3)))
        delta_2.append(delta_2[2].get_tex('dx'))
        self.play(Create(delta_2[2]))
        self.wait()
        self.play(Write(delta_2[3]))
        parts=MathTex(r'\frac{l}{dx}').shift(RIGHT)
        self.wait()
        self.play(Write(parts),FadeOut(delta_2[2],delta_2[3]))
        ment=[Text('Total mass: M').shift(UP*2)]
        self.play(Write(ment[0]),run_time=2)
        self.play(FadeOut(ment[0],parts))
        piecemass=[MathTex(r'\frac{M}{\frac{l}{dx}}').shift(DOWN*2),
                MathTex(r'\frac{M dx}{l}').shift(DOWN*2)
                ]
        self.play(Write(piecemass[0]))
        self.wait(0.2)
        self.play(ReplacementTransform(piecemass[0],piecemass[1]))
        self.wait()
        piece_gvt2=[MathTex(r'F').shift(UP*2),
                MathTex(r'F=G\frac{m_{1}m_{2}}{r^2} ').shift(UP*2),
                MathTex(r'F=G\frac{Mmdx}{l\cdot x^2} ').shift(UP*2)
                ]
        self.play(Write(piece_gvt2[0]),run_time=1)
        self.play(ReplacementTransform(piece_gvt2[0],piece_gvt2[1]))
        self.wait()
        self.play(ReplacementTransform(piece_gvt2[1],piece_gvt2[2]))
        self.wait()
        self.play(FadeOut(delta_2[1],big_stk2,piecemass[1]),
                piece_gvt2[2].animate.shift(DOWN*2))
        piece_gvt2.append(MathTex(r'\sum F=\sum G\frac{Mmdx}{l\cdot x^2} '))
        self.play(ReplacementTransform(piece_gvt2[2],piece_gvt2[3]))
        piece_gvt2.append(MathTex(r'\int F=\int G\frac{Mmdx}{l\cdot x^2} '))
        self.wait(0.2)
        self.play(ReplacementTransform(piece_gvt2[3],piece_gvt2[4]))#called int
        piece_gvt2.append(MathTex(r' F=\int G\frac{Mm}{l\cdot x^2} dx'))
        self.wait(2)
        self.play(ReplacementTransform(piece_gvt2[4],piece_gvt2[5]))#add int symbol
        piece_gvt2.append(MathTex(r' F=\int_{a}^{} G\frac{Mm}{l\cdot x^2} dx'))
        self.wait()
        self.play(ReplacementTransform(piece_gvt2[5],piece_gvt2[6]))
        piece_gvt2.append(MathTex(r'F=\int_{a}^{a+l} G\frac{Mm}{l\cdot x^2} dx'))
        self.wait()
        self.play(ReplacementTransform(piece_gvt2[6],piece_gvt2[7]))
        self.wait()
        piece_gvt2.append(MathTex(r'F=\int_{a}^{a+l} G\frac{Mm}{l\cdot x^2} dx'))
        piece_gvt2.append(MathTex(r'F=GMml^{-1}\left [ -x^{-1} \right ]_{a}^{a+l}'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\left (\left [ -\frac{1}{x}\right]^{a+l}-\left [ -\frac{1}{x}\right]^{a}\right )'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\left (\left [ -\frac{1}{a+l}\right]-\left [ -\frac{1}{a}\right]\right )'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\left (-\frac{1}{a+l}+\frac{1}{a}\right)'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\left (\frac{1}{a}-\frac{1}{a+l}\right)'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\left (\frac{(a+l)-a}{a(a+l)}\right)'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{l}\frac{l}{a^2+al}'))
        piece_gvt2.append(MathTex(r'F=\frac{GMm}{a^2+al}'))
        for i in range(7,len(piece_gvt2)-1):
            self.play(ReplacementTransform(piece_gvt2[i],piece_gvt2[i+1]))
        self.wait(3)
        self.play(FadeOut(piece_gvt2[len(piece_gvt2)-1]))


#========================================scene6:problem 1=======================================#
        prob_1=Text('First situation')
        self.play(Write(prob_1))
        self.wait()#TITLE
        stk_1=Line(start=LEFT*3+DOWN*2,
                   end=RIGHT*3+DOWN*2,
                   color=BLUE_E,stroke_width=25)
        pnt_1=Dot(point=UP*2,
                  color=BLUE_E,radius=0.13)
        pds_1=DashedLine(start=UP*3.5,end=DOWN*3.5)
        self.play(FadeOut(prob_1))
        self.play(Create(pds_1),
                  Create(stk_1),
                  Create(pnt_1))
        self.wait(2)
        x_axs_1=[Arrow(start=LEFT*4+DOWN*2,end=RIGHT*4+DOWN*2),
                 MathTex('x').shift(DOWN*2.5+RIGHT*5)
                 ]
        y_axs=[Arrow(start=DOWN*3,end=UP*3),
               MathTex('Y').shift(UP*3+RIGHT*1)
               ]
        self.play(GrowArrow(x_axs_1[0]),GrowArrow(y_axs[0]),
                  Write(x_axs_1[1]),Write(y_axs[1]))
        org=[Dot(point=DOWN*2).scale(1.5),
             MathTex('O').shift(DOWN*1.5+LEFT*0.5)
             ]
        self.wait()
        self.play(Create(org[0]),Write(org[1]))
        self.wait()
        self.play(FadeOut(org[0],org[1],x_axs_1[0],x_axs_1[1],y_axs[0],y_axs[1],pds_1))
        self.wait()
        Dts_1=[DoubleArrow(start=UP*2,end=DOWN*2)]
        Dts_1.append(MathTex('a').shift(RIGHT*0.5))#1
        self.play(GrowArrow(Dts_1[0]),Write(Dts_1[1]))
        self.wait()
        self.play(FadeOut(Dts_1[1],Dts_1[0]))
        delta_1=[Line(start=LEFT*0.01+DOWN*2-LEFT*2,end=RIGHT*0.01+DOWN*2-LEFT*2,stroke_width=25),
                 Line(start=LEFT*0.1,end=RIGHT*0.1,stroke_width=250)
                ]
        big_stk1=Line(start=LEFT*100,end=RIGHT*10,color=BLUE_E,stroke_width=250)
        self.play(FadeIn(delta_1[0]))
        self.play(ReplacementTransform(delta_1[0],delta_1[1]),
                  ReplacementTransform(stk_1,big_stk1),FadeOut(pnt_1))
        delta_1.append(MathTex('(x,0)').shift(LEFT))
        self.play(Write(delta_1[2]))
        self.wait()
        piece_gvt1=[MathTex(r'F=G\frac{Mmdx}{l\cdot y^2}').shift(UP*2)]
        self.play(Write(piece_gvt1[0]),run_time=3)
        arw1=[Line(start=LEFT*0.01+DOWN*2-LEFT*2,end=RIGHT*0.01+DOWN*2-LEFT*2,stroke_width=25).shift(LEFT*4),
              Dot(point=DOWN*2+RIGHT*2,color=BLUE_E,radius=0.13),
              Line(start=DOWN*2+LEFT*2,end=DOWN*2+RIGHT*2)
              ]
        arw1.append(Brace(arw1[2]))#3
        arw1.append(arw1[3].get_tex('y'))#4
        self.wait()
        self.play(FadeIn(arw1[0],arw1[1]))
        self.wait()
        self.play(FadeIn(arw1[3],arw1[4]))
        PT=Text('Pythagoras Theorem',t2s={'Pythagoras Theorem':ITALIC})
        self.play(FadeOut(arw1[0],arw1[1],arw1[3],arw1[4],big_stk1,delta_1[1],delta_1[2],piece_gvt1[0]),Write(PT))
        PTG=VGroup(Polygon([-2,-1.5,0],[-2,1.5,0],color=BLUE),#a
                   Polygon([-2,1.5,0],[2,-1.5,0],color=GREEN),#c
                   Polygon([-2,-1.5,0],[2,-1.5,0],color=RED),#b
                   MathTex('a',color=BLUE).shift(LEFT*2.5),
                   MathTex('b',color=RED).shift(DOWN*2),
                   MathTex('c',color=GREEN).shift(midpoint([-2,1.5,0],[2,-1.5,0])+UP*0.4+RIGHT*0.4)
                   )
        self.wait()
        self.play(ReplacementTransform(PT,PTG))
        PTF=[MathTex(r'a^{2}','+','b^{2}','=','c^{2}').shift(DOWN*3),
             MathTex(r'a^{2}+x^{2}=y^{2}').shift(DOWN*3)
             ]
        self.play(Write(PTF[0]))
        self.wait()
        self.play(ReplacementTransform(PTF[0],PTF[1]))
        self.wait()
        self.play(FadeOut(PTG),PTF[1].animate.shift(UP*4),Write(piece_gvt1[0].shift(DOWN*3.3)))
        piece_gvt1.append(Arrow(start=UP*0.7,end=DOWN*0.7))#1
        piece_gvt1.append(MathTex(r'F=G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}').shift(DOWN*1.3))#2
        self.play(GrowArrow(piece_gvt1[1]))
        self.play(ReplacementTransform(piece_gvt1[0],piece_gvt1[2]))
        self.wait()
        piece_gvt1.append(Arrow(start=DOWN*2+RIGHT,end=UP*2+LEFT,color=YELLOW))#3
        self.play(FadeOut(PTF[1]),
                  ReplacementTransform(piece_gvt1[1],piece_gvt1[3]),
                  piece_gvt1[2].animate.shift(DOWN*1.5))
        self.wait()
        self.play(FadeOut(piece_gvt1[2]),Rotate(piece_gvt1[3],angle=-0.5*PI,about_point=DOWN*2+RIGHT))
        force=[Vector([-2,0],color=YELLOW),Vector([2,0])]
        force.append(MathTex('F',color=YELLOW).shift(LEFT+UP*0.5))#2
        force.append(MathTex('-F').shift(RIGHT+UP*0.5))#3
        self.play(Rotate(piece_gvt1[3],angle=0.5*PI,about_point=DOWN*2+RIGHT))
        self.play(ReplacementTransform(piece_gvt1[3],force[0]))
        self.play(GrowArrow(force[1]))
        self.play(Write(force[2]),Write(force[3]))
        force.append(MathTex(r'\sum = 0').shift(DOWN))#4
        self.play(Write(force[4]))
        self.wait()
        self.play(FadeOut(force[0],force[1],force[2],force[3],force[4]))
        piece_gvt1[3]=Vector([-2,4],color=YELLOW).shift(DOWN*1.75+RIGHT*0.9)
        self.play(GrowArrow(piece_gvt1[3]))
        piece_gvt1.append(Vector([-2,0],color=BLUE_E).shift(DOWN*1.75+RIGHT*0.9))#4  x
        piece_gvt1.append(Vector([0,4],color=RED_E).shift(DOWN*1.75+RIGHT*0.9))#5    y
        piece_gvt1.append(Vector([-2,4],color=YELLOW).shift(DOWN*1.75+RIGHT*0.9))#6
        piece_gvt1.append(Vector([-2,4],color=YELLOW).shift(DOWN*1.75+RIGHT*0.9))#7
        self.add(piece_gvt1[6],piece_gvt1[7])
        self.play(ReplacementTransform(piece_gvt1[3],piece_gvt1[4]),
                  ReplacementTransform(piece_gvt1[6],piece_gvt1[5]))
        piece_gvt1.append(MathTex(r'F',color=YELLOW).shift(midpoint(DOWN*2+RIGHT,UP*2+LEFT)+0.4*(UP+RIGHT)))#8
        piece_gvt1.append(MathTex(r'F_x',color=BLUE_E).shift(midpoint(DOWN*1.75+RIGHT*0.9,DOWN*1.75+RIGHT*0.9-2*RIGHT)+DOWN*0.5))#9
        piece_gvt1.append(MathTex(r'F_y',color=RED_E).shift(midpoint(DOWN*1.75+RIGHT*0.9,DOWN*1.75+RIGHT*0.9+UP*4)+RIGHT*0.5))#10
        self.play(Write(piece_gvt1[8]),Write(piece_gvt1[9]),Write(piece_gvt1[10]))
        self.wait()
        for i in range(3):
            self.play(FadeOut(piece_gvt1[4],piece_gvt1[9]),run_time=1/6)
            self.play(FadeIn(piece_gvt1[4],piece_gvt1[9]),run_time=1/6)
        pg1=VGroup(piece_gvt1[4],piece_gvt1[5])
        pg2=VGroup(Vector([0.2*3,0],color=BLUE_E).shift(-RIGHT*4+DOWN),
                   Vector([0,0.4*3],color=RED_E).shift(-RIGHT*4+DOWN))
        self.wait()
        self.play(FadeOut(piece_gvt1[8],piece_gvt1[9],piece_gvt1[10],piece_gvt1[7]),
                  pg1.animate.scale(0.30))
        self.play(pg1.animate.shift(RIGHT*4+DOWN*0.75),
                  FadeIn(pg2))
        self.play(Indicate(piece_gvt1[4]),Indicate(pg2[0]))
        self.wait(0.2)
        self.play(FadeOut(pg1,pg2))

        fx=[Vector([-2,0],color=BLUE_E).shift(DOWN*1.75+RIGHT*0.9),
            Vector([0,4],color=RED_E).shift(DOWN*1.75+RIGHT*0.9)
            ]
        self.play(Create(fx[1]),Write(piece_gvt1[10]))
        self.play(Indicate(fx[1]),Indicate(piece_gvt1[10]))
        fy=[piece_gvt1[10]]#fy and fy
        self.play(FadeOut(fx[1],piece_gvt1[10]))
        self.play(Write(PTF[0].shift(UP*5)))
        PTF.append(MathTex(r'a^{2}','+','b^{2}','=','c^{2}').shift(UP*2))#2
        PTF.append(MathTex(r'\frac{a}{c}'))#3
        PTF.append(MathTex(r'\frac{a}{\sqrt{a^2+b^2}}'))#4
        PTF.append(MathTex(r'\frac{a}{\sqrt{a^2+b^2}}').scale(0.5).shift(UP*2+RIGHT*5))#5
        self.add(PTF[2])
        self.play(ReplacementTransform(PTF[2],PTF[3]))
        self.wait()
        self.play(ReplacementTransform(PTF[3],PTF[4]),FadeOut(PTF[0]))
        self.wait()
        self.play(ReplacementTransform(PTF[4],PTF[5]))
        what=MathTex(r'F_y')
        self.play(FadeIn(what))
        fy.append(MathTex(r'F_y=? \times F'))#1
        self.play(ReplacementTransform(what,fy[1]))
        self.wait()
        fy.append(MathTex(r'F_y=\frac{a}{\sqrt{a^2+x^2} } \cdot F'))#2
        self.play(ReplacementTransform(fy[1],fy[2]))
        self.wait()
        fy.append(MathTex(r'F_y=G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}}'))#3
        self.play(FadeOut(PTF[5]),ReplacementTransform(fy[2],fy[3]))
        self.wait(2)
        piece_gvt1.append(MathTex(r'\sum F=\sum G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}} '))#11
        self.play(ReplacementTransform(fy[3],piece_gvt1[11]))
        piece_gvt1.append(MathTex(r'\int F=\int G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}} '))
        self.wait(0.2)
        self.play(ReplacementTransform(piece_gvt1[11],piece_gvt1[12]))#called int
        piece_gvt1.append(MathTex(r' F=\int G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}}'))
        self.wait(2)
        self.play(ReplacementTransform(piece_gvt1[12],piece_gvt1[13]))#add int symbol
        piece_gvt1.append(MathTex(r' F=\int_{-\frac{l}{2}}^{} G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}}'))
        self.wait()
        self.play(ReplacementTransform(piece_gvt1[13],piece_gvt1[14]))
        piece_gvt1.append(MathTex(r'F=\int_{-\frac{l}{2}}^{\frac{l}{2}} G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}}'))#15
        self.wait()
        self.play(ReplacementTransform(piece_gvt1[14],piece_gvt1[15]))
        self.wait()        

        piece_gvt1.append(MathTex(r'F=\int_{-\frac{l}{2}}^{\frac{l}{2}} G\frac{Mm}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2} }dx'))
        piece_gvt1.append(MathTex(r'F=\int_{-\frac{l}{2}}^{\frac{l}{2}} G\frac{Mma}{l\cdot (a^{2}+x^{2})^{\frac{3}{2} }}dx'))
        piece_gvt1.append(MathTex(r'F=\frac{GMm}{l}\int_{-\frac{l}{2}}^{\frac{l}{2}} \frac{a}{(a^{2}+x^{2})^{\frac{3}{2} }}dx'))
        piece_gvt1.append(MathTex(r'F=\frac{GMma}{l}\int_{-\frac{l}{2}}^{\frac{l}{2}} (a^{2}+x^{2})^{-\frac{3}{2} }dx'))
        piece_gvt1.append(MathTex(r'F=\frac{GMma}{l} \left [\int (a^{2}+x^{2})^{-\frac{3}{2} }dx \right ] _{-\frac{l}{2}}^{\frac{l}{2}}'))
        piece_gvt1.append(MathTex(r'F=\frac{GMm}{l} \left [\frac{x}{a\sqrt{x^2+a^2} }\right ] _{-\frac{l}{2}}^{\frac{l}{2}}'))
        piece_gvt1.append(MathTex(r'F=\frac{2GMm}{al} \left [\frac{x}{\sqrt{x^2+a^2} }\right ] _{0}^{\frac{l}{2}}'))
        piece_gvt1.append(MathTex(r'F=\frac{2GMm}{al} \left [\frac{\frac{l}{2}}{\sqrt{(\frac{l}{2})^2+a^2} }-\frac{0}{\sqrt{0^2+a^2} }\right ]'))
        piece_gvt1.append(MathTex(r'F=\frac{2GMm}{a\sqrt{4a^2+l^2} }'))
        for i in range(15,len(piece_gvt1)-1):
            self.play(ReplacementTransform(piece_gvt1[i],piece_gvt1[i+1]))
        self.wait(3)
        self.play(FadeOut(piece_gvt1[len(piece_gvt1)-1]))


#========================================scene7:end of prob========================================#
        n=0.34
        ca=[[MathTex(r"1^{o}: F_{total}").scale(n).next_to(UP*3.7+LEFT*6,LEFT,buff=0),
            MathTex(r"=\int F_y"),
            MathTex(r"=\int \frac{a}{\sqrt{a^2+x^2} } \cdot F"),
            MathTex(r"=\int G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}G\frac{Mmdx}{l\cdot y^2}"),
            MathTex(r"=\int G\frac{Mmdx}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2}}"),
            MathTex(r'=\int_{-\frac{l}{2}}^{\frac{l}{2}} G\frac{Mm}{l\cdot (a^{2}+x^{2})}\frac{a}{\sqrt{a^2+x^2} }dx'),
            MathTex(r'=\int_{-\frac{l}{2}}^{\frac{l}{2}} G\frac{Mma}{l\cdot (a^{2}+x^{2})^{\frac{3}{2} }}dx'),
            MathTex(r'=\frac{GMm}{l}\int_{-\frac{l}{2}}^{\frac{l}{2}} \frac{a}{(a^{2}+x^{2})^{\frac{3}{2} }}dx'),
            MathTex(r'=\frac{GMma}{l}\int_{-\frac{l}{2}}^{\frac{l}{2}} (a^{2}+x^{2})^{-\frac{3}{2} }dx'),
            MathTex(r'=\frac{GMma}{l} \left [\int (a^{2}+x^{2})^{-\frac{3}{2} }dx \right ] _{-\frac{l}{2}}^{\frac{l}{2}}'),
            MathTex(r'=\frac{GMm}{l} \left [\frac{x}{a\sqrt{x^2+a^2} }\right ] _{-\frac{l}{2}}^{\frac{l}{2}}'),
            MathTex(r'=\frac{2GMm}{al} \left [\frac{x}{\sqrt{x^2+a^2} }\right ] _{0}^{\frac{l}{2}}'),
            MathTex(r'=\frac{2GMm}{al} \left [\frac{\frac{l}{2}}{\sqrt{(\frac{l}{2})^2+a^2} }-\frac{0}{\sqrt{0^2+a^2} }\right ]'),
            MathTex(r'=\frac{2GMm}{a\sqrt{4a^2+l^2} }')
            ]]
        ca.append(
            [MathTex(r'2^o: F_{total}').scale(n).next_to(UP*3.7+RIGHT,LEFT,buff=0),
             MathTex(r'=\int F'),
             MathTex(r'=\int G\frac{Mm}{l\cdot x^2} dx'),
             MathTex(r'=\int_{a}^{a+l} G\frac{Mm}{l\cdot x^2} dx'),
             MathTex(r'=GMml^{-1}\left [ -x^{-1} \right ]_{a}^{a+l}'),
             MathTex(r'=\frac{GMm}{l}\left (\left [ -\frac{1}{x}\right]^{a+l}-\left [ -\frac{1}{x}\right]^{a}\right )'),
             MathTex(r'=\frac{GMm}{l}\left (\left [ -\frac{1}{a+l}\right]-\left [ -\frac{1}{a}\right]\right )'),
             MathTex(r'=\frac{GMm}{l}\left (-\frac{1}{a+l}+\frac{1}{a}\right)'),
             MathTex(r'=\frac{GMm}{l}\left (\frac{1}{a}-\frac{1}{a+l}\right)'),
             MathTex(r'=\frac{GMm}{l}\left (\frac{(a+l)-a}{a(a+l)}\right)'),
             MathTex(r'=\frac{GMm}{l}\frac{l}{a^2+al}'),
             MathTex(r'=\frac{GMm}{a^2+al}')
             ]
        )
        for i in range(1,len(ca[0])):
            ca[0][i].scale(n).next_to(UP*(3.7-(i-1)*((3.7*2)/13))+LEFT*6,RIGHT,buff=0.1)
            if i < len(ca[1]):
                ca[1][i].scale(n).next_to(UP*(3.7-(i-1)*((3.7*2)/13))+RIGHT,RIGHT,buff=0.1)
        ca1=VGroup()
        for i in range(len(ca[0])):
            ca1.add(ca[0][i])
        for i in range(len(ca[1])):
            ca1.add(ca[1][i])
        self.play(Write(ca1),run_time=10)
        self.wait(5)
        self.play(FadeOut(ca1))
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)})
        curve=ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        area = ax.get_area(
            curve,
            x_range=(2, 5),
            color=(GREEN_E,ORANGE),
            opacity=1)
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(Create(area))
        self.play(Write(me[0].shift(UP)))
        ca2=VGroup(ax,curve,area,me[0])
        self.wait(2)
        ca3=VGroup(MathTex(r'\lim ?').shift(UP*-1.7+LEFT*3),
                   MathTex(r'\int ?').shift(UP*1.9+LEFT*1.4),
                   MathTex(r'\sin ?').shift(UP*0.2+LEFT*-3.4),
                   MathTex(r'\cos ?').shift(UP*-0.7+LEFT*-2.5),
                   MathTex(r'\oint ?').shift(UP+LEFT*3.9),
                   MathTex(r'\prod ?').shift(UP*1.2+LEFT*-1.7),
                   )
        self.play(ReplacementTransform(ca2,ca3))
        self.wait()
        self.play(FadeOut(ca3))


#========================================scene8:use of maths========================================#
        variable=[ImageMobject('Detail-Roman-copy-portrait-bust-Aristotle-Greek.jpg').scale(0.3).shift(RIGHT*3)]
        variable.append(Text('Aristotle').scale(0.5).shift(DOWN*2+RIGHT*3))
        self.play(FadeIn(variable[0]))
        self.play(Write(variable[1]))
        variable.append(MathTex(r'x-3=0').shift(LEFT*3))#2
        self.wait(2)
        self.play(Write(variable[2]))
        self.wait()
        variable.append(Vector([0,2],color=RED).shift(RIGHT*2))#3
        variable.append(Vector([0,-2],color=GREEN).shift(RIGHT*2))#4
        variable.append(MathTex('F=3N').next_to(RIGHT*3+UP,RIGHT))#5
        variable.append(MathTex('F=xN').next_to(RIGHT*3+UP*-1,RIGHT))#6
        variable.append(Text('At equilibrium',t2s={'At equilibrium':ITALIC}).scale(0.5).shift(RIGHT*2+UP*3))#7
        self.play(FadeOut(variable[0],variable[1]),
                  Create(variable[3]),Write(variable[5]))
        self.play(Create(variable[4]),Write(variable[6]))
        self.play(Write(variable[7]))
        self.wait(2)
        self.play(FadeOut(variable[3],variable[4],variable[5],variable[6],variable[7],variable[2]))
        self.wait()
        #
        geo=[MathTex('Geometry'),
             Text('Phase Space',t2s={'Phase Space':ITALIC})]
        self.play(Write(geo[0]))
        self.wait(0.2)
        self.play(ReplacementTransform(geo[0],geo[1]))
        self.wait()
        self.play(FadeOut(geo[1]))
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1.5, time_width=0.5)
        self.wait(2)
        self.play(stream_lines.end_animation())
        func1 = lambda pos: np.exp(pos[0]) * UR + np.abs(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(func1, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(flow_speed=1.5, time_width=0.5)
        self.wait(2)
        self.play(stream_lines.end_animation())
        geo.append(VGroup(MathTex(r'\nabla \cdot \mathbf{D} =\rho _f').next_to(UP*1.5+LEFT*2,RIGHT),
                      MathTex(r'\nabla \cdot \mathbf{B} = 0').next_to(UP*0.5+LEFT*2,RIGHT),
                      MathTex(r'\nabla \times  \mathbf{E} = -\cfrac{\partial \mathbf{B}}{\partial t }').next_to(UP*-0.5+LEFT*2,RIGHT),
                      MathTex(r'\nabla \times  \mathbf{H} = \mathbf{J}_f +  \cfrac{\partial \mathbf{D}}{\partial t }').next_to(UP*-1.5+LEFT*2,RIGHT)
        ))
        self.play(Write(geo[2]))
        self.wait(2)
        self.play(FadeOut(geo[2]))
        self.wait()
        #
        la=[Text('Linear Algebra',t2s={'Linear Algebra':ITALIC}),
            Text('Quantum physics',t2s={'Quantum physics':ITALIC}),
            ImageMobject('HEO.jpg').scale(1).shift(RIGHT*4),
            ImageMobject('guangpu.jpg').scale(0.7).shift(RIGHT*4+DOWN*2),
            VGroup(            
            MathTex(r'E_{p}=\int_{r_{n}}^{\infty}{-k\frac{e^2}{r^2}dr}=-\frac{ke^2}{r_{n}}',font_size=35).next_to(UP*2+LEFT*6,RIGHT),#4
            MathTex(r'S_{n}=\frac{\hbar}{2} \quad \varphi_{+}=\left(\begin{array}{l} \cos \frac{\theta}{2} e^{-i \varphi / 2} \\ \sin \frac{\theta}{2} e^{i \varphi / 2} \end{array}\right) ',font_size=35).next_to(UP*0.3+LEFT*6,RIGHT),
            MathTex(r' E(\alpha)=\langle\psi(r, \alpha)|\hat{H}| \psi(r, \alpha)\rangle ',font_size=35).next_to(DOWN*1.4+LEFT*6,RIGHT)
            )
        ]
        self.play(Write(la[0]))
        self.wait(0.2)
        self.play(ReplacementTransform(la[0],la[1]))
        self.play(FadeOut(la[0],la[1]),FadeIn(la[2],la[3]),Write(la[4]))
        self.wait()
        self.play(FadeOut(la[2],la[3],la[4]))
        #
        tp=[Text('Typology',t2s={'Typology':ITALIC}),
            VGroup(
            Text("Gauss' law",t2s={"Gauss' law":ITALIC}).next_to(UP*2+LEFT*6,RIGHT),
            Text("Ampère's law",t2s={"Ampère's law":ITALIC}).next_to(DOWN*2+LEFT*6,RIGHT)
            ),
            Text('vedio here').shift(RIGHT*4),
            MathTex(r'\Phi = \oint_S \vec{E} \cdot \hat{n} dA = \dfrac{q_{enc}}{\epsilon_0}').next_to(UP*2+LEFT*6,RIGHT),
            MathTex(r'\oint \vec{B} \cdot d\vec{l} = \mu_0 I').next_to(DOWN*2+LEFT*6,RIGHT),
            ImageMobject('gl1.jpg').next_to(UP*2+LEFT*6,RIGHT),
            ImageMobject('ap.jpg').next_to(DOWN*2+LEFT*6,RIGHT)
            ]
        self.play(Write(tp[0]))
        self.play(ReplacementTransform(tp[0],tp[1]))
        self.add(tp[2])
        self.wait(2)
        self.play(ReplacementTransform(tp[1][0],tp[3]),ReplacementTransform(tp[1][1],tp[4]))
        self.wait(2)
        self.play(FadeIn(tp[6],tp[5]),FadeOut(tp[4],tp[3]))
        self.wait()
        self.play(FadeOut(tp[6],tp[5],tp[2]))
        self.wait()
        #
class NearEnd(Scene):
    def construct(self):
        intro_inter=[MathTex('Intergration'),            #title
                     MathTex(r'\lim_{\delta x \to 0}\sum_{x=a}^{b} f(x+\frac{\delta x}{2})\delta x')    #formula
                     ]
        intro_inter.append(MathTex(r'\sum'))
        self.play(Write(intro_inter[0]))
        self.wait(2)
        self.play(ReplacementTransform(intro_inter[0],intro_inter[2]))
        self.play(Indicate(intro_inter[2]))
        ax1=VGroup(
            Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 70, 10],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True}))
        ax1.add(ax1[0].plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False))
        ax2=ax1[0].get_riemann_rectangles(
            ax1[1],
            x_range=(2,5),
            dx=0.1,
            color=(BLUE_E,RED),
            stroke_width=0
        )
        ax3=ax1[0].get_riemann_rectangles(
            ax1[1],
            x_range=(2,5),
            dx=0.1,
            color=(BLUE_E,RED),
            stroke_width=0
        )
        ax4=MathTex(r'\int_{2}^{5}x^2dx')
        self.wait()
        self.play(ReplacementTransform(intro_inter[2],ax1))
        self.play(Create(ax2))
        self.add(ax3)
        self.wait()
        self.play(ReplacementTransform(ax2,ax4))
        self.wait()
        self.play(FadeOut(ax4,ax3,ax1))
        self.wait()
        ax5=[MathTex('Mathematics'),
             MathTex('Physics'),
             Dot().shift(UP*2),
             MathTex('Physics')
        ]
        self.play(Write(ax5[0]))
        self.play(ReplacementTransform(ax5[0],ax5[2]))
        self.play(Write(ax5[1]))
        self.play(ReplacementTransform(ax5[2],ax5[3]))
        self.play(Indicate(ax5[1]),Indicate(ax5[3]))
        self.wait()
        self.play(FadeOut(ax5[3],ax5[1]))
        
#========================================scene9:end========================================#
        m='physics'
        end=[
            ImageMobject('p.png').scale(2),
            Text('5 July, 1687, Newton',t2s={'5 July, 1687, Newton':ITALIC}).scale(0.7).shift(DOWN*3),
            MathTex('physics'),#2
            MathTex('physics'),#3
            MathTex('maths',color=YELLOW).shift(UP),#4
            [MathTex('science',color=ORANGE).shift(UP*2+RIGHT*4),MathTex(m,color=ORANGE).shift(UP*2+RIGHT*4)],#5
            [MathTex('chemistry',color=GREEN).shift(DOWN*2.8+LEFT*2),MathTex(m,color=GREEN).shift(DOWN*2.8+LEFT*2)],#6
            [MathTex('philosophy',color=BLUE).shift(UP*2.4+LEFT*3.4),MathTex(m,color=BLUE).shift(UP*2.4+LEFT*3.4)],#7
            [MathTex('mathematics',color=RED).shift(DOWN*1.6+RIGHT*4.6),MathTex(m,color=RED).shift(DOWN*1.6+RIGHT*4.6)],#8
            MathTex('science',color=ORANGE).shift(UP*2+RIGHT*4),#9
        ]
        self.play(FadeIn(end[0]))
        self.play(Write(end[1]))
        self.wait()
        self.play(FadeOut(end[1],end[0]),Write(end[2]),Write(end[5][0]))
        self.add(end[3])
        self.wait()
        self.play(ReplacementTransform(end[2],end[4]))
        self.play(end[4].animate.shift(UP*0.6+RIGHT*3.6))
        self.play(ReplacementTransform(end[4],end[9]))
        self.wait()
        self.play(FadeOut(end[9]))
        for i in range(6,9):
            self.play(GrowFromCenter(end[i][0]))
        self.wait()
        for i in range(5,9):
            self.play(ReplacementTransform(end[i][0],end[i][1]))
        self.wait()
        self.play(FadeOut(end[5][1],end[6][1],end[7][1],end[8][1]))
        self.play(FadeOut(end[3]))
        
        end.append(Text('物理'))
        end.append(Text('  物  理'))
        end.append(Text('万  之  ').shift(LEFT*0.67))
        self.play(Write(end[10]))
        self.wait()
        self.play(ReplacementTransform(end[10],end[11]))
        self.play(FadeIn(end[12],shift=UP))
        self.wait()
        end1=VGroup(end[11],end[12])
        end2=Text('研究一切的物质的学科')
        end3=ImageMobject('sky.jpg')
        self.play(ReplacementTransform(end1,end2))
        self.wait(2)
        self.play(FadeIn(end3))
        self.wait()
        self.play(FadeOut(end3))

class Axes3DExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        dot_1 = Dot3D(point=axes.coords_to_point(3, 0, 0), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(4, 0, 0), color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.play(FadeIn(dot_1, dot_2,dot_3))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.play(Rotate(dot_1, PI * 4, about_point=ORIGIN, axis=OUT,rate_func=linear),
                  Rotate(dot_2,-PI * 4, about_point=ORIGIN, axis=OUT,rate_func=linear),
                  run_time=5)
        self.play(FadeOut(dot_1, dot_2,dot_3))
        
class EndKill(Scene):
    def construct(self):
        ek=MathTex('accurate').shift(RIGHT*0.2)
        ek1=MathTex('in').shift(LEFT*1)
        self.play(Write(ek))
        for i in range(5):
            self.play(FadeIn(ek1),run_time=0.4)
            self.play(FadeOut(ek1),run_time=0.4)
        self.play(FadeOut(ek))
        ek2=MathTex('PHYSICS')
        self.play(Write(ek2))
        self.wait()
        self.play(Indicate(ek2))
        self.wait()
        self.play(FadeOut(ek2))


class Rf(Scene):
    def construct(self):
        t=Text('Reference List').next_to(LEFT*7,RIGHT).shift(DOWN*-2)
        t1=Text('\t\tSeanIXz (2022). 如何让你的银河绚丽多彩. [online] 知乎专栏. Available\n at: https://zhuanlan.zhihu.com/p/187686728 [Accessed 23 Aug. 2023].\n\n\t\t3blue1brown (2019). videos/_2019/diffyq/part1/phase_space.py at master\n · 3b1b/videos. [online] GitHub. Available at: https://github.com/3b1b/videos/\nblob/master/_2019/diffyq/part1/phase_space.py#L1840 [Accessed 23 Aug. 202\n3].\n\n\t\tAmadio, A.H. and Kenny, A.J.P. (2019). Aristotle | Biography, Contributions, \n& Facts. In: Encyclopedia Britannica. [online] Available at: https://www.britannica.\ncom/biography/Aristotle [Accessed 23 Aug. 2023].\n\n\t\tKhan Academy. (2016). Heisenberg uncertainty principle. [online] Available \nat: https://www.khanacademy.org/science/physics/quantum-physics/quantum-\nnumbers-and-orbitals/v/heisenberg-uncertainty-principle [Accessed 23 Aug. 2023].\n\n\t\tManim Community (n.d.). Example Gallery. [online] Manim Community |\n Documentation. Available at: https://docs.manim.community/en/stable/\nexamples.html [Accessed 23 Aug. 2023].\n\n\t\tMatrix Force Method. (2008). Available at: http://www.iust.ac.ir/files/\ncefsse/pg.cef/Contents/force_method_ch6.pdf [Accessed 23 Aug. 2023].\n\n\t\toxfordscholastica (2020). Newton And Leibniz: The Fathers Of Calculus. \n[online] Oxford Summer School 2021: study in the historic university city of Oxford.\n Available at: https://www.oxfordscholastica.com/blog/newton-and-leibniz-the-\nfathers-of-calculus/ [Accessed 23 Aug. 2023].\n\n\t\tSimon, D.S. (2018). Topology and physics: a historical overview. [online] \niopscience.iop.org. Available at: https://iopscience.iop.org/book/mono/978-1-\n64327-234-4/chapter/bk978-1-64327-234-4ch1 [Accessed 23 Aug. 2023].\n\n\t\tStrang, G. and Herman, E. (2016). 6.5: Physical Applications of Integration. \n[online] Mathematics LibreTexts. Available at: https://math.libretexts.org/\nBookshelves/Calculus/Calculus_(OpenStax)/06%3A_Applications_of_\nIntegration/6.05%3A_Physical_Applications_of_Integration#:~:text=6.5%3A%\n20Physical%20Applications%20of%20Integration%201%20Mass%20\nand [Accessed 23 Aug. 2023].\n\n\t\tWikipedia Contributors (2019). Philosophiæ Naturalis Principia Mathematica.\n [online] Wikipedia. Available at: https://en.wikipedia.org/wiki/Philosophi\n%C3%A6_Naturalis_Principia_Mathematica [Accessed 23 Aug. 2023].\n\n\t\twww.latexlive.com. (n.d.). 在线LaTeX公式编辑器-编辑器. [online] Available at: \nhttps://www.latexlive.com/ [Accessed 23 Aug. 2023].\n\n\t\t月影 (2021). 经典原子模型（从汤姆逊到玻尔）. [online] 知乎专栏. Available at: \nhttps://zhuanlan.zhihu.com/p/445616443 [Accessed 23 Aug. 2023].',
                font_size=27,
                line_spacing=1.1
                ).next_to(LEFT*7,RIGHT).shift(DOWN*10)
        t2=VGroup(t,t1).shift(DOWN*10)
        self.add(t2)
        self.play(t2.animate.shift(UP*50),rate_functions=linear,run_time=30)


class fengmian(Scene):
    def construct(self):
        ax1=VGroup(
            Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 70, 10],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True}))
        ax1.add(ax1[0].plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False))
        ax1.add(ax1[0].get_riemann_rectangles(
            ax1[1],
            x_range=(2,5),
            dx=0.1,
            color=(BLUE_E,RED),
            stroke_width=0
        ))
        la=[Text('Linear Algebra',t2s={'Linear Algebra':ITALIC}),
            Text('Quantum physics',t2s={'Quantum physics':ITALIC}),
            ImageMobject('HEO.jpg').scale(1).shift(LEFT*4+UP*1.5),
            ImageMobject('guangpu.jpg').scale(0.7).shift(LEFT*4+UP*-0.5),
            VGroup(            
            MathTex(r'E_{p}=\int_{r_{n}}^{\infty}{-k\frac{e^2}{r^2}dr}=-\frac{ke^2}{r_{n}}',font_size=35).next_to(UP*2+LEFT*6,RIGHT),#4
            MathTex(r'S_{n}=\frac{\hbar}{2} \quad \varphi_{+}=\left(\begin{array}{l} \cos \frac{\theta}{2} e^{-i \varphi / 2} \\ \sin \frac{\theta}{2} e^{i \varphi / 2} \end{array}\right) ',font_size=35).next_to(UP*0.3+LEFT*6,RIGHT),
            MathTex(r' E(\alpha)=\langle\psi(r, \alpha)|\hat{H}| \psi(r, \alpha)\rangle ',font_size=35).next_to(DOWN*1.4+LEFT*6,RIGHT)
            )
        ]
        ax1.scale(0.5).shift(DOWN*2+RIGHT*3)
        self.add(ax1)
        self.add(Text('Integration').scale(2).shift(UP*2+RIGHT*3))
        self.add(MathTex(r'\int_2^5{x^2}').scale(2).shift(UP*-0.5+RIGHT*2.5))
        self.add(la[2],la[3])
        self.add(MathTex(r'\lim_{\delta x \to 0}\sum_{x=a}^{b} f(x+\frac{\delta x}{2})\delta x').shift(DOWN*2+LEFT*4))
