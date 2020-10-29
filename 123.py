import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
win = tk.Tk()

# 定义功能函数, event是必须添加的参数，不知道来自哪里

def button_command1():
    t = np.linspace(0,2,200)
    f1 = np.exp(-3*t)
    f2 = np.sin(4*np.pi*t)
    plt.subplot(111)
    plt.plot(t,f1)
    plt.show()
def button_command2():
    t = np.linspace(0,2,200)
    f2 = np.sin(4*np.pi*t)
    plt.subplot(111)
    plt.plot(t,f2)
    plt.show()
def button_command3():
    t = np.linspace(0,2,200)
    f1 = np.exp(-3*t)
    f2 = np.sin(4*np.pi*t)
    plt.subplot(111)
    plt.plot(t,f1*-f2)
    plt.show()
def button_command4():
    plt.subplot(111)
    def unit(t):
        r=np.where(t>0.0,1.0,0.0)
        return r
    t=np.linspace(-1.0,3.0,1000)
    plt.ylim(-1.0,3.0)
    plt.plot(t,unit(t))
    plt.show()

# 绑定事件

btn1 = tk.Button(win, text="指数信号", command=button_command1)
btn1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
win.geometry("300x300+200+200")

btn2 = tk.Button(win, text="正弦信号", command=button_command2)
btn2.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.2)
win.geometry("300x300+200+200")

btn3 = tk.Button(win, text="指数衰减的正弦信号", command=button_command3)
btn3.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.2)
win.geometry("300x300+200+200")

btn4 = tk.Button(win, text="阶跃信号", command=button_command4)
btn4.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.2)
win.geometry("300x300+200+200")

win.mainloop()


