import win32gui
from win32.lib import win32con
import time
import win32process
import datetime
from commctrl import LVM_GETITEMTEXT,LVM_GETITEMCOUNT
import os
import glob
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
ExpirationDate = '2017-11-11'
username = 'sqltxt'
password = 'iamanothwolf'

def Log(text):
    f = open(mylog,'a')
    f.write(str(status)+'\t'+datetime.datetime.now().strftime('[%H:%M:%S]')+'\t'+text+'\n')
    f.close()
    
def handle_window(hwnd,extra):#TB句柄
    if win32gui.IsWindowVisible(hwnd):
        if extra in win32gui.GetWindowText(hwnd):
            global TB
            TB = hwnd
def Kill():
    global status
    global times
    times = 0 #登录次数清零
    if int(time.strftime("%I%M%S")) == 85000:
        if "TradeBlazer.exe" in os.popen('tasklist /FI "IMAGENAME eq TradeBlazer.exe"').read():
            os.system('TASKKILL /F /IM TradeBlazer.exe')
            os.system('TASKKILL /F /IM TBDataCenter.exe')
            status = 0
            Log('进程清零')
            time.sleep(5)
    
def TBStar_TBLogin(un,pw):
    global status
    global times
    if "TradeBlazer.exe" not in os.popen('tasklist /FI "IMAGENAME eq TradeBlazer.exe"').read():
        #打开TB
        handle = win32process.CreateProcess(path+'TradeBlazer.exe','',None,None,0,win32process.CREATE_NO_WINDOW,None,path,win32process.STARTUPINFO())#打开TB,获得其句柄
        time.sleep(2)
        status = 1 
        Log('打开TB')
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
        win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'ComboBox',None),0,'Edit',None),win32con.WM_SETTEXT,0,un)
        time.sleep(1)
        win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'Edit',None),win32con.WM_SETTEXT,0,pw)
        time.sleep(1)
        win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770',None),0,'Button','登录(&L)'),win32con.BM_CLICK,1,0)
        status = 2
        times = 1
        Log(str(times)+' 次登录')
        #TB句柄
        time.sleep(10)
        win32gui.EnumWindows(handle_window,'交易开拓者')
        time.sleep(25)
        
def TradeStar():
    global status
    if status == 2 or status == 10:
        win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),22),0)#启动所有自动交易
        status = 3
        Log('启动交易')
        time.sleep(2)
    
def MonitorStar():
    global status
    if (status == 3):
        win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),7),11),0)#监控器
        #print (st)
        status = 4
        Log('打开监控')
        time.sleep(10)
    
    
def SaveWorkSpace():
    global status
    win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),9),0)#保存所有工作区
    status = 5
    Log('保存工作区')
    
    time.sleep(2)
def MonitorClose():
    global status
    win32gui.PostMessage(win32gui.FindWindow('#32770','自动交易头寸监控器'),win32con.WM_CLOSE,0,0)
    time.sleep(1)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认 '),0,'Button','是(&Y)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认 '),0,'Button','是(&Y)'),win32con.BM_CLICK,0,0)
    status = 6
    Log('关闭监控')
    time.sleep(2)

def TradeStop():
    global status
    win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),23),0)#停止所有自动交易
    status = 7
    Log('停止交易')
    time.sleep(2)

def TBClose():
    global status
    global times
    #win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),27),0)#退出程序(菜单方式）
    win32gui.PostMessage(TB,win32con.WM_CLOSE,0,0)
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认'),0,'Button','是(&Y)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
    time.sleep(2)
    win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','确认'),0,'Button','是(&Y)'),win32con.BM_CLICK,1,0)
    status = 8
    Log('关闭TB')
   
    times = 0#登录次数清零
    status = 0#状态清零
    
def AccountLogin_LoginFail():
    global status
    global times
    while 1:
        n = win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindowEx(TB,win32gui.FindWindowEx(TB,0,'AfxControlBar110',None),'AfxControlBar110',None),0,None,'帐户管理'),0,'SysListView32',None),LVM_GETITEMCOUNT)
        if n <1:
            status = 11
            Log('柜台关闭')
            win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),7),17),0)#帐户登录
            win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','帐户登录'),0,'Button','登录(&L)'),win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)#激活窗口
            time.sleep(2)
            win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindow('#32770','帐户登录'),0,'Button','登录(&L)'),win32con.BM_CLICK,1,0)
            status = 10
            times = times + 1
            Log(str(times)+' 次登录')
            time.sleep(20)
        else:
            break;
    #win32gui.PostMessage(TB,win32con.WM_COMMAND, win32gui.GetMenuItemID(win32gui.GetSubMenu(win32gui.GetMenu(TB),0),26),0)#锁定程序
def ShutdownR():
    import platform
    import os
    #import system
    global status
    ver = platform.platform()
    if 'Windows-7' in ver:
        os.system('shutdown -r')
        status = 20
        Log('周末重启系统')
        time.sleep(60)
    else:
        status = 20
        Log('非WIN7系统周末不重启')

def Rubber():
    global status
    if username != 'sqltxt' or username != 'gentle':
        for fname in os.listdir(path):
            if 'LOG_' in fname:
                status = 40
                Log('清扫')
                os.remove(path+fname)
    f = open(mylog,'a')
    f.write('\n')
    f.close()
    
def Expired():
    if datetime.datetime.now()>datetime.datetime.strptime(ExpirationDate,"%Y-%m-%d"):
        print(datetime.datetime.now())
        print("过期日"+ExpirationDate)
    elif datetime.datetime.now()<=datetime.datetime.strptime(ExpirationDate,"%Y-%m-%d") and datetime.datetime.strptime(ExpirationDate,"%Y-%m-%d")-datetime.datetime.now()<datetime.timedelta(12):
        print('即将过期')
        
if __name__=='__main__':
    f = open(mylog,'a')
    f.write('\n')
    f.write('\t'+datetime.datetime.now().strftime('[%H:%M:%S]')+'\tAutoRunTB启动'+'\n')
    f.close()
    status = 0
    times = 0
    while 1:
        if datetime.datetime.now().weekday()<=5:
            if (85000<=int(time.strftime("%I%M%S"))<= 115000 and status == 0):
                Kill()
                TBStar_TBLogin(username,password)
                Expired()
                AccountLogin_LoginFail()
                TradeStar()
                MonitorStar()
            if int(time.strftime("%H%M%S") )== 153500 or int(time.strftime("%H%M%S") == 23500) :
                SaveWorkSpace()
                MonitorClose()
                TradeStop()
                TBClose()
                Rubber()
                time.sleep(20)
        elif datetime.datetime.now().weekday()==6 and int(time.strftime("%H%M%S") == 120000) :
            ShutdownR()
        
