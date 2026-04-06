from manim import *
import numpy as np

# 全局配置：白色背景 + 静态渲染友好
config.background_color = WHITE
Text.set_default(color=BLACK)
MathTex.set_default(color=BLACK)

class MuonPositronDiagram(Scene):
    def construct(self):
        # ==========================================
        # 1. 核心工具：伪 3D 到 2D 投影系统
        # ==========================================
        ex = np.array([-0.7, -0.3, 0])  # X轴视觉方向 
        ey = np.array([ 0.8, -0.2, 0])  # Y轴视觉方向 
        ez = np.array([ 0.0,  1.0, 0])  # Z轴视觉方向 
        
        def to_2d(x, y, z):
            """将 3D 坐标投影到 2D 画布"""
            return x * ex + y * ey + z * ez
        
        def get_3d_arc(orig, v1_3d, v2_3d, radius, color=BLACK, num_points=30):
            """在 3D 空间中计算真实圆弧并投影"""
            v1 = np.array(v1_3d, dtype=float)
            v2 = np.array(v2_3d, dtype=float)
            u1 = v1 / np.linalg.norm(v1)
            u2 = v2 / np.linalg.norm(v2)
            
            dot_prod = np.dot(u2, u1)
            u2_orth = u2 - dot_prod * u1
            norm_orth = np.linalg.norm(u2_orth)
            if norm_orth > 1e-6:
                u2_orth = u2_orth / norm_orth
            else:
                u2_orth = np.zeros_like(u2_orth)
                
            theta = np.arccos(np.clip(dot_prod, -1.0, 1.0))
            t_vals = np.linspace(0, theta, num_points)
            
            points = [orig + to_2d(*(radius * (np.cos(t) * u1 + np.sin(t) * u2_orth))) for t in t_vals]
            arc = VMobject(color=color)
            arc.set_points_smoothly(points)
            return arc

        def draw_plane(center):
            """绘制统一视角的参考平面（学术风格）"""
            p1 = center + to_2d(-2.5, -2.5, 0)
            p2 = center + to_2d( 2.5, -2.5, 0)
            p3 = center + to_2d( 2.5,  2.5, 0)
            p4 = center + to_2d(-2.5,  2.5, 0)
            return Polygon(p1, p2, p3, p4, fill_color=BLUE_E, fill_opacity=0.06, stroke_color=WHITE, stroke_width=2)

        # ==========================================
        # 2. 左图：Muon
        # ==========================================
        left_center = np.array([-3.5, -1.0, 0])
        #l_plane = draw_plane(left_center)
        l_z_axis = Arrow(left_center, left_center + to_2d(0, 0, 3.8), buff=0, stroke_width=3, color=BLACK)
        l_z_label = MathTex(r"\mathbf{p}_\mu").next_to(l_z_axis.get_end(), UP, buff=0.1)
        
        muon = Circle(radius=0.25, fill_color=RED_E, fill_opacity=1, stroke_color=DARK_GRAY, stroke_width=1.5).move_to(left_center)
        muon_label = MathTex(r"\mu^+", font_size=38).next_to(muon, RIGHT, buff=0.2)
        
        # 定义 Muon 自旋向量 S (更新方向以实现最大清晰度：向左上 (-x, -y, +z象限))
        # 尝试：[-2.0, -1.0, 1.5]
        S_3d = np.array([2.0, -1.0, 1.5])
        S_tip = left_center + to_2d(*S_3d)
        S_arrow = Arrow(left_center, S_tip, buff=0, stroke_width=4, color=RED_E)
        # 显式放置标签以获得最佳清晰度，向左上
        S_label = MathTex(r"\mathbf{S}", color=RED_E).next_to(S_tip, LEFT, buff=0.1).shift(UP*0.1)
        
        # 定义 S 在平面上的投影向量 S_perp
        S_perp_3d = np.array([2.0, -1.0, 0])
        S_perp_tip = left_center + to_2d(*S_perp_3d)
        S_perp_arrow = Arrow(left_center, S_perp_tip, buff=0, stroke_width=3, color=BLACK)
        # 显式放置标签，向左上
        S_perp_label = MathTex(r"\mathbf{S}_\perp", color=BLACK).next_to(S_perp_arrow.get_center(), DOWN, buff=0.2)
        
        l_proj_line = DashedLine(S_tip, S_perp_tip, color=GRAY_D, stroke_width=3, dash_length=0.1)
        
        # 计算新 $\psi$ 角
        psi_arc = get_3d_arc(left_center, [0,0,1], S_3d, radius=1.0, color=RED_E)
        psi_label = MathTex(r"\psi", color=RED_E).move_to(psi_arc.point_from_proportion(0.5) + UP*0.2 + LEFT*0.2)

        # 进动轨迹圆环（深色虚线）
        #ring_r = np.linalg.norm(S_perp_3d)
        #ring_z = S_3d[2]
        #ring_points = [left_center + to_2d(ring_r * np.cos(t), ring_r * np.sin(t), ring_z) for t in np.linspace(0, 2*np.pi, 100)]
        #precession_ring_smooth = VMobject().set_points_smoothly(ring_points)
        #precession_ring = DashedVMobject(precession_ring_smooth, num_dashes=36, color=RED_E, stroke_width=2)
        
        left_group = VGroup(#l_plane,
                            l_proj_line, 
                            #precession_ring, 
                            l_z_axis, l_z_label, muon, muon_label, 
                            S_arrow, S_label, S_perp_arrow, S_perp_label, psi_arc, psi_label)
        # 学术风格：缩小 VGroup 以获得更多呼吸空间
        left_group.scale(0.8)

        # ==========================================
        # 3. 右图：Positron
        # ==========================================
        right_center = np.array([3.5, -1.0, 0])
        #r_plane = draw_plane(right_center)
        r_z_axis = Arrow(right_center, right_center + to_2d(0, 0, 3.8), buff=0, stroke_width=3, color=BLACK)
        r_z_label = MathTex(r"\mathbf{p}_\mu").next_to(r_z_axis.get_end(), UP, buff=0.1)
        
        positron = Circle(radius=0.15, fill_color=BLUE_D, fill_opacity=0.8, stroke_color=DARK_GRAY, stroke_width=1.5).move_to(right_center)
        positron_label = MathTex(r"e^+", font_size=38).next_to(positron, LEFT, buff=0.2).shift(UP*0.3)
        
        # 定义 正电子动量向量 P (保持原方向：向右上 (-x, +y, +z象限))
        # np.array([-1.5, 2.2, 2.2])
        P_3d = np.array([-1.5, 2.2, 2.2])
        P_tip = right_center + to_2d(*P_3d)
        P_arrow = Arrow(right_center, P_tip, buff=0, stroke_width=4, color=BLUE_D)
        P_label = MathTex(r"\mathbf{P}", color=BLUE_D).next_to(P_tip, UP, buff=0.1)
        
        # 定义 P 在平面上的投影 P_perp
        P_perp_3d = np.array([-1.5, 2.2, 0])
        P_perp_tip = right_center + to_2d(*P_perp_3d)
        P_perp_arrow = Arrow(right_center, P_perp_tip, buff=0, stroke_width=3, color=BLUE_D)
        P_perp_label = MathTex(r"\mathbf{P}_\perp", color=BLUE_D).next_to(P_perp_tip, RIGHT, buff=0.1)
        
        #👉 核心关联：在此处继承左图更新后的新的 S_perp_3d（`np.array([-2.0, -1.0, 0])`）
        S_perp_tip_R = right_center + to_2d(*S_perp_3d)
        S_perp_arrow_R = Arrow(right_center, S_perp_tip_R, buff=0, stroke_width=3, color=BLACK)
        # 显式放置标签，向左上
        S_perp_label_R = MathTex(r"\mathbf{S}_\perp", color=BLACK).next_to(S_perp_arrow_R.get_center(), DOWN, buff=0.2)
        
        r_proj_line = DashedLine(P_tip, P_perp_tip, color=GRAY_D, stroke_width=3, dash_length=0.1)
        
        theta_arc = get_3d_arc(right_center, [0,0,1], P_3d, radius=1.0, color=BLUE_D)
        theta_label = MathTex(r"\theta", color=BLUE_D).move_to(theta_arc.point_from_proportion(0.5) + UP*0.2 + RIGHT*0.2)
        
        phi_arc = get_3d_arc(right_center, S_perp_3d, P_perp_3d, radius=0.8, color=GREEN_E)
        phi_label = MathTex(r"\phi", color=GREEN_E).move_to(phi_arc.point_from_proportion(0.5) + DOWN*0.3)
        
        right_group = VGroup(#r_plane,
                             r_proj_line, r_z_axis, r_z_label, positron, positron_label, 
                             P_arrow, P_label, P_perp_arrow, P_perp_label, 
                             S_perp_arrow_R, S_perp_label_R, 
                             theta_arc, theta_label, phi_arc, phi_label)
        # 学术风格：缩小 VGroup 以获得更多呼吸空间
        right_group.scale(0.8)

        # ==========================================
        # 4. 最终整合
        # ==========================================
        #divider = DashedLine(UP * 3.5, DOWN * 3.5, color=GRAY_C, stroke_width=2, dash_length=0.15)
        
        # 移除了标题，仅保留图形和分割线
        self.add( left_group, right_group)