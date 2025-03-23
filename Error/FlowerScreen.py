from random import randint
from threading import Thread
import tkinter as tk
import time
 

def Start():
    root = tk.Tk()
    root.attributes('-transparentcolor','#f0f0f0')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.overrideredirect(True)
    root.state("zoomed")
    root.attributes('-topmost', True)
    root.update()

    def draw_line(canvas, x1, y1, x2, y2, color):
        canvas.create_line(x1, y1, x2, y2, fill=color)
    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    root.withdraw()
    for y in range(0, randint(300,400)):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(randint(500,600), 600):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(800, 1000):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(1200, 1500):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(2000, 3000):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(3500, 4000):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    for y in range(4200, 10000):
        color = f"#{randint(0, 0xFFFFFF):06x}"  # 随机生成颜色
        draw_line(canvas, y, 1, y, screen_width, color)
    root.update()
    root.withdraw()
    root.update()
    time.sleep(0.2)
    root.deiconify()
    root.update()
    time.sleep(0.2)
    root.withdraw()
    root.update()
    time.sleep(0.1)
    root.deiconify()
    root.update()
    time.sleep(0.1)
    time.sleep(2)
    root.withdraw()
    root.update()
    time.sleep(0.1)
    root.deiconify()
    root.update()
    time.sleep(0.1)
    root.withdraw()
    root.update()
    time.sleep(0.1)
    root.deiconify()
    root.update()
    time.sleep(0.1)
    root.withdraw()
    root.update()
if __name__ == "__main__":
    Start()