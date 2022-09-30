#!/bin/bash
#重装系统后注意两处盘符的修改
##exec 1>>G:\Demo_Git\pic_url\log.txt 2>&1
##cd G:\Demo_Git\pic_url

NowDateTime=$(date +%Y-%m-%d)
file="backup_log/log.txt"
filename=${NowDateTime}${file}
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>>${filename}: 2>&1
# Everything below will go to the file filename

# 执行的命令主体
echo 开始运行备份命令
echo `date`······备份进行中 
git add .
git commit -m "From Auto Updata"
git push -u origin master -f 
git pull –rebase origin master
echo 图床备份结束运行备份命令——————————————
echo `date`······备份结束中