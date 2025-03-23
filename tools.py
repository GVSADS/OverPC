#所需模块
#前置
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]=""
#UI库
import tkinter.filedialog as tf
import tkinter.messagebox as tm
import tkinter.ttk as ttk
import tkinter as tk
import pygame
pygame.mixer.init()
#系统库
import sys
from io import BytesIO
import platform
import getpass
import psutil
import shutil
import traceback
#配置文件库
import configparser
import json
#编码库
import binascii
import hashlib
import base64
import uuid
import re
#进程库
from threading import Thread
import subprocess
#时间库
import datetime,time
#图像库
from PIL import Image,ImageTk
import cv2
#网页库
import flask    
import flask_socketio
import webbrowser
import urllib.request
import requests
import ftplib
import ftp
import socket
#数学库
import random,math
#音频库
import wave
#Win32库
import win32gui
import win32api
import pystray
import pyautogui

#基础变量
temp=os.environ["temp"]

#读/写/添
def openw(file,write,mode="1",encoding="UTF-8"):
    if mode=="1" or mode==1:
        f=open(file,"w",encoding=encoding)
        f.write(write)
        f.close()
    elif mode=="2" or mode==2:
        f=open(file,"wb")
        f.write(write)
        f.close()
    else:
        return
    return
def opena(file,write,mode="1",encoding="UTF-8"):
    if mode=="1" or mode==1:
        f=open(file,"a",encoding=encoding)
        f.write(write)
        f.close()
    elif mode=="2" or mode==2:
        f=open(file,"ab")
        f.write(write)
        f.close()
    else:
        return
    return
def openr(file,mode="1",encoding="UTF-8"):
    if mode=="1" or mode==1:
        f=open(file,"r",encoding=encoding)
        read=f.read()
        f.close()
    elif mode=="2" or mode==2:
        f=open(file,"rb")
        read=f.read()
        f.close()
    else:
        return
    return read

#MP3播放
def MP3Play(mp3_path,volume=10,sleep=-1):
    pygame.mixer.music.load(mp3_path) # 加载音乐
    pygame.mixer.music.set_volume(volume)# 设置音量大小0~1的浮点数
    pygame.mixer.music.play() # 播放音频
    if sleep == -1:
        time.sleep(get_duration_wave(mp3_path))
    else:
        time.sleep(sleep)

#MP3时间获取
def get_duration_wave(file_path):
   with wave.open(file_path, 'r') as audio_file:
      frame_rate = audio_file.getframerate()
      n_frames = audio_file.getnframes()
      duration = n_frames / float(frame_rate)
      return duration

#时间格式化
def TimeFormat(s,end=""):
    return time.strftime('[%Y/%m/%d %H:%M:%S]: '+str(s)+end, time.localtime())

def Time(s="%Y/%m/%d %H:%M:%S"):
    return time.strftime(s, time.localtime())

#Base64转图片
def base64_to_image(base64_str: str) -> Image.Image:
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img

#图片转Base64
def image_to_base64(image: Image.Image, fmt='png') -> str:
    output_buffer = BytesIO()
    image.save(output_buffer, format=fmt)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    return f'data:image/{fmt};base64,' + base64_str

#异步装饰器
def asyncs(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

#获取一个文件MD5
def md5_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()

#获取多个文件MD5(自匹配)
def md5_files(*file_paths):
    md5_list = []
    for file_path in file_paths:
        md5_list.append(md5_file(file_path))
    return md5_list

#获取所有可用的摄像头设备
def get_available_cameras():
    camera_list = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            camera_list.append(index)
        cap.release()
        index += 1
    return camera_list

#任务栏高度
def get_taskbar_height():
    return win32api.GetSystemMetrics(4)

# 获取(x,y)位置的颜色
def on_more_color(x, y):
    # 获取(x,y)位置的颜色
    rgb = pyautogui.screenshot().getpixel((x, y))

    # 转换为十六进制格式
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    # 输出RGB和十六进制颜色值
    print(f"Mouse at ({x}, {y}) - RGB: {rgb}, Hex: {hex_color}")

#窗口居中
def index(root,W,H):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    width = W
    height = H
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
def index100(root,W,H):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    width = W
    height = H
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2 - 100
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
def index50(root,W,H):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    width = W
    height = H
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2 - 50
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))



# -*- coding: utf-8 -*-
import win32api
import win32con,winreg,os

"""判断键是否存在"""
def Judge_Key(key_name,
              reg_root=win32con.HKEY_CURRENT_USER,#根节点  其中的值可以有：HKEY_CLASSES_ROOT、HKEY_CURRENT_USER、HKEY_LOCAL_MACHINE、HKEY_USERS、HKEY_CURRENT_CONFIG
              reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",# 键的路径
              ):
    # print(key_name)
    """
    :param key_name: #  要查询的键名
    :param reg_root: # 根节点
#win32con.HKEY_CURRENT_USER
#win32con.HKEY_CLASSES_ROOT
#win32con.HKEY_CURRENT_USER
#win32con.HKEY_LOCAL_MACHINE
#win32con.HKEY_USERS
#win32con.HKEY_CURRENT_CONFIG
    :param reg_path: #  键的路径
    :return:feedback是（0/1/2/3：存在/不存在/权限不足/报错）
    """
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    try:
        key = winreg.OpenKey(reg_root, reg_path, 0, reg_flags)
        location, type = winreg.QueryValueEx(key, key_name)
        print("键存在", "location（数据）:", location, "type:", type)
        feedback=0
    except FileNotFoundError as e:
        print("键不存在",e)
        feedback =1
    except PermissionError as e:
        print("权限不足",e)
        feedback = 2
    except:
        print("Error")
        feedback = 3
    return  feedback

"""开机自启动"""
def AutoRun(switch="open",#开：open # 关：close
            zdynames=None,
            current_file=None,
            abspath = os.path.abspath(os.path.dirname(__file__))):
    """
    :param switch: 注册表开启、关闭自启动
    :param zdynames: 当前文件名
    :param current_file: 获得文件名的前部分
    :param abspath: 当前文件路径
    :return:
    """
    print(zdynames)

    path = abspath + '\\' + zdynames  # 要添加的exe完整路径如：
    judge_key = Judge_Key(reg_root=win32con.HKEY_CURRENT_USER,
                          reg_path=r"Software\Microsoft\Windows\CurrentVersion\Run",  # 键的路径
                          key_name=current_file)
    # 注册表项名
    KeyName = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, KeyName, 0, win32con.KEY_ALL_ACCESS)
    if switch == "open":
        # 异常处理
        try:
            if judge_key==0:
                print("已经开启了，无需再开启")
            elif judge_key==1:
                win32api.RegSetValueEx(key, current_file, 0, win32con.REG_SZ, path)
                win32api.RegCloseKey(key)
                print('开机自启动添加成功！')
        except:
            print('添加失败')
    elif switch =="close":
        try:
            if judge_key==0:
                win32api.RegDeleteValue(key, current_file)  # 删除值
                win32api.RegCloseKey(key)
                print('成功删除键！')
            elif judge_key==1:print("键不存在")
            elif judge_key==2:print("权限不足")
            else:print("出现错误")
        except:
            print('删除失败')


def get_available_drives():
    drives = []
    for drive in range(ord('A'), ord('Z')+1):
        drive_name = chr(drive) + ":\\"
        if os.path.exists(drive_name):
            drives.append(drive_name)

    return drives

def SELFYD(title,root):#漂浮窗窗口
    def StartMove(event):
        global x, y
        x = event.x
        y = event.y
    def StopMove(event):
        global x, y
        x = None
        y = None
    def OnMotion(event):
        global x, y
        deltax = event.x - x
        deltay = event.y - y
        root.geometry("+%s+%s" % (root.winfo_x() + deltax, root.winfo_y() + deltay))
        root.update()
    title.bind("<ButtonPress-1>", StartMove)
    title.bind("<ButtonRelease-1>", StopMove)
    title.bind("<B1-Motion>", OnMotion)


def is_internet_available():
    try:
        urllib.request.urlopen('https://www.baidu.com')
        return True
    except:
        return False

def Get(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return SystemError

def Post(url,data=dict):
	try:
		r = requests.post(url=url,data=data)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return SystemError


class G:
    def wifiT(url):
        try:
            host = socket.gethostbyname(url)
            s = socket.create_connection((host, 80), 2)
            return True
        except Exception as e:
            return False
def Computer_data(get=str):
    #计算机的网络名称
    node=platform.node()
    #获取操作系统名称及版本号
    platformstr=platform.platform()
    #计算机处理器信息
    processor=platform.processor()
    #获取系统类型,如windows
    system=platform.system()
    #获取系统盘
    winpath = os.environ["WINDIR"][:-7]
    #获取用户列表
    Users=os.listdir(winpath+"Users")
    #获取应用列表
    Program_Filesx86=os.listdir(winpath+"Program Files (x86)")
    #获取系统应用列表
    Program_Files=os.listdir(winpath+"Program Files")
    #获取temp缓存目录
    temp=os.environ["temp"]
    #获取当前用户
    Userspath=os.environ["USERPROFILE"]
    #获取当前桌面文件
    Desktop=os.listdir(Userspath+r"\Desktop")
    #获取Fonts字体
    Fonts=os.listdir(winpath+r"windows\Fonts")
    #获取是否联网
    wifi=G.wifiT(url="www.baidu.com")
    if get == "node":
        return node
    elif get == "platformstr":
        return platformstr
    elif get == "processor":
        return processor
    elif get == "system":
        return system
    elif get == "winpath":
        return winpath
    elif get == "Users":
        return Users
    elif get == "Program_Filesx86":
        return Program_Filesx86
    elif get == "Program_Files":
        return Program_Files
    elif get == "Userspath":
        return Userspath
    elif get == "Desktop":
        return Desktop
    elif get == "Fonts":
        return Fonts
    else:
        return None