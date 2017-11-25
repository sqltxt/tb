import win32con
import win32api
import win32gui
import time
import queue
import requests
import json

corp_id = 'wx87780fb826353ecc'
secret = 'XlOvsTpuNaINPsV2Wm6TMRLt_k1lgxZjJwrSaVND0Lo'
agentid = 1000003

def GetTV_Host():
    TV = win32gui.FindWindow('#32770','TeamViewer')
    #print(hex(TV))
    ID = win32gui.FindWindowEx(TV,0,'Edit',None)
    #print(hex(ID))
    PW = win32gui.FindWindowEx(TV,ID,'Edit',None)
    #print(hex(PW))
    
    ID_buf_size = win32gui.SendMessage(ID, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节  
    #print(buf_size)
    ID_str_buffer = win32gui.PyMakeBuffer(win32gui.SendMessage(ID, win32con.WM_GETTEXTLENGTH, 0, 0) + 1)  # 生成buffer对象
    #print(str_buffer)
    win32api.SendMessage(ID, win32con.WM_GETTEXT, ID_buf_size, ID_str_buffer)  # 获取buffer  
    ID_address, ID_length = win32gui.PyGetBufferAddressAndLen(ID_str_buffer) 
    IDstr = win32gui.PyGetString(ID_address, ID_length) 
    
    PW_buf_size = win32gui.SendMessage(PW, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节  
    #print(buf_size)
    PW_str_buffer = win32gui.PyMakeBuffer(win32gui.SendMessage(PW, win32con.WM_GETTEXTLENGTH, 0, 0) + 1)  # 生成buffer对象
    #print(str_buffer)
    win32api.SendMessage(PW, win32con.WM_GETTEXT, PW_buf_size, PW_str_buffer)  # 获取buffer  
    PW_address, PW_length = win32gui.PyGetBufferAddressAndLen(PW_str_buffer) 
    PWstr = win32gui.PyGetString(PW_address, PW_length) 
    
    return IDstr[:-1]+'\n'+PWstr[:-1]

def wx_msg(corp_id, secret,agentid,msg):
    try:
        values = {'corpid' :corp_id,
              'corpsecret':secret
              }
        req = requests.post('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=values)
        token = json.loads(req.text)["access_token"]
        #try:
        dict_arr = {"touser": "@all",
                    "toparty": "@all",
                    "msgtype": "text",
                    "agentid": agentid,
                    "text": {"content": msg},
                    "safe": "0"}
        data = json.dumps(dict_arr,ensure_ascii=False,indent=2,sort_keys=True).encode('utf-8')
        reqs = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token,data)
    except Exception as e:
        with open('微信发送失败:'+str(int(time.strftime("%H%M%S")))+'.log') as f:
            f.write(e)

       
if __name__=='__main__':
    #GetTV_Host()
    wx_msg(corp_id, secret,agentid,GetTV_Host())
    #while 1:
        #time.sleep(1)
