#!/bin/bash
#author Oliver
#since 2020-09-03 15:24:31
 
#git remote rm origin
#replace your git location
#git remote add origin 'https://github.com/**********'
#cd G:/Demo_Git/pic_url
echo "----------本地库状态----------"
git status
echo "----------本地库状态----------"
createAt=$(date "+%Y-%m-%d %H:%M:%S")
#git pull remote master
git add .
#执行shell脚本，可以传一个参数 $1 是git 的提交的msg：./shell.sh "提交代码"
#git commit -m $1
git commit -m "${createAt}"
git push origin master --force
#执行成功
if [ "$?" = "0" ]
then
  echo -e "\033[42;34m push to github success! \033[0m"
  ping localhost -n 3
else
   echo -e "\033[41;30m push to github fail! \033[0m"
   ping localhost -n 3
   exit 1
fi
 