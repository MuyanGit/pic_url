'''
Author: muyangit muyangit@outlook.com
Date: 2022-10-20 20:22:26
LastEditors: muyangit muyangit@outlook.com
LastEditTime: 2022-10-20 23:37:06
FilePath: \AutoJSg:\Demo_Git\pic_url\自动监听文件变化.py
Description: 

Copyright (c) 2022 by muyangit muyangit@outlook.com, All Rights Reserved. 
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<检测文件夹变化>

# 导入watchdog对应模块
from watchdog.observers import Observer
from watchdog.events import *
# 导入时间模块
import time
# 导入系统模块
import os


#设置删除多少天前的文件
def deletefile(path,N = 2,ext = '.log'):
    """设置删除多少天前的文件

    Args:
        path (_type_): path
        N (int, optional): 天数. Defaults to 2.
        ext (str, optional): 扩展名. Defaults to '.log'.
    """
    for eachfile in os.listdir(path):
                filename = os.path.join(path,eachfile)
                if os.path.isfile(filename):
                            lastmodifytime = os.stat(filename).st_mtime
                            endfiletime = time.time() - 3600 * 24 * N #设置删除多久之前的文件
                            if endfiletime > lastmodifytime:
                                if ext in filename:
                                    os.remove(filename)
                                    #print "删除文件 %s 成功" % filename
                elif os.path.isdir(filename):#如果是目录则递归调用当前函数
                        deletefile(filename)

def os_system(pro_path,sh_file):
    """git-bash.exe--cmd调用

    Args:
        pro_path (_type_): 项目路径
        sh_file (_type_): 路径的脚本sh_file
    """
    cmd_=f'start D:\MySoftware\DEV\VersionCtrl\Git\git-bash.exe --cd={pro_path} -c "bash {sh_file}"'
    os.system(cmd_)

def push(change):
    """_summary_

    Args:
        change (_type_): _description_
    """
    print('-'*76)
    os_system('G:\Demo_Git\pic_url','一键上传图床.sh')
    print('·'*76)
    # 备份博客
    os_system('G:\MuyanGitBlog\MuyanGit\杂项\博客备份','bolg_backup.sh')
    os_system('G:\MuyanGitBlog\PonyTown2020\杂项\博客备份','bolg_backup.sh')
    # os.system()
    print('+'*76)


class FileEventHandler(FileSystemEventHandler):
    # 初始化魔术方法
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # 文件或文件夹移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))
            # 这里我们只判断文件修改,如需加入文件夹修改,只需在上面的if条件中调用push函数即可
            push("文件移动: {0} to {1}".format(event.src_path, event.dest_path))

    # 创建文件或文件夹
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            push("创建文件:{0}".format(event.src_path))

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))
            push("删除文件:{0}".format(event.src_path))

    # 移动文件或文件夹
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            push("文件修改:{0}".format(event.src_path))


if __name__ == "__main__":
    deletefile(r'G:\MuyanGitBlog\MuyanGit\杂项\博客备份',7,'.txt\uf03a')
    deletefile(r'G:\MuyanGitBlog\PonyTown2020\杂项\博客备份',7,'.txt\uf03a')
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = r"G:\Demo_Git\pic_url\img"
    observer.schedule(event_handler, dis_dir, True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(300)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    