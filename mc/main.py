import manim

class OpeningAnimation(Scene):
    def construct(self):
        # 背景设置
        self.camera.background_color = "#1a1a2e"
        
        # 标题文字
        title = Text("人工智能的未来", font="SimHei", font_size=72)
        title.set_color("#ffffff")
        title.to_edge(UP, buff=1.5)
        
        # 副标题
        subtitle = Text("探索机器学习的无限可能", font="SimHei", font_size=48)
        subtitle.set_color("#a0a0ff")
        subtitle.next_to(title, DOWN, buff=0.8)
        
        # 演讲者信息
        speaker_info = Text("演讲者：张三", font="SimHei", font_size=36)
        speaker_info.set_color("#cccccc")
        speaker_info.next_to(subtitle, DOWN, buff=1.2)
        
        # 日期信息
        date_info = Text("2024年1月", font="SimHei", font_size=32)
        date_info.set_color("#cccccc")
        date_info.next_to(speaker_info, DOWN, buff=0.3)
        
        # 动画序列
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(0.5)
        self.play(Write(speaker_info), run_time=1)
        self.wait(0.3)
        self.play(Write(date_info), run_time=1)
        self.wait(2)
        
        # 淡出开场信息
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(speaker_info),
            FadeOut(date_info),
            run_time=1.5
        )
        self.wait(0.5)