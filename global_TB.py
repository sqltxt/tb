import time

username ='sqltxt'
password = 'iamanothwolf'
corp_id = 'wx87780fb826353ecc'
secret = 'WVClMaoadG7yP6sbsEox5HCwuHFG1SjrDqIjMVVfQmc'
agentid = 1000002

'''
username ='Gentle'
password = 'iamanoth1977OK'
corp_id = 'wx87780fb826353ecc'
secret = 'zOTGHqMW_R01vX9ij2MKTNdg49x0f-UDT3h_CwYxcVo'
agentid = 1000004
'''

week_day = {
        1: '周一',
        2: '周二',
        3: '周三',
        4: '周四',
        5: '周五',
        6: '周六',
        0: '周日',
    }

path =  'C:/Users/Administrator/Documents/tbv5321_x64_portable/'
fbk = username+'_'+str(int(time.strftime("%Y%m%d")))+'.fbk'
mylog  = path+'LOG_'+time.strftime('%Y%m%d')+'_'+week_day[int(time.strftime("%w"))]+'.txt'
ExpirationDate = 20991220
TB_handle= 0
Accounts = 0
Monitor_handle = 0
Rubber_times = 0
Expired_times = 0
Trade = 0
status = 0
times =0
kill = 1 #默认已经杀过进程
def handle_window(hwnd,extra):#global_TB.TB_handle句柄
    if win32gui.IsWindowVisible(hwnd):
        if extra in win32gui.GetWindowText(hwnd):
            #global global_TB.TB_handle
            global_TB.TB_handle= hwnd
