@echo off
rem 设置默认值
set content="%date% %time%: Updated By MuyanGit"
set /p content= 输入本次提交的内容，不建议省略：

git add .

rem 提交更新

git commit -m %content%

rem 推送到服务端
rem git push

git push origin master --force && echo 执行成功 || echo 执行失败


pause