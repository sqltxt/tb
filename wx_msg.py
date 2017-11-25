import requests
import json
def wx_msg(corp_id, secret,agentid,msg):
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
if __name__ == '__main__':
    wx_msg('wx87780fb826353ecc','jrZvrrQ1Q_zICTbZas651lO7p0jhxLdo3kQ0Pz2fAI_9O_H7YDGUB6qmrqE9dX0y',3,'删繁就简三秋树 立异标新二月花')
