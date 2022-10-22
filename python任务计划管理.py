#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python任务计划管理.py
@Time    :   2022/10/22 01:17:43
@Author  :   muyangit 
@Version :   1.0
@Contact :   muyangit@outlook.com
@License :   (C)Copyright 2021-2025, muyangit&laysen
@Desc    :   None
'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import schedule
import time
import os


# 定义你要周期运行的函数
def job():
    print("I'm working...")

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

def deletelog():
    deletefile(r'G:\MuyanGitBlog\MuyanGit\杂项\博客备份',7)
    deletefile(r'G:\MuyanGitBlog\PonyTown2020\杂项\博客备份',7)    


def os_system(pro_path,sh_file):
    """git-bash.exe--cmd调用

    Args:
        pro_path (_type_): 项目路径
        sh_file (_type_): 路径的脚本sh_file
    """
    cmd_=f'start D:\MySoftware\DEV\VersionCtrl\Git\git-bash.exe --cd={pro_path} -c "bash {sh_file}"'
    print(f"执行{pro_path}\{sh_file}")
    os.system(cmd_)

def push_pic(change):
    """备份图床

    Args:
        change (_type_): _description_
    """
    # 备份图床
    print('·'*38)
    os_system('G:\Demo_Git\pic_url','一键上传图床.sh')
    print('·'*38)


def push_bolg_backup(change):
    """_summary_

    Args:
        change (_type_): _description_
    """
    # 备份图床
    print('-'*76)
    os_system('G:\Demo_Git\pic_url','一键上传图床.sh')
    print('·'*38)
    # 备份博客
    os_system('G:\MuyanGitBlog\MuyanGit\杂项\博客备份','bolg_backup.sh')
    print('·'*38)
    os_system('G:\MuyanGitBlog\PonyTown2020\杂项\博客备份','bolg_backup.sh')
    # os.system()
    print('+'*76)


def push_git():
    from git import Repo
    import os

    os.system(r"G:\MuyanGitBlog\MuyanGit\杂项\博客备份\博客备份.bat")

    # 上传图片到 pic_url
    mydirfile = os.path.abspath(r'G:\Demo_Git\pic_url')  # code的文件位置，我默认将其存放在根目录下
    repo = Repo(mydirfile)

    g = repo.git
    g.add("--all")
    try:
        g.commit("-m auto update" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        # print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        g.push()
        print("Successful push!")
    except BaseException as e:
        print("Failed push!")


def do_job():
    schedule.every(5).minutes.do(push_pic)  # 每隔 10 分钟运行一次 job 函数
    schedule.every(4).hours.do(push_bolg_backup)  # 每隔 1 小时运行一次 job 函数
    schedule.every(9).hours.do(deletelog)  # 每隔 1 小时运行一次 job 函数
    schedule.every().day.at("10:30").do(job)  # 每天在 10:30 时间点运行 job 函数
    # schedule.every().monday.do(job)  # 每周一 运行一次 job 函数
    # schedule.every().wednesday.at("13:15").do(job)  # 每周三 13：15 时间点运行 job 函数
    # schedule.every().minute.at(":17").do(job)  # 每分钟的 17 秒时间点运行 job 函数
    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(1)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # push_git()
    do_job()
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
