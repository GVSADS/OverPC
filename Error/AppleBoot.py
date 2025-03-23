from random import randint
from threading import Thread
import tkinter as tk
import time



#异步装饰器
def asyncs(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper


def Start():
    root = tk.Tk()
    root.attributes('-transparentcolor','#f0f0f0')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.overrideredirect(True)
    root.state("zoomed")
    root.attributes('-topmost', True)
    root.update()

    def Text(text):
        tk.Label(root,text=text,fg="#FFF",bg="#000",font=("Moder DOS 437",15)).pack(anchor="sw")
    def FText():
        tk.Label(root,text="",font=("Moder DOS 437",15)).pack(anchor="sw")
    Text("Please contact the Voodoo Kernel Dev-Team with a photo of the Information printed below,")
    Text("Along With a description of your system configuration and what you were doing at the time that")
    Text("the kernel panic occurred. We appologize for the lnconvenience")
    FText()
    Text('Panic(CPU 0 Caller 0x001AC05E): "Windows Teacher Error"')
    Text("Debugger Called: <Panic>")
    Text("Backtrace (CPU 0),Frame : Return Address (4 potential ponies on stack)")
    Text("0x14e1ffce68 : 0x12b08c (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("0x14e1ffce69 : 0x12b07c (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("0x14e1ffce70 : 0x12b05c (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("0x14e1ffce23 : 0x12b0cc (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("0x14e1ffcf35 : 0x12b0fc (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("0x14e1ffcf90 : 0x12b0ac (0xfffffffff 0xfffffffff 0xfffffffff)")
    Text("Backtrace terminated-invalid frame pointer 0")
    FText()
    Text("BSD process name corresponding to current thread: Unknown")
    FText()
    Text("Windows version:")
    Text("Win 32/Run")
    FText()
    Text("Kernel version:")
    Text("Win32 Kernel V3.2.5 / EFI Boot System V7")
    inputlabel=tk.Label(root,text=" ",fg="#434343",bg="#434343",font=("Moder DOS 437",15))
    inputlabel.pack(anchor="sw")

    @asyncs
    def forget():
        for _ in range(10):
            inputlabel.pack_forget()
            time.sleep(0.3)
            inputlabel.pack(anchor="sw")
            time.sleep(0.3)
        time.sleep(5)
        root.destroy()
    forget()
    
    @asyncs
    def bg():
        for _ in range(5):
            time.sleep(0.1)
            root["bg"]="#f0f0f0"
            time.sleep(0.1)
            root["bg"]="#000"
            time.sleep(0.1)
            root["bg"]="#f0f0f0"
    bg()

    root.mainloop()
if __name__ == "__main__":
    Start()