::删除过程文件夹
rd /s /q C:\Users\Administrator\tb\__pycache__
rd /s /q C:\Users\Administrator\tb\build\AutoRunTB
pause
::删除生成文件和启动目录文件
del /f/s/q C:\Users\Administrator\tb\dist\AutoRunTB.exe
del /f/s/q "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\AutoRunTB.exe"
pause
::打包exe后拷贝到启动目录下
pyinstaller -F -i C:\Users\Administrator\tb\qihuo.ico C:\Users\Administrator\tb\AutoRunTB.py
copy "C:\Users\Administrator\tb\dist\AutoRunTB.exe" "C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
pause
::重启电脑
shutdown -r -f -t 0
