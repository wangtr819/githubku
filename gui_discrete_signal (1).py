import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal_type):
    # 创建一个新的 Figure 对象，用于绘制图形
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    # 在 Figure 中添加一个子图
    ax = fig.add_subplot(111)

    if signal_type == 'impulse':
        # 生成从 -10 到 10 的整数序列
        n = np.arange(-10, 11)
        # 创建一个与 n 长度相同的全零数组
        x = np.zeros_like(n)
        # 将 n 等于 0 的位置对应的 x 元素设为 1，生成单位冲激信号
        x[n == 0] = 1
        # 使用 stem 函数绘制离散信号
        ax.stem(n, x)
        # 设置子图的标题
        ax.set_title('Impulse Signal')
    elif signal_type == 'step':
        n = np.arange(-10, 11)
        # 生成单位阶跃信号，当 n 大于等于 0 时为 1，否则为 0
        x = np.where(n >= 0, 1, 0)
        ax.stem(n, x)
        ax.set_title('Step Signal')
    elif signal_type == 'ramp':
        n = np.arange(-10, 11)
        # 生成斜坡信号，当 n 大于等于 0 时为 n，否则为 0
        x = np.where(n >= 0, n, 0)
        ax.stem(n, x)
        ax.set_title('Ramp Signal')

    # 设置 x 轴标签
    ax.set_xlabel('n')
    # 设置 y 轴标签
    ax.set_ylabel('x[n]')

    # 创建一个 FigureCanvasTkAgg 对象，用于将 matplotlib 的图形嵌入到 tkinter 窗口中
    canvas = FigureCanvasTkAgg(fig, master=root)
    # 绘制图形
    canvas.draw()
    # 将图形显示在 tkinter 窗口中，并设置布局
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)


# 创建主窗口
root = tk.Tk()
# 设置主窗口的标题
root.title("Discrete Signal Plotter")

# 创建一个按钮，点击时调用 plot_signal 函数并传入 'impulse' 参数
button_impulse = tk.Button(root, text="Impulse Signal", command=lambda: plot_signal('impulse'))
# 使用 grid 布局管理器将按钮放置在第 0 行第 0 列
button_impulse.grid(row=0, column=0)

# 创建一个按钮，点击时调用 plot_signal 函数并传入 'step' 参数
button_step = tk.Button(root, text="Step Signal", command=lambda: plot_signal('step'))
button_step.grid(row=0, column=1)

# 创建一个按钮，点击时调用 plot_signal 函数并传入 'ramp' 参数
button_ramp = tk.Button(root, text="Ramp Signal", command=lambda: plot_signal('ramp'))
button_ramp.grid(row=0, column=2)

# 进入主事件循环，使窗口保持显示并处理用户的操作
root.mainloop()
    