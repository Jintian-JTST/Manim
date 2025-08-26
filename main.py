from manim import *

#config.background_color = "#22125E"  # 黑色背景
class MinecraftIntroAbstract(Scene):
    def construct(self) -> None:
        # ===================== 分镜1：Minecraft三维度引入 =====================
        # 3个抽象维度方块（替代文字）
        overworld = [Square(side_length=2, fill_color=GREEN, fill_opacity=0.8, color=GREEN),
                     ImageMobject(r'.\Grass_Block_JE7_BE6.png')]  # 主世界（绿色方块）
        nether = [Square(side_length=2, fill_color=RED, fill_opacity=0.8, color=RED), 
                  ImageMobject(r'.\Netherrack_JE4_BE2.png')]        # 下界（红色方块）
        the_end = [Square(side_length=2, fill_color=PURPLE, fill_opacity=0.8, color=PURPLE),
                   ImageMobject(r'.\End_Stone_JE3_BE2.png')] # 末地（紫色方块）

        # 初始位置（从屏幕下方飞入）
        overworld[1].move_to(LEFT * 3)
        nether[1].move_to(ORIGIN)
        the_end[1].move_to(RIGHT * 3)

        # 动画：3个方块依次飞入并悬浮
        self.play(
            FadeIn(overworld[1], nether[1], the_end[1]),
            run_time=1.5
        )
        self.wait(0.5)

        # 强调末地（对应演讲稿："The End应该是最令人惊讶的"）
        #end_highlight = SurroundingRectangle(the_end[1], color=YELLOW, buff=0.3, stroke_width=4)
        self.play(
            #Create(end_highlight),
            Indicate(the_end[1]), # 末地放大+变黄（突出）
            run_time=1
        )
        self.wait(2)

        self.remove(*overworld, *nether, *the_end)

        # ===================== 分镜1.5：地球图标旋转 =====================

        Earth=Text('🌏').scale(3).set_color(BLUE)
        qu=Text('🧐').scale(1.5).set_color(YELLOW).shift(RIGHT*5+DOWN*2)
        self.add(Earth,qu)
        self.play(Rotate(Earth,angle=PI*2,rate_func=linear, run_time=4))
        self.remove(Earth,qu)

        # ===================== 分镜1.6：末地图标出现 =====================
        ve=Text('💻').scale(2).shift(RIGHT*3.5+UP*2)
        self.play(Write(ve))
        self.wait(3)
        self.play(FadeOut(ve))



class Binary(Scene):
    def construct(self):
        # ===================== 分镜1：二进制数字出现 =====================
        '''Binaries, used commonly in every computer, can represent numbers and values by the on and off of anything, e.g., lights, switches, etc..'''
        num=[np.random.randint(0, 2) for _ in range(20)]
        binary_numbers = VGroup(*[
            Tex(str(num[_]), font_size=48, color=WHITE)
            for _ in range(20)
        ])
        for _ in range(20):
            if num[_]==1:
                binary_numbers[_].set_color(YELLOW)
            else:
                binary_numbers[_].set_color(GRAY)
        binary_numbers.arrange_in_grid(rows=4, cols=5, buff=0.7).move_to(ORIGIN)

        # 动画：二进制数字从屏幕上方飞入
        self.play(
            FadeIn(binary_numbers, shift=UP),
            run_time=2
        )
        self.wait(2)
        binary_number= VGroup(*[
            Text('')
            for _ in range(20)
        ])

        for i in range(20):
            if num[i]==1:
                binary_number[i]=Text('💡', font_size=40, color=YELLOW)
            else:
                binary_number[i]=Text('💡', font_size=40, color=GRAY)
        binary_number.arrange_in_grid(rows=4, cols=5, buff=0.5).move_to(ORIGIN)

        # 清除屏幕上的二进制数字
        self.remove((binary_numbers)).add(binary_number)
        self.wait(1)


        binary_number1= VGroup(*[
            Text('')
            for _ in range(20)
        ])

        for i in range(20):
            if num[i]==1:
                binary_number1[i]=Text('⚪', font_size=40, color=GREEN)
            else:
                binary_number1[i]=Text('⚪', font_size=40, color=RED)
        binary_number1.arrange_in_grid(rows=4, cols=5,buff=(0.25,0.5)).move_to(ORIGIN)
        self.remove((binary_number)).add(binary_number1)
        self.wait(1)

        bin = Text('Binary Numbers').scale(1.5)
        self.play(ReplacementTransform(binary_number1, bin))

        tower1 = Text('Binary Numbers', color=PURPLE)
        tower2 = Text('Logic Gates', color=BLUE)
        tower3 = Text('Operators', color=GREEN)
        tower4 = Text('Units', color=YELLOW)
        tower5 = Text('CPU', color=RED)
        tower = VGroup(tower5, tower4, tower3, tower2, tower1)
        tower.arrange_in_grid(rows=5, buff=0.5)

        self.wait()
        self.play(ReplacementTransform(bin, tower1), FadeIn(tower2, tower3, tower4, tower5))

        # 使用LaggedStart依次高亮每个部分
        self.play(LaggedStart(
            Indicate(tower1,run_time=0.5),
            Indicate(tower2,run_time=0.5),
            Indicate(tower3,run_time=0.5),
            Indicate(tower4,run_time=0.5),
            Indicate(tower5,run_time=0.5),
            lag_ratio=0.1 # 每个动画间隔0.5秒
        ))
        #Shade = Rectangle(height=10, width=20, fill_color=BLACK, fill_opacity=0.8,stroke_width=0)
        jjcc=VGroup(MathTex(r'+').scale(2),
                    VGroup(MathTex(r'-').scale(2),
                    MathTex(r'\times').scale(2),
                    MathTex(r'\div').scale(2))
                    )
        jjcc[1].arrange_in_grid(cols=3,buff=0.5)
        jjcc.arrange_in_grid(cols=2,buff=0.5)
        self.wait()
        self.play(FadeOut(tower1,tower3,tower4,tower5), 
                  ReplacementTransform(tower2,jjcc))
        self.wait(3)
        self.play(Blink(jjcc[0],run_time=0.5))
        self.wait()
        self.play(Blink(jjcc[1][0],run_time=0.5))
        self.wait()
        self.play(Blink(jjcc[1][1],run_time=0.5))
        self.wait()
        self.play(Blink(jjcc[1][2],run_time=0.5))
        self.wait()
        add=Text('Addition').shift(RIGHT*0.5)
        self.play(ReplacementTransform(jjcc[1],add))
        self.wait(5)
        # ...之前的代码...

        # 创建 A 列表
        A = [
            MathTex(r'0+0=', r'0').shift(UP*2),
            MathTex(r'0+1=', r'1').shift(UP*1),
            MathTex(r'1+0=', r'1').shift(UP*-1),
            MathTex(r'1+1=', r'0').shift(UP*-2),
            MathTex(r'1', color=YELLOW)
        ]
        A[-1].scale(0.5).next_to(A[-2], DOWN).shift(RIGHT)
        for _ in A:
            if _ ==A[-1]:
                self.play(TransformFromCopy(A[-2],_))
            else:
                self.play(TransformFromCopy(add,_))
        self.wait()
        self.play(FadeOut(add,jjcc[0]),
                  (A[_].animate.shift(DOWN*0.5) for _ in [0,1]),
                  (A[_].animate.shift(DOWN*-0.5) for _ in [-3,-2]))        # 创建 B - A 的副本，但每个元素的最后一项变为蓝色

        # 动画：将 A 变换为 B，强调 sum bits
        sum_text = Text('Sum Bits', color=BLUE).shift(UP*3)
        carry_text = Text('Carry Bits', color=PURPLE).shift(UP*-3)
        B=[
            Rectangle(color=BLUE,height=4,width=1).shift(RIGHT*0.75)
        ]
        # 播放动画
        self.play(
            Write(sum_text),
            Create(B[0])
        )
        self.wait(2)

        # 强调 carry bit
        self.play(
            Circumscribe(A[-1],color=PURPLE,),
            Write(carry_text),
        )
        self.wait(5)
        

class sub(Scene):
    def construct(self) -> None:
        sub=Title('Substraction')
        self.play(Write(sub))
        self.wait(3)
        # 直接创建 "Addition?" 文本
        add_text = Text('Addition?').scale(1.5)
        self.play(Write(add_text))
        self.wait(1)
        
        # 翻转动画
        self.play(
            Rotate(
                add_text,
                angle=PI,  # 180度翻转
                axis=UP,   # 绕Y轴翻转
                run_time=1.5
            )
        )
        self.wait(0.5)
        
        # 淡出动画
        self.play(FadeOut(add_text))
        self.wait(1)
        S = [
            MathTex(r'0-0=', r'0').shift(UP*1.5),
            MathTex(r'1-0=', r'1').shift(UP*0.5),
            MathTex(r'1-1=', r'0').shift(UP*-0.5),
            MathTex(r'0-1=', r'1').shift(UP*-1.5),
            MathTex(r'1', color=YELLOW)
        ]
        S[-1].scale(0.5).next_to(S[-2], DOWN).shift(RIGHT)
        for _ in S:
            self.play(Write(_))
            self.wait(0.5)
        self.wait(5)
        self.play(FadeOut(*self.mobjects), FadeIn(Text('Complements')))        
        self.wait(5)



class comp(Scene):
    def construct(self):
        com = Text("Complements")
        com1 = com.copy()
        self.add(com)
        
        # 创建下划线
        underline = Line(LEFT, RIGHT)
        underline.width = config["frame_width"] - 2
        com1.to_edge(UP)        
        underline.next_to(com1, DOWN)
        
        # 移动文本到顶部并创建下划线
        self.play(
            com.animate.to_edge(UP),
            Create(underline)
        )
        self.wait()

        # 创建两种补码的表示
        C = []
        C.append(Tex(r"One", r"'s Complement").shift(UP*0.5))
        C[0][0].set_color(BLUE)
        C.append(Tex(r"Two", r"'s Complement").shift(UP*-0.5))
        C[-1][0].set_color(GOLD)

        self.play(TransformFromCopy(com, C[0]))
        self.play(TransformFromCopy(com, C[1]))
        self.wait(2)
        self.play(FadeOut(*C))
        
        # 创建8位二进制数
        original_bits = ["1", "0", "1", "0", "1", "1", "0", "0"]
        original_group = VGroup()
        complement_group = VGroup()
        
        # 创建原码
        for i, bit in enumerate(original_bits):
            orig_bit = Tex(bit, font_size=36, color=GREEN if int(bit)==0 else PINK)
            orig_bit.shift(LEFT * (3.5 - i) * 0.8 + UP * 1.0)
            original_group.add(orig_bit)
        
        # 创建反码（直接反转） - 放在场景中央
        for i, bit in enumerate(original_bits):
            comp_bit = Tex("0" if bit == "1" else "1", font_size=36, color=BLUE)
            comp_bit.shift(LEFT * (3.5 - i) * 0.8)  # 放在ORIGIN位置
            complement_group.add(comp_bit)
        
        # 添加标签
        original_label = Tex(r"Original Value").scale(0.75).next_to(original_group, LEFT, buff=0.3)
        complement_label = Tex(r"One", r"'s Complement").scale(0.75).next_to(complement_group, LEFT, buff=0.3)
        complement_label[0].set_color(BLUE)

        # 显示原码和反码
        self.play(
            Write(original_group),
            Write(original_label),
        )
        
        # 添加箭头连接每一位
        arrows = VGroup()
        for i in range(len(original_bits)):
            arrow = Arrow(
                start=original_group[i].get_bottom(),
                end=complement_group[i].get_top(),
                buff=0.1,
                max_tip_length_to_length_ratio=0.15,
                color=GREEN if int(original_bits[i])==0 else PINK
            )
            arrows.add(arrow)
        self.play(Create(arrows),Write(complement_group),
            Write(complement_label))
        self.wait()
        self.play(FadeOut(arrows))
        
        # 添加2's complement
        # 创建2's complement结果 (01010100)
        result_bits = ["0", "1", "0", "1", "0", "1", "0", "0"]
        result_group = VGroup()
        
        for i, bit in enumerate(result_bits):
            result_bit = Tex(bit, font_size=36)
            result_bit.shift(LEFT * (3.5 - i) * 0.8 + DOWN * 1.0)  # 放在下方
            result_group.add(result_bit)
        
        # 显示加1操作
        plus_one = MathTex("+", "1", font_size=36).next_to(complement_group, RIGHT, buff=0.5)
        self.play(Write(plus_one))
        
        # 逐步展示加1过程
        # 从最低位开始加1
        self.play(
            plus_one[1].animate.set_color(RED)
        )
        
        # 最低位加1：1 + 1 = 0，进位1
        self.play(
            TransformFromCopy(complement_group[7], result_group[7]),
            FadeOut(plus_one)
        )
        
        # 显示进位
        carry = Tex(r"1", font_size=24, color=RED).next_to(complement_group[6], DOWN, buff=0.1)
        self.play(Write(carry))
        
        # 第二位：1 + 1 = 0，进位1
        self.play(
            carry.animate.next_to(complement_group[5], DOWN, buff=0.1),
            TransformFromCopy(complement_group[6], result_group[6]),
        )
        
        # 第三位：0 + 1 = 1，无进位
        self.play(
            carry.animate.next_to(complement_group[4], DOWN, buff=0.1),
            TransformFromCopy(complement_group[5], result_group[5]),
            FadeOut(carry)  # 进位用完
        )
        
        # 剩余的位直接复制
        self.play(
            AnimationGroup(TransformFromCopy(complement_group[i], result_group[i]) for i in range(5)),
            run_time=0.5
        )
        
        # 添加最终标签
        result_label = Tex(r"Two", r"'s Complement").scale(0.75).next_to(result_group, LEFT, buff=0.3)
        result_label[0].set_color(GOLD)
        
        # 将结果组变为金色
        self.play(
            result_group.animate.set_color(GOLD),
            Write(result_label)
        )
        comlist=[result_label,complement_label,original_label]
        # 在最后添加问号表情
        self.wait(5)
        qu = Text('🧐?').scale(1.5).set_color(YELLOW).to_corner(DR)
        self.play(
            GrowFromEdge(qu, RIGHT),
            FadeOut(*[mob for mob in self.mobjects if mob not in comlist ]),
            (comlist[_].animate.scale(1/0.75).move_to(ORIGIN+(_-1)*UP) for _ in range(len(comlist)))
        )

        self.wait(2)
        sub=Tex(r'Subtraction')
        eq=Tex(r'=').rotate(PI/2)
        rst_label = Tex(r"Two", r"'s Complement")
        rst_label[0].set_color(GOLD)
        add=Tex(r'+')
        ad=Tex(r"Addition")
        sqeaa=VGroup(sub,eq,rst_label,add,ad)
        sqeaa.arrange(DOWN,buff=0.3)
        self.play(
            Unwrite(qu),
            ReplacementTransform(result_label, rst_label),
            FadeIn(sqeaa[0],sqeaa[1],sqeaa[3],sqeaa[4]),
            FadeOut(complement_label,original_label)
        )
        self.wait(10)


class minus(Scene):
    def construct(self):
        # 初始化方程列表
        equation = [
            MathTex(r'5', r'-', r'3', r'=', r'?'),  # 0
            MathTex(r'101', r'-', r'011', r'=', r'?').shift(UP*2),  # 1
        ]
        
        # 显示初始方程
        self.play(Write(equation[0]))
        self.play(equation[0].animate.shift(UP*2))
        self.wait()
        
        # 转换为二进制方程
        self.play(ReplacementTransform(equation[0], equation[1]))
        self.wait(2)
        
        # 展示3的二进制表示
        minus_number = MathTex(r"011").next_to(equation[1], DOWN, buff=1.0)
        self.play(TransformFromCopy(equation[1][2], minus_number))

        # 计算1's complement
        ones_complement = MathTex(r"100").next_to(minus_number, DOWN, buff=0.5).set_color(BLUE)
        flip_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                start=minus_number[0][i].get_bottom(),
                end=ones_complement[0][i].get_top(),
                buff=0.1,
                color=YELLOW
            )
            flip_arrows.add(arrow)
        
        self.play(
            Create(flip_arrows),
            Write(ones_complement)
        )
        self.wait()
        
        # 计算2's complement
        add_one = MathTex(r'+1').next_to(ones_complement, RIGHT, buff=0.2)
        twos_complement = MathTex(r"101").next_to(ones_complement, DOWN, buff=0.5)
        twos_complement.set_color(GOLD)
        self.play(Write(add_one))
        self.play(TransformFromCopy(ones_complement, twos_complement))
        self.wait()
        
        # 展示5 + 3的2's complement
        equation.append(MathTex(r'101', r'+', r'101', r'=', r'?').shift(UP*2))  # 3
        self.play(
            ReplacementTransform(equation[1], equation[2]),
            ReplacementTransform(twos_complement, equation[2][2]),
            FadeOut(add_one, ones_complement, flip_arrows, minus_number)
        )
        self.play(Wiggle(equation[2][2]))
        self.wait()
        
        # 高亮加法方程
        self.play(LaggedStart(
            Indicate(equation[2][0], run_time=0.5),
            Indicate(equation[2][1], run_time=0.5),
            Indicate(equation[2][2], run_time=0.5),
            Indicate(equation[2][3], run_time=0.5),
            lag_ratio=0.1
        ))
        
        # 显示加法结果（带进位）
        equation.append(MathTex(r'101', r'+', r'101', r'=1', r'010').shift(UP*2))  # 4
        self.play(ReplacementTransform(equation[2], equation[3]))
        
        # 显示完整结果
        equation.append(MathTex(r'101', r'+', r'101', r'=', r'1', r'010').shift(UP*2))  # 5
        self.add(equation[4])
        self.remove(equation[3])
        
        # 添加负号表示省略进位
        no = MathTex(r'-').move_to(equation[4][4].get_center())
        self.wait()
        self.play(Write(no))
        self.wait()
        
        # 返回带进位的结果
        self.add(equation[3])
        self.remove(equation[4])
        
        # 显示最终结果（省略进位）
        equation.append(MathTex(r'101', r'+', r'101', r'=', r'010').shift(UP*2))  # 6
        self.play(FadeOut(no), ReplacementTransform(equation[3], equation[5]))
        
        # 放大最终结果
        self.play(equation[5].animate.scale(2).move_to(ORIGIN))
        
        # 显示十进制结果
        equation.append(MathTex(r'5', r'-', r'3', r'=', r'2').scale(2))  # 7
        self.play(ReplacementTransform(equation[5], equation[6]))
        
        # 高亮结果
        self.play(Circumscribe(equation[6][-1], shape=Circle))
        
        # 缩小结果
        self.play(equation[6].animate.scale(0.5))
        self.wait()
        
        # 移动最终结果到原点
        equation.append(MathTex(r'101', r'+', r'101', r'=', r'010'))  # 8
        self.play(ReplacementTransform(equation[6], equation[7]))
        self.wait()
        
        # 添加详细加法表达式
        equation.append(MathTex(r'1', r'0', r'1', r'+', r'1', r'0', r'1', r'=', r'0', r'1', r'0'))  # 8
        self.add(equation[8])
        self.remove(equation[7])
        
        # 高亮第一个加数
        self.play(LaggedStart(
            Indicate(equation[8][0]),
            Indicate(equation[8][1]),
            Indicate(equation[8][2]),
            lag_ratio=0.25
        ))
        self.wait()
        
        # 高亮第二个加数
        self.play(LaggedStart(
            Indicate(equation[8][4]),
            Indicate(equation[8][5]),
            Indicate(equation[8][6]),
            lag_ratio=0.25
        ))
        self.wait()
        
        # 高亮结果
        self.play(LaggedStart(
            Indicate(equation[8][8]),
            Indicate(equation[8][9]),
            Indicate(equation[8][10]),
            lag_ratio=0.25
        ))
        self.wait()



class ComputerMemory(Scene):
    def construct(self):
        # 创建计算机方框
        computer = Rectangle(width=5, height=3, color=BLUE, fill_opacity=0.2, fill_color=BLUE)
        c=Text('Computer').scale(0.5).next_to(computer,DOWN)
        self.play(Create(computer), GrowFromEdge(c,UP),run_time=1.5)

        # 创建内存芯片图案 (修复三维坐标问题)
        memory_chip = VGroup(
            Rectangle(width=0.8, height=1.2, fill_opacity=0.3, fill_color=GREY),
            *[Line(
                start=[-0.4, 0.5 - i*0.2, 0],
                end=[0.4, 0.5 - i*0.2, 0]
            ) for i in range(6)]
        )
        m=Text('RAM').scale(0.7)
        memory_chip.scale(0.7).shift(computer.get_center() + RIGHT*4)
        m.next_to(memory_chip)
        self.play(DrawBorderThenFill(memory_chip), GrowFromEdge(m,RIGHT), run_time=1)
        
        # 创建补码数据 (使用网格自动排列)
        complements = [
            Text("10110101", font="Monospace", font_size=24),
            Text("11100011", font="Monospace", font_size=24),
            Text("10001101", font="Monospace", font_size=24),
            Text("11011010", font="Monospace", font_size=24),
            Text("10101011", font="Monospace", font_size=24),
            Text("10101010", font="Monospace", font_size=24),
            Text("......", font="Monospace", font_size=36),
            Text("......", font="Monospace", font_size=36),
        ]
        
        # 使用网格布局自动排列数据[4](@ref)
        comp_group = VGroup(*complements).arrange_in_grid(
            rows=4, cols=2, 
            buff=(0.5, 0.3),
            cell_alignment=ORIGIN
        )
        comp_group.move_to(computer.get_center())
        
        # 显示所有数据
        self.play(FadeIn(comp_group))
        self.wait(0.5)
        
        # 创建黄色高亮框并遍历所有补码
        highlight = SurroundingRectangle(complements[0], color=YELLOW, buff=0.1, stroke_width=2)
        self.play(Create(highlight), run_time=0.5)
        
        # 依次高亮每个数据
        for i in range(1, len(complements)-2):
            self.play(
                highlight.animate.become(
                    SurroundingRectangle(complements[i], color=YELLOW, buff=0.1, stroke_width=2)
                ),
                run_time=0.3
            )
            self.wait(0.1)
        
        # 最终展示
        self.play(FadeOut(highlight))
        self.wait(10)






class BinaryTable(Scene):
    def construct(self):
        # 表格数据（所有值转为字符串是关键修复）
        table_data = [
            ["\mathrm{Bin.}","\mathrm{Dec.}","\mathrm{1's.}","\mathrm{2's.}"],
            ["0000", "0", "0", "0"],
            ["0001", "1", "1", "1"],
            ["0010", "2", "2", "2"],
            ["0011", "3", "3", "3"],
            ["0100", "4", "4", "4"],
            ["0101", "5", "5", "5"],
            ["0110", "6", "6", "6"],
            ["0111", "7", "7", "7"],
            ["1000", "8", "-7", "-8"],
            ["1001", "9", "-6", "-7"],
            ["1010", "10", "-5", "-6"],
            ["1011", "11", "-4", "-5"],
            ["1100", "12", "-3", "-4"],
            ["1101", "13", "-2", "-3"],
            ["1110", "14", "-1", "-2"],
            ["1111", "15", "-0", "-1"]
        ]

        # 创建紧凑表格（关键优化）
        table = MathTable(
            table_data,
            # 紧凑布局参数
            h_buff=0.1,  # 水平间距减少25%
            v_buff=0.1,  # 垂直间距减少25%
            include_outer_lines=False,
            line_config={"stroke_width": 0},
            arrange_in_grid_config={"cell_alignment": ORIGIN}
            ).to_edge(LEFT)

        for row in table.get_rows():
            for cell in row:
                cell.set(font_size=26)

        # 动画序列
        self.play(LaggedStart(
            *(Write(i,run_time=0.5) for i in table.get_rows()),lag_ratio=0.25
        ), run_time=2)

        # 获取第三列所有单元格（索引从0开始，第三列索引为2）
        # 设置整列颜色为黄色（通过动画渐变）
        self.play(
            table.get_columns()[2].animate.set_color(BLUE),
        )
        self.wait(1)
        self.play(
            table.get_columns()[3].animate.set_color(GOLD),
        )
        self.wait(1)


        # 获取目标单元格（第12行数据，索引11）
        target_row = 11  # 1011所在行
        decimal_cell = table.get_cell((target_row+1, 2))  # 11的位置
        ones_comp_cell = table.get_cell((target_row+1, 3))  # -4的位置
        twos_comp_cell = table.get_cell((target_row+1, 4))  # -5的位置
        dec1=MathTex(r"\mathrm{Dec.}-15=\mathrm{1's.}")
        dec2=MathTex(r"\mathrm{Dec.}-16=\mathrm{2's.}")
        dec=VGroup(dec1,dec2).arrange(DOWN,0.5).scale(0.75).move_to(RIGHT*2+UP*2)
        # 创建两个方框（11和-4）
        box1 = SurroundingRectangle(decimal_cell, color=YELLOW, buff=0.1)
        box2 = SurroundingRectangle(ones_comp_cell, color=RED, buff=0.1)
        box=VGroup(box1,box2)
        # 动画1：方框出现在11和-4上
        self.play(Create(box1), Create(box2))
        self.play(TransformFromCopy(box,dec[0]))
        
        # 动画2：-4的方框移动到-5的位置
        self.play(
            box2.animate.move_to(twos_comp_cell).set_color(GREEN),
            run_time=1.5,
            rate_func=smooth
        )
        self.play(TransformFromCopy(box,dec[1]))
        
        # 清理动画
        self.play(FadeOut(box1), FadeOut(box2))
        self.wait(0.5)

        zeros =  SurroundingRectangle(table.get_cell((17, 3)), color=PINK, buff=0.1)
        zero1 =  SurroundingRectangle(table.get_cell((17, 4)), color=PINK, buff=0.1)
        zero =   SurroundingRectangle(table.get_cell((2, 3)), color=PINK, buff=0.1)

        self.play(Create(zero),Create(zeros))
        self.wait(3)
        self.play(zeros.animate.become(zero1))
        self.wait(5)





class clk(Scene):
    def construct(self):
        # 创建时钟表格数据
        table_data = [
            ["\mathrm{Clock}","\mathrm{1's.}","\mathrm{2's.}"],
            ["12", "0", "0"],
            ["1", "1", "1"],
            ["2", "2", "2"],
            ["3", "3", "3"],
            ["4", "4", "4"],
            ["5", "5", "5"],
            ["6", "-5", "-6"],
            ["7", "-4", "-5"],
            ["8", "-3", "-4"],
            ["9", "-2", "-3"],
            ["10", "-1", "-2"],
            ["11", "-0", "-1"]
        ]

        # 创建紧凑表格
        table = MathTable(
            table_data,
            arrange_in_grid_config={"cell_alignment": ORIGIN},
            h_buff=0.15,
            v_buff=0.15,
            include_outer_lines=False,
            line_config={"stroke_width": 0}
        ).scale(0.8).to_edge(LEFT)

        # 设置字体大小
        for row in table.get_rows():
            for cell in row:
                cell.set(font_size=24)
        
        
        
        
        clock = Circle(radius=2, color=WHITE)
        # 创建时钟
        # 创建时钟数字（12在顶部，顺时针排列1-11）
        numbers = VGroup()
        for i in range(12):
            # 计算角度：从顶部开始顺时针排列
            angle = i * -TAU/12 + PI/2  # 关键修改：使用负角度实现顺时针排列
            
            # 计算位置
            position = 1.7 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 显示数字（12在最顶部）
            if i == 0:
                num = MathTex("12", font_size=36).move_to(position)
            else:
                num = MathTex(str(i), font_size=36).move_to(position)
            numbers.add(num)
        
        hour_hand = Arrow(
            start=ORIGIN, 
            end=1.5 * UP,  # UP方向对应12点位置
            color=YELLOW,
            stroke_width=8
        )
        
        # 组合所有时钟元素
        clock_group = VGroup(clock, numbers).move_to(ORIGIN)
        
        # 显示初始元素
        self.play(FadeIn(clock),
                  LaggedStart(
                      *(GrowFromCenter(u,run_time=0.5) for u in numbers),
                      lag_ratio=0.25
                  ))
        self.wait(1)
        

        self.play(LaggedStart(
            *(Write(i,run_time=0.5) for i in table.get_rows()),lag_ratio=0.25
        ), run_time=2)



        self.wait(2)
        self.play(numbers[6].animate.scale(1.2).set_color(YELLOW))

        # 获取要框住的行（索引7到12，对应数据行6到11）
        rows_to_highlight = table.get_rows()[7:13]

        # 创建包含所有目标行的组合
        highlight_group = VGroup(*rows_to_highlight)

        # 创建包围矩形（带圆角）
        surround_rect = SurroundingRectangle(
            highlight_group,
            color=YELLOW,
            buff=0.15,
            stroke_width=3
        )

        # 添加矩形到场景
        self.play(FadeIn(surround_rect))
        self.wait(2)
        self.play(Uncreate(surround_rect),numbers[6].animate.scale(1/1.2).set_color(WHITE))

        s3=SurroundingRectangle(VGroup(table.get_rows()[4]),color=ORANGE)
        hour_hand.rotate_about_origin(-PI/2)
        self.play(GrowFromEdge(s3,UP),GrowArrow(hour_hand.set_color(ORANGE)))
        self.wait(5)
        s4=SurroundingRectangle(VGroup(table.get_rows()[10]),color=ORANGE)
        self.play(ReplacementTransform(s3,s4),Rotating(hour_hand,about_point=ORIGIN,radians=PI,run_time=1,rate_func=smoothererstep))
        self.wait(5)


        wujianer=MathTex(r'5',r'-2',r'=?').shift(RIGHT*5+UP*0.5)
        ten=MathTex(r'+10').next_to(wujianer[1],DOWN,buff=1)
        self.play(FadeOut(s4,hour_hand))
        self.play(Write(wujianer))
        minus2=SurroundingRectangle(VGroup(table.get_rows()[11]),color=BLUE)
        self.play(Circumscribe(wujianer[1]),Create(minus2))
        self.play(TransformFromCopy(minus2,ten))
        self.wait()
        five=MathTex(r'5').next_to(wujianer[0],DOWN,buff=1)
        fiveteen=MathTex(r'=15').next_to(ten,buff=0.1)
        self.play(TransformFromCopy(wujianer[0],five))
        self.wait(5)
        self.play(Write(fiveteen))
        hour_hand.rotate_about_origin(-PI/2)
        self.play(GrowArrow(hour_hand))
        self.play(Rotating(hour_hand,about_point=ORIGIN,radians=-PI/2-2*PI,run_time=3,rate_func=smoothererstep))
        self.play(Indicate(numbers[3],color=ORANGE))
        self.wait(3)
        self.play(GrowFromEdge(Text('😊').to_corner(DR),RIGHT))
        self.wait(5)


class TwosComplementStableZero(Scene):
    def construct(self) -> None:
        # 标题
        title = Text("Two's Complement Ranges", font_size=42)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=UP))
        self.wait(0.2)

        # 全局参数（可调）
        bar_width = 4.5
        bar_height = 0.38
        tick_len = 0.25
        label_gap = 0.45     # 左侧位数标签离条形左端的距离
        range_x = 3.2        # range 文本的固定 x 坐标（独立于条形）
        y_positions = [1.5, 0.0, -1.5]   # 三行的垂直坐标（由上到下）
        bits_list = [4, 8, 16]

        # 逐行绘制（确保条形中心 x=0）
        for n, y in zip(bits_list, y_positions):
            low = -2 ** (n - 1)
            high = 2 ** (n - 1) - 1

            # 条形，明确放在 x=0, y=<row y>
            bar = Rectangle(width=bar_width, height=bar_height,
                            stroke_width=2, fill_opacity=0.15)
            bar.move_to(np.array([0.0, y, 0.0]))

            # 计算左右端点（全局坐标）
            left_pt = bar.get_left()
            right_pt = bar.get_right()

            # 刻度线（注意 y 坐标一致）
            low_tick = Line(left_pt + DOWN * tick_len, left_pt + UP * tick_len)
            zero_tick = Line(np.array([0.0, y - tick_len, 0.0]), np.array([0.0, y + tick_len, 0.0]))
            high_tick = Line(right_pt + DOWN * tick_len, right_pt + UP * tick_len)

            # 刻度数字（放在刻度正下方）
            low_label = MathTex(str(low), font_size=20).move_to(np.array([left_pt[0], y - 0.35, 0.0]))
            zero_label = MathTex("0", font_size=20).move_to(np.array([0.0, y - 0.35, 0.0]))
            high_label = MathTex(str(high), font_size=20).move_to(np.array([right_pt[0], y - 0.35, 0.0]))

            # 左侧位数标签（靠近条形左端，但独立定位，不影响条形）
            bits_label = Tex(f"{n} bits", font_size=26)
            bits_label.move_to(np.array([left_pt[0] - label_gap-0.5, y, 0.0]))

            # range 文本（固定在 range_x，不与条形绑定）
            range_tex = MathTex(f"{low}\\;\\text{{to}}\\;{high}", font_size=26)
            range_tex.next_to(bar,buff=0.5)

            # 把行元素组合，但注意：不要用 arrange/对该组合的宽度做进一步布局，
            # 我们已经手动把每个元素放到全局坐标。
            row_group = VGroup(bits_label, bar, low_tick, zero_tick, high_tick,
                               low_label, zero_label, high_label, range_tex).shift(LEFT*3)

            # 依次淡入每一行（也可以一次性添加）
            if y == 1.5:
                self.play(FadeIn(bits_label, bar, low_tick, zero_tick, high_tick,
                               low_label, zero_label, high_label, shift=UP), run_time=1)
                self.wait(2)
                self.play(Write(range_tex))
            else:
                self.play(FadeIn(row_group),run_time=0.5)
            self.wait(2)

        # 通用公式（右上）
        formula = MathTex(r"\text{Range: }-2^{n-1}\ \text{to}\ 2^{n-1}-1", font_size=32)
        formula.to_edge(RIGHT).shift(UP * 0.5)
        self.play(Write(formula))
        self.wait(1.0)

        others = Group(*[m for m in self.mobjects if m is not formula])
        self.play(
            formula.animate.move_to(ORIGIN).scale(2).set_color(ORANGE),
            FadeOut(others)
        )



        # ========= Extreme Value +1 ? =========
        add_one = Tex('Extreme Value', r'\ +1', r'\ ?').scale(2)

        # 上移 Extreme Value +1 ?
        arrow = Arrow(start=DOWN, end=DOWN * 3,color=YELLOW).next_to(add_one, DOWN, buff=0.2).shift(UP*1.5)
        over = Text("Overflow Error").set_color(RED).next_to(arrow, DOWN, buff=0.2)
        self.play(FadeOut(formula), Write(add_one[0]), Write(add_one[1]))
        self.play(Write(add_one[-1]), run_time=2)
        self.wait(2)
        self.play(add_one.animate.shift(UP * 1.5),GrowArrow(arrow), FadeIn(over))
        self.wait(7)

        # 全部淡出
        self.play(FadeOut(add_one), FadeOut(arrow), FadeOut(over))
        self.wait(1)

        vals = [
            (2147483646, "01111111111111111111111111111110"),
            (2147483647, "01111111111111111111111111111111"),
            (2147483648, "10000000000000000000000000000000"),
        ]

        start_y = 1.0   # 起始纵坐标
        line_spacing = 1.2  # 行间距

        min_gap = 0.8  # 二进制与十进制间隔

        rows = []

        for i, (dec_val, bin_val) in enumerate(vals):
            dec_tex = MathTex(dec_val,font_size=30)
            bin_tex = Text(bin_val, font="Consolas", font_size=26)

            # 十进制数字右对齐到x=0（digits部分）
            if isinstance(dec_tex, VGroup) and len(dec_tex) > 1:
                digits = dec_tex[1]
                digits.align_to(ORIGIN, RIGHT)
                # 负号保持相对位置，不动
            else:
                dec_tex.align_to(ORIGIN, RIGHT)

            # 二进制右对齐到x=0
            bin_tex.align_to(ORIGIN, RIGHT)

            # 组合：二进制左，十进制右，间距 min_gap
            row = VGroup(bin_tex, dec_tex).arrange(RIGHT, buff=min_gap)

            # 设置行垂直位置
            target_y = start_y - i * line_spacing
            row.move_to(np.array([0, target_y, 0]))

            if i == 0:
                # 第一行直接出现
                self.play(FadeIn(row))
                rows.append(row)
                self.wait(1)
                continue

            prev_row = rows[-1]

            plus_one = Tex("+1", font_size=28, color=YELLOW).next_to(prev_row[0], RIGHT, buff=0.1)
            self.play(FadeIn(plus_one))
            self.wait(0.6)

            row.set_opacity(0)
            self.add(row)

            if i==2:
                minus=MathTex(r'-',font_size=30).next_to(dec_tex,LEFT,buff=0.1)

                # TransformFromCopy 从上一行复制到当前行，原行不动
                self.play(
                    TransformFromCopy(prev_row[0], bin_tex, run_time=0.9),
                    TransformFromCopy(prev_row[1], dec_tex, run_time=0.9),
                    GrowFromEdge(minus,RIGHT),
                    row.animate.set_opacity(1.0),
                )
            else:
                # TransformFromCopy 从上一行复制到当前行，原行不动
                self.play(
                    TransformFromCopy(prev_row[0], bin_tex, run_time=0.9),
                    TransformFromCopy(prev_row[1], dec_tex, run_time=0.9),
                    #GrowFromEdge(minus,RIGHT),
                    row.animate.set_opacity(1.0),
                )
            self.play(FadeOut(plus_one))
            rows.append(row)
            self.wait(5)

        self.play(FocusOn(minus,))
        self.wait(3)








class MinecraftIntegerRange(Scene):
    def construct(self):
        # 1. 显示整数范围的数学区间表示
        bit32=MathTex(r'32\ \mathrm{bits}').shift(UP*0.5)
        range_text = MathTex(r"[-2147483648, \quad 2147483647]").scale(0.75).next_to(bit32,DOWN,1)
        self.play(Write(bit32))
        self.play(TransformFromCopy(bit32,range_text))
        self.wait(1)

        # 2. 显示"player positions" 和 "block states" 文字占位（你后面可以替换成图片）
        player_pos = Text("Player Positions", font_size=24).to_edge(LEFT,1).shift(DOWN*2)
        block_state = Text("Block States", font_size=24).to_edge(RIGHT,1).shift(DOWN*2)
        self.play(FadeIn(player_pos))
        self.play(FadeIn(block_state))
        self.wait(1)

        # 3. 数字溢出动画：先显示一个超大数，然后变成溢出箭头
        big_num = Tex("3000000000000000000000...", font_size=28).next_to(range_text, DOWN)
        overflow_arrow = Arrow(start=range_text.get_bottom(), end=big_num.get_bottom() + DOWN*1,color=YELLOW)
        overflow_label = Text("Overflow!", font_size=36,color=RED).next_to(overflow_arrow, DOWN)
        self.play(Write(big_num))
        self.wait(1)
        self.play(Transform(big_num, overflow_arrow), FadeIn(overflow_label))
        self.wait(1)
        self.play(FadeOut(big_num), FadeOut(overflow_label,player_pos,block_state,bit32,range_text))

        # 4. 显示Java代码，代码用Code类，充满屏幕中心
        code = Code(
            "C:/Users/wangj/Desktop/manimce/project/5.mc/prob.java",
            language="java",
            background="window"
        )
        code.scale_to_fit_height(config.frame_height * 0.9).to_edge(LEFT, buff=0.5)
        self.add(code)
        self.wait(2)

        # --- 下面用 SurroundingRectangle 高亮指定代码行 ---

        # --- 下面是高亮你指定代码块的操作 ---
        highlight_rect = Rectangle(
            width=11,
            height=8/29,
            stroke_color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        ).center().to_edge(LEFT, buff=0.5).shift(UP*1.4)

        self.play(Create(highlight_rect))
        range_text = Tex(r"$\mathrm{errorWithNaN} \in [-100, 80]$").scale(0.75).next_to(highlight_rect, DOWN).shift(RIGHT*3)
        self.play(Write(range_text))
        self.wait(2)




        # 变换高亮到另一段代码，例如第 13-27 行
        new_rect = Rectangle(
            width=11,
            height=8/29*15,
            stroke_color=YELLOW,
            stroke_width=4,
            fill_opacity=0
        ).center().to_edge(LEFT, buff=0.5).shift(DOWN*1)

        self.play(highlight_rect.animate.become(new_rect), FadeOut(range_text))

        self.wait(5)






        # 7. 解释distance计算，显示二维坐标系，标出(0,0)和点(x,z)，显示sqrt距离公式
        plane = NumberPlane(x_range=[-15,15,1], y_range=[-15,15,1],
                            x_length=8,y_length=8,
                            background_line_style={"stroke_opacity":0.2}).to_edge(RIGHT,0)
        origin = Dot(plane.c2p(0,0), color=YELLOW)
        point = Dot(plane.c2p(10,6), color=RED)
        line = Line(origin.get_center(), point.get_center(), color=BLUE)
        label = MathTex("d").next_to(line.get_center(), UP)
        #self.play(Create(line), )
        dist_formula = MathTex(r"d=\sqrt{x^2 + z^2}").move_to(LEFT*4+DOWN*2)

        #self.play(FadeOut(code))
        self.play(code.animate.scale(0.5).to_edge(LEFT, 0.5).to_edge(UP*0.5),FadeOut(highlight_rect))
        self.play(Create(plane), FadeIn(origin))
        self.play(FadeIn(point), Create(line),Write(label), Write(dist_formula))
        self.wait(5)
        

 # 大正方形参数
        big_size = 2.0  # 大正方形边长（你可以调）
        # 创建并把大正方形放到屏幕左下角（第三象限），稍微往里移动一些
        big = Square(side_length=big_size).set_stroke(width=3, color=WHITE)
        big.to_corner(DL).shift(RIGHT * 2.5 + UP )

        # 1) 创建大正方形
        self.play(Create(big),FadeOut(dist_formula))
        self.wait(0.5)

        # 2) 用大括号标注大正方形的一条边（这里用左边）
        brace_big = Brace(big, LEFT, buff=0.06)
        label_big = Tex(r"16"," blocks", font_size=24).next_to(brace_big, LEFT, buff=0.08)
        self.play(GrowFromCenter(brace_big), Write(label_big))
        self.wait(0.8)

        # 3) 将大正方形分为 4 个小正方形 —— 通过画中心的竖线和横线
        vline = Line(big.get_top(), big.get_bottom()).set_stroke(width=2)
        hline = Line(big.get_left(), big.get_right()).set_stroke(width=2)
        # 动画绘制分割线
        self.play(Create(vline), Create(hline))
        self.wait(0.6)

        # 4) 移除大括号和标签（准备给小方块做标注）
        self.play(FadeOut(brace_big), FadeOut(label_big))
        self.wait(0.3)

        # 5) 选取其中一个小正方形（例如左上象限）并用大括号标注这一小方形的一侧
        # 计算小正方形中心位置（对于 big_size=2，子正方边长 = big_size/2）
        sub_side = big_size / 2.0
        half_offset = big_size / 4.0  # 从 big 中心到小方中心的偏移量
        big_center = big.get_center()
        # 这里选左上小方块：x 负，y 正
        small_center = big_center + np.array([-half_offset, half_offset, 0])
        small = Square(side_length=sub_side).set_stroke(width=3, color=WHITE).move_to(small_center)

        # 为了视觉效果我们不需要再绘制小方块（分割线已画出），用一个透明边框来强调它
        small_border = SurroundingRectangle(small, color=YELLOW, buff=0.02)
        self.play(Create(small_border))
        self.wait(0.5)

        # 在该小方块左边加 Brace 与标签
        brace_small = Brace(small, LEFT, buff=0.04)
        label_small = Tex(r"8"," blocks", font_size=22).next_to(brace_small, LEFT, buff=0.06)
        self.play(GrowFromCenter(brace_small), Write(label_small))
        self.wait(15)








class disappear(Scene):
    def construct(self):
        codeLine=Code(
            None,
            """float errorWithNaN = 100 - """+"""Mth.sqrt(x * x + z * z)"""+""" * 8;""",'java'
        ).scale(0.75).shift(UP)
        eq=MathTex(r'\Downarrow ')
        Te=MathTex(r'\mathrm{errorWithNaN}=100-8\ ',r'\sqrt[]{x^2+z^2}').scale(0.5).next_to(eq,DOWN)
        over=Text('OverflowError',color=RED).scale(0.5).next_to(Te,LEFT,1)
        arr=Arrow(start=over.get_right(),end=Te.get_left(),color=YELLOW)

        self.play(Write(codeLine))
        self.wait(5)
        self.play(GrowFromCenter(eq),GrowFromEdge(Te,UP))
        self.wait(5)

        self.play(GrowFromEdge(over,RIGHT),GrowArrow(arr))


        self.wait(3)

        large=MathTex(r'x^2+z^2',r'>2147483647').scale(0.5).next_to(Te,DOWN)
        self.play(Circumscribe(Te[-1]))
        self.play(Write(large))
        self.wait()
        self.play(Wiggle(over))
        self.wait(3)

        nan = MathTex(r'\mathrm{errorWithNaN}=', r'\mathrm{NaN}').scale(0.5).next_to(eq,DOWN)
        nan[1].set_color(RED)  # 第二个元素设为红色        
        self.play(ReplacementTransform(Te,nan))


        self.wait(10)
        self.play(FadeOut(nan,over,eq,arr,large))
        example=Title('Example')
        xz=[
            MathTex(r'x = 4634',r'0',r', z = 0').scale(0.75).shift(UP),
            MathTex(r'x',r'^2+',r'z',r'^2=',r'?').scale(0.75),
            MathTex(r'46340',r'^2+',r'0',r'^2=',r'2,147,395,600').scale(0.75),
            MathTex(r'>').scale(0.75),#3
            MathTex(r'=').scale(0.75),#4
            MathTex(r'<').scale(0.75),#5
            MathTex(r'2,147,483,647').scale(0.75),
        ]
        xz[3].next_to(xz[2],RIGHT)
        xz[4].next_to(xz[2],RIGHT)
        xz[5].next_to(xz[2],RIGHT)
        xz[6].next_to(xz[3],RIGHT)
        self.play(Write(example),codeLine.animate.next_to(example,DOWN),GrowFromEdge(xz[1],DOWN))
        self.wait()
        self.play(Write(xz[0]))
        self.play(ReplacementTransform(xz[1],xz[2]))
        self.wait(2)
        self.play(GrowFromEdge(xz[5],LEFT),GrowFromEdge(xz[6],LEFT))
        self.wait(10)
        
        xz.append(MathTex(r'x = 4634',r'1',r', z = 0').scale(0.75).shift(UP))
        self.play(ReplacementTransform(xz[0],xz[-1]),FadeOut(xz[5],xz[6]))
        xz.append(MathTex(r'46341',r'^2+',r'0',r'^2=',r'2,147,488,281').scale(0.75))
        self.play(ReplacementTransform(xz[2],xz[-1]))
        self.play(GrowFromEdge(xz[3],LEFT),GrowFromEdge(xz[6],LEFT))
        self.wait(2)


        ov=Text('Overflow!',color=RED).scale(0.75).shift(DOWN)
        self.play(Write(ov))
        self.wait()
        neg=MathTex(r'2,147,488,281',r' - 4,294,967,296 = ',r'-2,147,479,015').scale(0.75).next_to(ov,DOWN)
        self.play(TransformFromCopy(xz[-1],neg[0]),GrowFromEdge(neg[1],LEFT),GrowFromEdge(neg[2],LEFT))
        NaN=MathTex(r'\sqrt{-2,147,479,015}=',r'\mathrm{Not\ a\ Number}',).scale(0.75).next_to(ov,DOWN)
        NaN[1].set_color(YELLOW)
        self.wait(2)
        self.play(ReplacementTransform(neg,NaN))


        self.wait(10)
        









# Manim CE
# Render example:
# manim -pqh mod_wrap.py ModWrapDemo

# manim animation: illustrate integer wrap-around making distance appear small again
# 对应 manim community v0.14+ API（若你的版本不同，少量改动即可）


class WrapAroundDistance(Scene):
    def construct(self):
        # --- Visual setup ---
        #title = Text("32-bit wrap-around demo", font_size=36).to_edge(UP)
        #self.play(FadeIn(title))

        # coordinate reference (visual only)
        axes = NumberPlane(
            x_range=(-80, 80, 1),
            y_range=(-30, 30, 1),
            background_line_style={"stroke_opacity": 0.2},
        ).scale(1)
        self.play(Write(axes))

        # scaling from "mathematical x" to screen coordinates
        SCALE = 20000  # visual scale factor: real x=65536 -> screen x ~ 65.5

        # A moving point representing (x, z) with z fixed at 0 for the main example
        x_tracker = ValueTracker(0)
        dot = always_redraw(lambda: Dot(axes.c2p(x_tracker.get_value() / SCALE, 0), radius=0.12,color=YELLOW))
        cir = always_redraw(
            lambda: Circle(
                radius=np.linalg.norm(
                    axes.c2p(x_tracker.get_value() / SCALE, 0) - axes.c2p(0, 0)
                ),
                color=GREEN
            ).move_to(axes.c2p(0, 0))  # 圆心放在原点
        )

        # show formula: 2 = x*x + z*z  (we'll display 2 mod 2^32)
        formula = MathTex(r"2 = x \cdot x + z \cdot z", font_size=30).shift(DOWN+RIGHT*4)
        #mod_tag = MathTex(r"\bmod\ 2^{32}", font_size=26).next_to(formula, RIGHT, buff=0.4)
        self.play(FadeIn(formula,dot,cir), #FadeIn(mod_tag)
                  )

        # dynamic text showing x, z, raw 2 and 2 mod 2^32
        x_text = always_redraw(lambda:
            MathTex(r"x=", str(int(round(x_tracker.get_value()))), font_size=28)#=================================================================================================================================================
            .next_to(formula, DOWN, aligned_edge=LEFT)
        )
        z_val = 0  # fixed for this demo
        z_text = MathTex(r"z=", str(z_val), font_size=28).next_to(x_text, RIGHT, buff=0.8)#=================================================================================================================================================

        def compute_raw() -> int:
            xv = int(round(x_tracker.get_value()))
            return xv * xv + z_val * z_val

        raw_text = always_redraw(lambda: MathTex(r"2=", str(compute_raw()), font_size=24).next_to(formula, DOWN,1.5))#=================================================================================================================================================

        def compute_mod() -> int:
            xv = int(round(x_tracker.get_value()))
            mod = (xv * xv + z_val * z_val) % (2**32)
            return mod

        #mod_text = always_redraw(lambda: MathTex(r"2_{\bmod 2^{32}}=", str(compute_mod()), font_size=24).next_to(raw_text, DOWN))

        # show sqrt result (what Mth.sqrt would return)
        #sqrt_text = always_redraw(lambda: MathTex(r"\sqrt{2_{\bmod 2^{32}}}=", str(int(math.isqrt(compute_mod()))), font_size=28).next_to(mod_text, DOWN))

        self.play(FadeIn(x_text), FadeIn(z_text), FadeIn(raw_text), 
                  #FadeIn(mod_text), FadeIn(sqrt_text)
                  )
        self.wait(0.5)

        # --- Animation sequence with comments mapping to your subtitles ---

        # Subtitle 1:
        # "However, things do not end here."
        # -> Animation: small pause + highlight the dot to signal "there's more"
        #self.play(dot.animate.scale(1.6), run_time=0.4)
        #self.play(dot.animate.scale(1/1.6), run_time=0.4)
        # (this short emphasis corresponds to the sentence above)

        # Subtitle 2:
        # "When we still increase `x` and `z` to larger values, then `x * x + z * z` will eventually become larger and larger, since the distance is simply increasing."
        # -> Animation: move dot outward while raw 2 increases (visual from numeric changes)
        #self.play(x_tracker.animate.set_value(5000), run_time=3)  # goes to x = 5000 (visual)
        # numeric displays update automatically
        self.play(raw_text.animate.set_color(YELLOW))
        # Subtitle 3:
        # "But if we keep increasing `x` and `z`, the value will wrap around again and again, it can led a fake positive value, and thus `Mth.sqrt()` will return a valid positive number again."
        # -> Animation: continue increasing x so that 2 mod 2^32 wraps (we animate to 65536)
        #    numeric display will show raw big number, then mod reduces it (wrap)
        self.play(x_tracker.animate.set_value(100000), run_time=7)  #####################################################################################################
        self.play(raw_text.animate.set_color(WHITE))
        #self.wait(5)

        # Subtitle 4:
        # "This is why blocks reappear again at some places far away."
        # -> Animation: demonstrate a "block" that disappears when true distance is large,
        #    but reappears when the wrapped 2 becomes small (i.e., sqrt becomes small)
        #block = Square(side_length=1).move_to(axes.c2p(20, 0))  # a block somewhere on map
        #block_label = MathTex(r"\text{Block}", font_size=20).next_to(block, DOWN, buff=0.1)
        #self.play(FadeIn(block), FadeIn(block_label))

        # Behavior rule (visualized): if displayed sqrt > threshold -> hide block ; if <= threshold -> show
        # We'll animate: as x increases past threshold, raw distance large -> hide block;
        # then after wrap (when mod becomes small), show it again.
        # First, move x to a value causing sqrt > 10 (hide)
        #self.play(x_tracker.animate.set_value(12000), run_time=3)
        # hide block because displayed sqrt large
        #self.play(FadeOut(block), FadeOut(block_label))
        #self.wait(0.6)

        # then continue to 65536 where mod wraps to 0 -> sqrt becomes 0 -> block reappears
        #self.play(x_tracker.animate.set_value(65536), run_time=3)
        # show block reappearing (demonstrating the "fake positive" from wrap)
        #self.play(FadeIn(block), FadeIn(block_label))
        self.wait(10)

        # --- Specific numeric example you gave ---
        # Subtitle 5:
        # "Lets see another example. Suppose we have `x = 65536, z = 0`, then `x * x + z * z` will be `4,294,967,296`."
        # -> Animation: set x exactly, highlight the raw number and show 4,294,967,296
        self.play(x_tracker.animate.set_value(65536), run_time=1)  #####################################################################################################
        # briefly highlight raw_text and mod_text
        self.play(Circumscribe(raw_text))
        # Subtitle 6:
        # "Since 4,294,967,296 - 4,294,967,296 = 0"
        # -> Animation: show a quick math box demonstrating subtraction equals zero
        eq = MathTex(r"4,294,967,296 - 4,294,967,296 = 0", font_size=28).next_to(formula,UP,3)
        self.play(Write(eq))
        self.wait(1.0)
        #self.play(FadeOut(eq))

        # Subtitle 7:
        # "You say, what? WHY 4,294,967,296 not 2,147,483,647? This is because an entire 'turn' of 32 bits is `2^32 = 4,294,967,296`, which is the maximum value of a 32-bit signed integer."
        # -> Animation: show 2^32 expression and a rotating modulus arrow to indicate a full turn
        pow2 = MathTex(r"2^{32} = 4{,}294{,}967{,}296", font_size=28).next_to(eq, DOWN,1)
        turn_arrow = Arrow(start=pow2.get_top(), end=eq.get_bottom())
        self.play(Write(pow2))
        self.play(GrowArrow(turn_arrow))
        self.wait(1.0)
        self.play(FadeOut(pow2), FadeOut(turn_arrow))

        # Subtitle 8:
        # "So exactly at `x = 65536` it will wrap around to `0`. When we take the square root of this value using `Mth.sqrt()`, it returns `0`, which is valid."
        # -> Animation: emphasize sqrt_text becoming 0, briefly pulse the dot and the block to show reappearance is "valid"
        self.play(Indicate(dot))
        # final short pause then fade out
        self.wait(10)
        # end



class XINGJI(Scene):
    def construct(self) -> None:
        fo=MathTex(r"\left(\frac{r}{8}\right)^2 \equiv  n\  (\mathrm{mod\ } 2^{32})")
        f=MathTex(r'0 \le n \le 2^{31}').next_to(fo,DOWN)
        self.play(Write(fo),Write(f))
        self.wait(5)



class SinRegion(Scene):
    def construct(self) -> None:
        max_radius = config.frame_height
        dr = 0.05

        # 中心小圆
        center_circle = Circle(radius=0.1, color='#F7E9A3', fill_opacity=1, stroke_width=0)

        rings = [center_circle]

        r = 0
        while r < max_radius:
            if np.sin(r**2) > 0:
                ring = Annulus(inner_radius=r, outer_radius=r+dr, color='#F7E9A3', fill_opacity=1, stroke_width=0)
                rings.append(ring)
            r += dr/2

        # 使用 LaggedStart 顺序生成圆环
        self.play(LaggedStart(*[FadeIn(r) for r in rings], lag_ratio=0.005))
        self.play(LaggedStart(*[Indicate(r,color=BLUE,run_time=0.5) for r in rings], lag_ratio=0.005))
        self.wait(10)
        '''self.play(LaggedStart(
            (
            LaggedStart(*[Indicate(r,color=BLUE,run_time=0.5) for r in rings], lag_ratio=0.005),
            LaggedStart(*[Indicate(r,color=RED,run_time=0.5) for r in rings], lag_ratio=0.005),
            LaggedStart(*[Indicate(r,color=BLUE,run_time=0.5) for r in rings], lag_ratio=0.005),
            LaggedStart(*[Indicate(r,color=RED,run_time=0.5) for r in rings], lag_ratio=0.005),
            LaggedStart(*[Indicate(r,color=BLUE,run_time=0.5) for r in rings], lag_ratio=0.005),
            LaggedStart(*[Indicate(r,color=RED,run_time=0.5) for r in rings], lag_ratio=0.005),
            ),lag_ratio=0.5)
                  )'''







class FormulaDerivation(Scene):
    def construct(self) -> None:
        # 标题
        title = Text("Fr", font_size=48)
        title.to_edge(UP)
        #self.play(Write(title))

        ax=NumberPlane()
        #ax = Axes(x_range=[0, 10, 1],y_range=[-2, 2, 1],axis_config={"include_numbers": False})

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: np.sin(x), x_range=[-10, 10], use_smoothing=False,color=YELLOW)
        self.play(FadeIn(ax, graph))

        pos=Rectangle(BLUE,((config.frame_height))/2,round(config.frame_width) ,fill_opacity=0.5).to_edge(UP,0)
        neg=Rectangle(RED,((config.frame_height))/2,round(config.frame_width) ,fill_opacity=0.5).to_edge(DOWN,0)
        
        self.wait(2)
        self.play(GrowFromEdge(pos,DOWN))
        self.wait(2)
        self.play(FadeOut(pos),GrowFromEdge(neg,DOWN))
        self.wait(2)
        self.play(FadeOut(neg))
        #self.play(FadeOut(ax,graph))




        # 第一步：周期与分母
        step1 = MathTex(
            r"T \;=\; 2^{32}\cdot 8^{2}",
            r"=\;2^{32}\cdot 64",
            font_size=40
        )
        step1.next_to(title, DOWN, buff=0.8)
        BLAC=Rectangle(BLACK,config.frame_height,config.frame_width,fill_opacity=0.8)

        self.play(FadeIn(BLAC))
        self.play(Write(step1[0]))
        self.wait(0.5)
        self.play(TransformFromCopy(step1[0], step1[1]), run_time=1)  # 简短变换展示等式
        self.wait(0.6)

        # 第二步：omega 的代数形式
        omega_exact = MathTex(
            r"\omega \;=\;\frac{2\pi}{T}",
            r"=\;\frac{2\pi}{2^{38}}",
            r"=\;\frac{\pi}{2^{37}}",
            font_size=40
        )
        omega_exact.next_to(step1, DOWN, buff=0.7)
        # 逐项出现并强调最终简化形式
        self.play(Write(omega_exact[0]))
        self.wait(2)
        self.play(Write(omega_exact[1]))
        self.wait(2)
        self.play(Write(omega_exact[2]))
        self.wait(2)

        # 第三步：数值近似（使用你给出的数值）
        omega_numeric = MathTex(
            r"\omega",r"\approx 2.2858094988549370016427\times 10^{-11}",
            font_size=36
        )
        omega_numeric.next_to(omega_exact, DOWN, buff=0.6).align_to(omega_exact[0],LEFT)
        self.play(FadeIn(omega_numeric[1], shift=DOWN))
        self.wait(10)

        # 第四步：最终函数形式
        final = MathTex(
            r"f(r) \;=\; \sin\!\bigl(2.2858\times 10^{-11} r^{2}\bigr)",
            font_size=48
        )
        self.play(Write(final),FadeOut(omega_exact,omega_numeric,step1))
        self.wait(10)


        graph1 = ax.plot(lambda x: np.sin(x**2), x_range=[-10, 10],color=GREEN)
        self.play(FadeOut(BLAC,final))
        self.play(graph.animate.become(graph1))
        self.wait()
        
        
        r_max = 20  # r 最大值
        n_max = int((r_max**2) / np.pi) + 1  # 需要多少个零点

        # 计算零点位置
        zeros = [np.sqrt(n * np.pi) for n in range(n_max)]

        blue = VGroup()
        red = VGroup()

        for i in range(len(zeros) - 1):
            w = zeros[i+1] - zeros[i]  # 区间宽度
            rect = Rectangle(
                height=config.frame_height,
                width=w,
                fill_opacity=0.5,
                stroke_width=0
            ).shift(RIGHT * (zeros[i] + zeros[i+1]) / 2)

            if i % 2 == 0:
                rect.set_color(BLUE)
                blue.add(rect)
                blue.add(rect.copy().center().shift(-RIGHT * (zeros[i] + zeros[i+1]) / 2))
            else:
                rect.set_color(RED)
                red.add(rect)
                red.add(rect.copy().center().shift(-RIGHT * (zeros[i] + zeros[i+1]) / 2))

        self.play(FadeIn(blue))
        self.wait(5)
        self.play(FadeOut(blue))
            
        self.play(FadeIn(red))
        self.wait(5)
        self.play(FadeOut(red))
            





'''        # 小结：把 omega 的精确形式与函数放大短暂强调
        self.play(
            Indicate(omega_exact[2], scale_factor=1.15),
            Indicate(final, scale_factor=1.08),
            run_time=1.2
        )
        self.wait(1.2)

        # 结尾淡出（保留屏幕以便截帧）
        self.play(
            *[FadeOut(mob, shift=UP) for mob in [title, step1, omega_exact, omega_numeric]],
            run_time=1.0
        )
        self.wait(0.6)
        # 最终停留 final 与注释
        self.play(final.animate.to_edge(UP))
        self.wait(2.0)
'''

'''        # 右下角：短说明（中文），包括奇偶性校正
        #note_lines = VGroup(
            Text("说明：仅在 r 的正半轴放置“方块”，负半轴不放。", font_size=22),
            Text("注：你写到“sine 是偶函数”，实际上 sin 是奇函数；若需关于原点的偶对称请用 cos。", font_size=20)
        )
        note_lines.arrange(DOWN, aligned_edge=LEFT)
        note_lines.to_corner(DR)
        # 逐行淡入
        for i, line in enumerate(note_lines):
            self.play(FadeIn(line, shift=RIGHT), run_time=0.8)
            self.wait(0.35)
'''



class Sin2DTo3D(ThreeDScene):
    def construct(self) -> None:
        # --- 参数 ---
        r_max = 10
        surface_resolution = (20, 20)
        sweep_time = 1.0

        # --- 坐标系 ---
        axes = ThreeDAxes(
            x_range=[-r_max, r_max, 1],
            y_range=[-r_max, r_max, 1],
            z_range=[-1.5, 1.5, 0.5],
            x_length=2*r_max,
            y_length=2*r_max,
            z_length=3,
        )
        axes.move_to(ORIGIN)
        self.add(axes)

        # --- 2D 横截面曲线 ---
        curve = ParametricFunction(
            lambda t: np.array([t, 0.0, np.sin(t**2)]),
            t_range=[-r_max, r_max],
            color=BLUE,
            stroke_width=3,
        )
        self.set_camera_orientation(phi=90*DEGREES, theta=-90*DEGREES)  # 俯视
        self.play(Create(curve), run_time=1.2)
        self.wait(0.6)

        # --- 3D 曲面 ---
        def surf1(u, v):
            x = v * np.cos(u)
            y = v * np.sin(u)
            z = np.sin(v**2) 

            return np.array([x, y, z if z>=0 else 0])
        def surf2(u, v):
            x = v * np.cos(u)
            y = v * np.sin(u)
            z = np.sin(v**2) 

            return np.array([x, y, z if z<=0 else 0])

        surface1 = Surface(
            surf1,
            u_range=[0, 2*PI],
            v_range=[0, r_max],
            resolution=surface_resolution,
            stroke_color=BLACK,
            stroke_width=0
        )
        surface2 = Surface(
            surf2,
            u_range=[0, 2*PI],
            v_range=[0, r_max],
            resolution=surface_resolution,
            stroke_color=BLACK,
            stroke_width=0
        )
        def ze(u,v) :
            x = v * np.cos(u)
            y = v * np.sin(u)
            z = 0
            return np.array([x, y, z])


        surfac=Surface(
            ze,
            u_range=[0, 2*PI],
            v_range=[0, r_max],
            resolution=surface_resolution,
            fill_opacity=1,stroke_width=0
            
        ).set_fill(RED, opacity=1)
        surface1.set_fill(BLUE, opacity=1)
        surface2.set_fill(RED, opacity=1)

        # --- 动画：曲面出现 + 摄像机抬起旋转 ---
        # 摄像机移动
        # 开始摄像机持续旋转

        # 同时显示曲面
        ##self.play(FadeIn(surface), run_time=sweep_time)

        # 等待一段时间（曲面显示 + 旋转进行中）
        #self.wait(2)

        # 停止旋转
        #self.stop_ambient_camera_rotation()

        self.begin_ambient_camera_rotation(rate=0.3)  # 每秒旋转 rate*2π 弧度
        self.move_camera(phi=30*DEGREES, theta=45*DEGREES, run_time=sweep_time,
                         added_anims=[
            FadeOut(curve),
            FadeIn(surface2,surface1)])
        self.wait(1)






class Distance(Scene):
    def construct(self):


        plane = NumberPlane()
        origin = Dot(plane.c2p(0,0), color=YELLOW)
        point = Dot(plane.c2p(4,3), color=ORANGE)
        line = Line(origin.get_center(), point.get_center(), color=BLUE)
        label = MathTex("r").next_to(line.get_center(), UP)
        #self.play(Create(line), )
        dist_formula = MathTex(r"r^2=x^2 + z^2").move_to(-DOWN*2+LEFT*4)
        self.play(FadeIn(plane))
        self.wait()
        self.play(Create(origin),Create(point))
        self.play(Create(line))
        self.play(Write(label))
        self.wait()
        self.play(Write(dist_formula))
        self.wait()

'''        axes = NumberPlane(
            x_range=(-80, 80, 1),
            y_range=(-30, 30, 1),
            background_line_style={"stroke_opacity": 0.2},
        ).scale(1)
        self.play(Write(axes))
        SCALE = 20000  # visual scale factor: real x=65536 -> screen x ~ 65.5
        x_tracker = ValueTracker(0)
        dot = always_redraw(lambda: Dot(axes.c2p(x_tracker.get_value() / SCALE, 0), radius=0.12,color=YELLOW))
        cir = always_redraw(
            lambda: Circle(
                radius=np.linalg.norm(
                    axes.c2p(x_tracker.get_value() / SCALE, 0) - axes.c2p(0, 0)
                ),
                color=GREEN
            ).move_to(axes.c2p(0, 0))  # 圆心放在原点
        )
        formula = MathTex(r"r^2 = x \cdot x + z \cdot z", font_size=30).shift(DOWN+RIGHT*4)
        self.play(FadeIn(formula,dot,cir))
        self.wait(0.5)

        self.play(x_tracker.animate.set_value(100000), run_time=7)  #####################################################################################################
        self.play(x_tracker.animate.set_value(1000), run_time=7)  #####################################################################################################

'''



from manim import *
import textwrap

class OpeningQuote(Scene):
    def construct(self):
        # 英文名言
        quote_en = "The eternal mystery of the world is its comprehensibility. The fact that it is comprehensible is a miracle."
        wrapped_quote_en = "\n".join(textwrap.wrap(quote_en, width=70))

        main_text_en = Text(
            wrapped_quote_en,
            font_size=28,
            t2c={'mystery':YELLOW,'comprehensibility':BLUE,'miracle':YELLOW},
            line_spacing=1.25
        ).to_edge(LEFT,1).to_edge(UP,1)

        author_en = Text(
            "- Albert Einstein, 1936. Physics and Reality",
            font_size=24
        ).next_to(main_text_en, DOWN,0.5).to_edge(RIGHT,1)

        # 中文翻译
        quote_cn = "世界永恒的奥秘在于它居然是可以被理解的。它之所以能够被理解，本身就是一个奇迹。"
        wrapped_quote_cn = "\n".join(textwrap.wrap(quote_cn, width=22))

        main_text_cn = Text(
            wrapped_quote_cn,
            font_size=32,
            t2c={'奥秘':YELLOW,'理解':BLUE,'奇迹':YELLOW},
            line_spacing=1.25
        ).next_to(author_en, DOWN, buff=1.5).to_edge(LEFT,1)

        author_cn = Text(
            "—— 阿尔伯特·爱因斯坦，1936年 《物理学与现实》",
            font_size=24
        ).next_to(main_text_cn, DOWN,0.5).to_edge(RIGHT,1)

        # 组合上下结构
        cir=Text('*注：有人声称这句话改写了1936年《富兰克林研究所杂志》上一篇文章中的一段话：“世界永恒的奥秘在于它的可理解性……它是可以理解的这个事实是一个奇迹。”',
                 font_size=10).to_corner(DL,0)
        # 动画
        self.play(LaggedStart(FadeIn(main_text_en),FadeIn(author_en),FadeIn(main_text_cn),FadeIn(author_cn),FadeIn(cir),lag_ratio=0.25))
        self.wait(4)
