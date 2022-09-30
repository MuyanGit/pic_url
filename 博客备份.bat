@echo OFF
::重装系统后注意两处盘符的修改
G:
G:\Demo_Git\pic_url\
start D:\MySoftware\DEV\VersionCtrl\Git\git-bash.exe -c "pic_url_backup.sh"
git add .
git commit -m "From Auto Updata"
git push -u origin master -f 
git pull –rebase origin master