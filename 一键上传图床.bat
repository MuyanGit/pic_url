@echo off
rem ����Ĭ��ֵ
set content="%date% %time%: Updated By MuyanGit"
set /p content= ���뱾���ύ�����ݣ�������ʡ�ԣ�

git add .

rem �ύ����

git commit -m %content%

rem ���͵������
rem git push

git push origin master --force && echo ִ�гɹ� || echo ִ��ʧ��


