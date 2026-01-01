import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False

# 1. 定义维度与数据
labels = ['操作', '运营', '战术', '大局观', '心态']
players = {
    '荣华': [6.0, 6.0, 5.0, 5.5, 5.0],
    'lium': [6.5, 6.5, 5.5, 6.0, 6.5],
    '钢总': [7.5, 7.5, 6.0, 6.5, 7.5],
    '龙哥': [8.5, 9.5, 7.0, 7.0, 8.5],
    '导师': [9.0, 9.0, 7.5, 8.0, 8.5]
}
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']  # 区分选手颜色

# 2. 雷达图基础设置
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]  # 闭合图形
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

# 3. 绘制每个选手的雷达图
for idx, (name, values) in enumerate(players.items()):
    values += values[:1]  # 闭合数据
    ax.plot(angles, values, 'o-', linewidth=2, label=name, color=colors[idx])
    ax.fill(angles, values, alpha=0.25, color=colors[idx])

# 4. 图表美化与标注
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_ylim(0, 10)
ax.set_yticks(range(0, 11, 2))
ax.set_title('魔兽争霸3 SSG顶尖选手六维能力雷达图（10分制）', fontsize=16, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
plt.tight_layout()
plt.show()