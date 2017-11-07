import win32gui
from win32.lib import win32con
import time
import win32process
import datetime
from commctrl import LVM_GETITEMTEXT,LVM_GETITEMCOUNT

week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }

path   = 'C:/Users/Administrator/Documents/tbv5321_x64_portable/'
mylog  = path+'LOG_'+time.strftime('%Y%m%d')+'_'+week_day[datetime.datetime.now().weekday()]+'.txt'

def Open_TB(username,password):
    #打开TB
    handle = win32process.CreateProcess(path+'TradeBlazer.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None,path,win32process.STARTUPINFO())#打开TB,获得其句柄
    time.sleep(2)
    #数据重置
    win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'Button','数据重置'),win32con.BM_CLICK,1,0)
    time.sleep(2)
    win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','数据重置'),0,'Button','重置(&R)'),win32con.BM_CLICK,1,0)
    time.sleep(2)
    win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认'),0,'Button','是(&Y)'),win32con.BM_CLICK,1,0)
    time.sleep(2)
    win32gui.PostMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','提示'),0,'Button','确定'),win32con.BM_CLICK,1,0)
    time.sleep(2)
    #登录框
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'ComboBox',None),0,'Edit',None),win32con.WM_SETTEXT,0,username)
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'Edit',None),win32con.WM_SETTEXT,0,password)
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'Button','登录(&L)'),win32con.BM_CLICK,1,0)
    #TB句柄
    time.sleep(10)
    win32gui.EnumWindows(handle_window,'交易开拓者')

def handle_window(hwnd,extra):#TB句柄
    if win32gui.IsWindowVisible(hwnd):
        if extra in win32gui.GetWindowText(hwnd):
            global TB
            TB = hwnd
def Close_Monit():
    win32gui.PostMessage(win32gui.FindWindow('#32770','自动交易头寸监控器'),win32con.WM_CLOSE,0,0)
    time.sleep(2)
    print(hex(win32gui.FindWindow('#32770','确认 ')))
    time.sleep(1)
    print(hex(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认 '),0,'Button','是(&Y)')))
    time.sleep(1)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认 '),0,'Button','是(&Y)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认 '),0,'Button','是(&Y)'),win32con.BM_CLICK,0,0)
    
def Close_TB():
    #win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),27),0)#退出程序(菜单方式）
    win32gui.PostMessage(TB,win32con.WM_CLOSE,0,0)
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认'),0,'Button','是(&Y)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认'),0,'Button','是(&Y)'),win32con.BM_CLICK,1,0)
    print('关闭TB')

def Login_Agin():
    while 1:
        n = win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindowEx(TB,win32gui.FindWindowEx(TB,0,'AfxControlBar110',None),'AfxControlBar110',None),0,None,'帐户管理'),0,'SysListView32',None),LVM_GETITEMCOUNT)
        if n <1:
            win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),7),17),0)#帐户登录
            win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','帐户登录'),0,'Button','登录(&L)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
            time.sleep(2)
            win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','帐户登录'),0,'Button','登录(&L)'),win32con.BM_CLICK,1,0)
            time.sleep(20)
        else:
            break;
    #win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),26),0)#锁定程序

if __name__=='__main__':
    while 1:
        if datetime.datetime.now().weekday()<=5:
            if time.ctime()[12:19] == "8:50:00" or time.ctime()[12:19] == "20:50:00" :
                Open_TB('sqltxt','iamanothwolf')
                time.sleep(25)
                Login_Agin()
                time.sleep(3)
                win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),22),0)#启动所有自动交易
                time.sleep(2)
                win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),7),11),0)#监控器
                time.sleep(10)
            if time.ctime()[12:19] == "15:35:00" or time.ctime()[12:19] == "2:35:00" :
                Close_Monit()
                time.sleep(2)
                win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),9),0)#保存所有工作区
                time.sleep(2)
                win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),23),0)#停止所有自动交易
                time.sleep(2)
                Close_TB()
                time.sleep(10)
