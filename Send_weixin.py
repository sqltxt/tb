import json
import requests

def text(corp_id, secret,agentid,msg):
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
