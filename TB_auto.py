#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
print(type (handle))
print (handle)#打印句柄(函数返回进程句柄、线程句柄、进程ID以及线程ID)
print(type (handle[0]))
#print (dir(handle[0]))
print (handle[0].handle)
print (handle[1].handle)
print (handle[2])
print (handle[3])

print ('%x' % (handle[0].handle))
print ('%x' % (handle[1].handle))
print ('%x' % (handle[2]))
print ('%x' % (handle[3]))
import time
#time.sleep(25)#24秒 监控器弹出

time.sleep(10)


import win32gui, win32con, win32api
import time, math, random
  
def _MyCallback( hwnd, extra ):
    windows = extra
    temp=[]
    temp.append(hex(hwnd))                   #窗口句柄 16进制
    temp.append(win32gui.GetClassName(hwnd)) #窗口类名
    temp.append(win32gui.GetWindowText(hwnd))#窗口标题
    windows[hwnd] = temp
  
def TestEnumWindows():
    windows = {}#字典
    win32gui.EnumWindows(_MyCallback, windows)#枚举窗口
    print ("Enumerated a total of  windows with %d classes",(len(windows)))
    print ('------------------------------')
    #print classes
    print ('-------------------------------')
    for item in windows :
        print  (windows[item])

print ("Enumerating all windows...")
TestEnumWindows()
print (type(handle[2]))
#print(chr(handle[2]).encode)
#print(handle[2])

def TBF(st1):
    windows = {}
    win32gui.EnumWindows(_MyCallback, windows)#枚举窗口
   # for item in windows :
        #print  (windows[item])
        #st2 = '交易开拓者平台(旗舰版) 64位 - [工作区1-rb888 5分钟线]'
                                #
    for t in windows.values():
        for item in windows :
            if st1 in str(t[2]):
                if (s_temp != str(t[2])):
                    s_temp = str(t[2])                
                    print  (s_temp)
                                        #else:
                                           #print("没找到"+str(windows.keys()))
                                #return st2

#h=win32gui.FindWindow(None,hex(handle[2])) #int->unico:chr()
        
h=win32gui.FindWindow(None,'交易开拓者平台(旗舰版) 64位 -') #int->unico:chr()
print (hex(h))

h1=win32gui.FindWindow(None,'交易开拓者平台(旗舰版) 64位 - [工作区1-rb888 5分钟线]') #int->unico:chr()
print (hex(h1))

TBF('交易开拓者平台(旗舰版)')
#_MyCallback(h,'#32770')
time.sleep(5)
hd=win32process.GetWindowThreadProcessId (handle[2])
print((hd[1]))
print ("All tests done!")

'''
import win32gui
left,top,right,bottom = win32gui.GetWindowRect(handle[2])
win32api.SetCursorPos((left+5,top+5))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) 
time.sleep(0.05) 
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
'''
time.sleep(2500000)

win32process.TerminateProcess(handle[0],0)#终止进程
print('关闭TB')
'''
import win32ui
import win32con

wnd=win32ui.FindWindow('Afx:0000000140000000:8:0000000000010003:0000000000000000:00000000012A0309','交易开拓者平台(旗舰版) 64位 - [工作区1-rb888 1日线]')
left, top, right, bottom = win32gui.GetWindowRect(handle[0])
win32api.SetCursorPos((left+5,top+5))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) 
time.sleep(0.05) 
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

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
