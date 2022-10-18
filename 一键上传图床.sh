#!/bin/bash
#author Oliver
#since 2020-09-03 15:24:31
 
#git remote rm origin
#replace your git location
#git remote add origin 'https://github.com/**********'
git pull remote master
git add .
#执行shell脚本，可以传一个参数 $1 是git 的提交的msg：./shell.sh "提交代码"
git commit -m $1
git push origin master --force
#执行成功
if [ "$?" = "0" ]
then
  echo -e "\033[42;34m push to github success! \033[0m"
else
   echo -e "\033[41;30m push to github fail! \033[0m"
   exit 1
fi
 