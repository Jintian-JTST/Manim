import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 定义常数
c = 2.28580929e-11

# 平滑过渡函数
def transition(distance, start, width, color1, color2):
    """创建颜色平滑过渡"""
    t = np.clip((distance - start) / width, 0, 1)
    t = t[..., np.newaxis]  # 增加维度用于广播
    return t * color1 + (1 - t) * color2

# 设置更大范围和更高分辨率以减少锯齿
max_radius = 5e6  # 扩大到500万像素半径
resolution = 3000  # 提高分辨率到3000x3000像素
x = np.linspace(-max_radius, max_radius, resolution)
y = np.linspace(-max_radius, max_radius, resolution)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# 计算足够多的k值覆盖范围外区域
k_max = int((c * max_radius**2) / (2 * np.pi)) + 30
radii = []
for k in range(0, k_max):
    inner = np.sqrt(2 * k * np.pi / c)
    outer = np.sqrt((2*k + 1) * np.pi / c)
    radii.append((inner, outer))

# 使用精确的矢量计算创建掩码
background_color = np.array(mcolors.to_rgb('#62529E'))  # 深紫色背景
ring_color = np.array(mcolors.to_rgb('#F7E9A3'))       # 浅黄色环

# 初始化为背景色
mask = np.ones(R.shape + (3,))  # RGB数组
mask = mask * background_color  # 应用背景色

# 精确绘制所有环
for k, (inner, outer) in enumerate(radii):
    # 计算距离边界的差异
    dist_inner = R - inner
    dist_outer = outer - R
    
    # 使用平滑过渡减少锯齿
    transition_width = min(5000, (outer - inner) * 0.1)  # 过渡宽度自适应
    
    # 对于内部区域
    if inner > 0:
        inner_mask = (R >= inner) & (R < inner + transition_width)
        mask[inner_mask] = transition(dist_inner[inner_mask], 0, transition_width, 
                                      background_color, ring_color)
    
    # 对于外部区域
    outer_mask = (R > outer - transition_width) & (R <= outer)
    if transition_width > 0:
        mask[outer_mask] = transition(dist_outer[outer_mask], 0, transition_width, 
                                      ring_color, background_color)
    
    # 主环区域（不含过渡）
    main_mask = (R >= inner + transition_width) & (R <= outer - transition_width)
    mask[main_mask] = ring_color

# 创建图形
plt.figure(figsize=(10, 10), dpi=100)
plt.imshow(mask, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')

# 添加标注
plt.text(0.98, 0.02, 
         f'显示 {len(radii)} 个同心环 | c = {c:.2e}',
         transform=plt.gca().transAxes, ha='right', va='bottom',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# 添加中心效果
plt.plot(0, 0, 'wo', markersize=5, alpha=0.7)

plt.title(r'$\sin\left((x^2 + y^2) \cdot 2.2858 \times 10^{-11}\right) \geq 0$', 
          fontsize=16, pad=20, color='white')
plt.axis('off')  # 隐藏坐标轴

plt.tight_layout()
plt.savefig('precise_rings.png', dpi=150, bbox_inches='tight')
plt.show()