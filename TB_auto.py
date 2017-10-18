#打开方式1
#import win32api
#win32api.ShellExecute(0,'open','notepad.exe','','',1)
#win32api.ShellExecute(0,'open','C:/Users/Administrator/Documents/tbv5321_x64_portable/TradeBlazer.exe','','C:/Users/Administrator/Documents/tbv5321_x64_portable/',1)

#打开方式2
#import os
#os.system('notepad')
#os.system('C:/Users/Administrator/Documents/tbv5321_x64_portable/TradeBlazer.exe')

#打开方式3
import win32process
handle = win32process.CreateProcess('C:/Users/Administrator/Documents/tbv5321_x64_portable/TradeBlazer.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None,'C:/Users/Administrator/Documents/tbv5321_x64_portable/',win32process.STARTUPINFO())#打开TB,获得其句柄  
print (handle)#打印句柄(函数返回进程句柄、线程句柄、进程ID以及线程ID)
import time
time.sleep(25)#24秒 监控器弹出

#关闭TB
win32process.TerminateProcess(handle[0],0)#终止进程




'''
import win32ui
import win32con

wnd=win32ui.FindWindow('Afx:0000000140000000:8:0000000000010003:0000000000000000:00000000012A0309','交易开拓者平台(旗舰版) 64位 - [工作区1-rb888 1日线]')
wnd.SendMessage(win32con.WM_CLOSE)
time.sleep(5)

#wnd=win32ui.FindWindow('#32770','自动交易头寸监控器')
#wnd.SendMessage(win32con.WM_CLOSE)
#time.sleep(5)
w=win32ui.FindWindow('#32770','确认')
time.sleep(3)
#w=win32ui.FindWindow('Button','是(&Y)')
b=w.GetDlgItem('Button','是(&Y)')
b.postMessage(win32con.BM_CLICK)
'''
