
import time
import datetime
week_day = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
path =  'C:/Users/Administrator/Documents/tbv5321_x64_portable/'
mylog  = path+'LOG_'+time.strftime('%Y%m%d')+'_'+week_day[datetime.datetime.now().weekday()]+'.txt'
ExpirationDate = '2017-11-11'
username = 'sqltxt'
password = 'iamanothwolf'
TB_handle= 0#
Accounts = 0#win32gui.SendMessage(win32gui.FindWindowEx(win32gui.FindWindowEx(win32gui.FindWindowEx(TB_handle,win32gui.FindWindowEx(TB_handle,0,'AfxControlBar110',None),'AfxControlBar110',None),0,None,'帐户管理'),0,'SysListView32',None),LVM_GETITEMCOUNT)
Monitor_handle = 0#win32gui.FindWindow('#32770','自动交易头寸监控器')
Rubber_times = 0
Expired_times = 0
Trade = 0
status = 0
times =0
corp_id = 'wx87780fb826353ecc'
secret = 'WVClMaoadG7yP6sbsEox5HCwuHFG1SjrDqIjMVVfQmc'
agentid = 1000002
#'wx87780fb826353ecc','WVClMaoadG7yP6sbsEox5HCwuHFG1SjrDqIjMVVfQmc',1000002,
#global_TB.corp_id,global_TB.secret,global_TB.agentid,
def handle_window(hwnd,extra):#global_TB.TB_handle句柄
    if win32gui.IsWindowVisible(hwnd):
        if extra in win32gui.GetWindowText(hwnd):
            #global global_TB.TB_handle
            global_TB.TB_handle= hwnd
