import win32gui
from win32.lib import win32con
import time
import win32process
import datetime

def handle_window(hwnd, extra):
 if win32gui.IsWindowVisible(hwnd):
     if '交易开拓者平台' in win32gui.GetWindowText(hwnd):
         #print(hwnd)#10进制句柄
         #print(hex(hwnd))#16进制
         win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
         
def Close_DialogBox():
    time.sleep(5)
    hd=win32gui.FindWindow('#32770','确认')
    #print(type(hd))
    #print(hex(hd))
    hdc=win32gui.FindWindowEx(hd,0,'Button','是(&Y)')
    #print(hex(hdc))
    time.sleep(5)
    win32gui.SendMessage(hdc,win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
    time.sleep(3)
    win32gui.SendMessage(hdc,win32con.BM_CLICK,1,0)
    '''
    win32gui.SendMessage(hdc,win32con.WM_KEYDOWN,win32con.VK_SPACE,0)#压下空格
    time.sleep(1)
    win32gui.SendMessage(hdc,win32con.WM_KEYUP,win32con.VK_SPACE,0)#抬起空格
    '''
    
def TB_Open():
    handle = win32process.CreateProcess('C:/Users/Administrator/Documents/tbv5321_x64_portable/TradeBlazer.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None,'C:/Users/Administrator/Documents/tbv5321_x64_portable/',win32process.STARTUPINFO())#打开TB,获得其句柄  
    time.sleep(25)
    
if __name__=='__main__':
    while 1:
        if datetime.datetime.now().weekday()>0 and datetime.datetime.now().weekday()<=6:
            if time.ctime()[12:19] == "8:50:00" or time.ctime()[12:19] == "20:50:00" :
                TB_Open()
                time.sleep(15)
            if time.ctime()[12:19] == "15:35:00" or time.ctime()[12:19] == "2:35:00" :
                win32gui.EnumWindows(handle_window,None)
                #time.sleep(1)
                Close_DialogBox()
                time.sleep(10)
