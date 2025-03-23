from ftplib import FTP
import os
temp=os.environ["temp"]


def upload(f, remote_path, local_path):
    fp = open(local_path, "rb")
    buf_size = 1024
    f.storbinary("STOR {}".format(remote_path), fp, buf_size)
    fp.close()
def download(f, remote_path, local_path):
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(remote_path), fp.write, buf_size)
    fp.close()
def quit(f):
    f.quit()
def typefile(f,file):
    local_path=temp+"/TEMPfile"
    fp = open(local_path, "wb")
    buf_size = 1024
    f.retrbinary('RETR {}'.format(file), fp.write, buf_size)
    fp.close()
    f=open(local_path,"r",encoding="UTF-8")
    get=f.read()
    f.close()
    os.remove(local_path)
    return get
def nlst(ft,cwd=""):
    try:
        ft.nlst(cwd)
    except:
        return []
    return ft.nlst(cwd)
def DownLoadFileTree(ft, LocalDir, RemoteDir):
        def DownLoadFile(ft, LocalFile, RemoteFile):  # 下载单个文件
                file_handler = open(LocalFile, 'wb')
                ft.retrbinary('RETR ' + RemoteFile, file_handler.write)
                file_handler.close()
                return True
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        ft.cwd(RemoteDir)
        RemoteNames = ft.nlst()
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if file.find(".") == -1:
                if not os.path.exists(Local):
                    os.makedirs(Local)
                DownLoadFileTree(ft,Local, file)
            else:
                DownLoadFile(ft,Local, file)
        ft.cwd("..")
        return