@echo OFF
::重装系统后注意两处盘符的修改
G:
G:\Demo_Git\pic_url\
git add .
git commit -m "From Auto Updata"
git push -u origin master -f 
git pull –rebase origin master