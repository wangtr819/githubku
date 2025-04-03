import numpy as np
import matplotlib.pyplot as plt

# 生成连续信号
t_continuous = np.linspace(0, 1, 1000)
y_continuous = np.sin(2 * np.pi * 5 * t_continuous)

# 生成离散信号
t_discrete = np.arange(0, 1, 0.1)
y_discrete = np.sin(2 * np.pi * 5 * t_discrete)

# 绘制连续信号
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, y_continuous)
plt.title('Continuous Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# 绘制离散信号1
plt.subplot(1, 2, 2)
plt.stem(t_discrete, y_discrete)
plt.title('Discrete Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
 
