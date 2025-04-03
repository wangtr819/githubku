import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(signal_type):
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    if signal_type == 'impulse':
        n = np.arange(-10, 11)
        x = np.zeros_like(n)
        x[n == 0] = 1
        ax.stem(n, x)
        ax.set_title('Impulse Signal')
    elif signal_type == 'step':
        n = np.arange(-10, 11)
        x = np.where(n >= 0, 1, 0)
        ax.stem(n, x)
        ax.set_title('Step Signal')
    elif signal_type == 'ramp':
        n = np.arange(-10, 11)
        x = np.where(n >= 0, n, 0)
        ax.stem(n, x)
        ax.set_title('Ramp Signal')

    ax.set_xlabel('n')
    ax.set_ylabel('x[n]')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)


root = tk.Tk()
root.title("Discrete Signal Plotter")

button_impulse = tk.Button(root, text="Impulse Signal", command=lambda: plot_signal('impulse'))
button_impulse.grid(row=0, column=0)

button_step = tk.Button(root, text="Step Signal", command=lambda: plot_signal('step'))
button_step.grid(row=0, column=1)

button_ramp = tk.Button(root, text="Ramp Signal", command=lambda: plot_signal('ramp'))
button_ramp.grid(row=0, column=2)

root.mainloop()
    