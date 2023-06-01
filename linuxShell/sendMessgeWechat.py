# !/usr/bin/env python
# coding=utf-8
import requests
import json

def send_message(_message):
    useridstr = '08e14eb9eaa319cf357c558d57b0e669'#'202305310001'
    agentid = '1000002'
    corpid = 'ww40dc069e5465cd86'
    corpsecret = 'koz5hWpcL7JtdtpLhxA2yFjEQ7CqUgBESYrcPJgbwS8'
    response = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    data = json.loads(response.text)
    # print(response.text)
    access_token = data['access_token']
    # print('access_token是：'+access_token)

    json_dict = {
       "touser" : useridstr,
       "msgtype" : "text",
       "agentid" : agentid,
       "text" : {
           "content" : _message
       },
       "safe": 0,
       "enable_id_trans": 0,
       "enable_duplicate_check": 0,
    #    "duplicate_check_interval": 1800
    }
    json_str = json.dumps(json_dict)
    print(json_str)
    response_send = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}", data=json_str)
    print(response_send.text)
    return json.loads(response_send.text)['errmsg'] == 'ok'

# for _ in range(5):
if __name__ == '__main__':
    send_message("中概互联涨停啦")


#!/root/.virtualenvs/wechat/bin/python

# usage: send message via wechat


# import requests
# import sys
# import json
# import urllib3
# urllib3.disable_warnings()
# ### 填写参数###
# # Corpid是企业号的标识
# Corpid = "ww40dc069e5465cd86"
# # Secret是管理组凭证密钥
# Secret = "koz5hWpcL7JtdtpLhxA2yFjEQ7CqUgBESYrcPJgbwS8"
# # 应用ID
# Agentid = "1000002"
# # token_config文件放置路径
# Token_config = r'/tmp/zabbix_wechat_config.json'
# ### 下面的代码都不需要动###
# def GetTokenFromServer(Corpid, Secret):
#     """获取access_token"""
#     Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
#     Data = {
#         "corpid": Corpid,
#         "corpsecret": Secret
#     }
#     r = requests.get(url=Url, params=Data, verify=False)
#     print(r.json())
#     if r.json()['errcode'] != 0:
#         return False
#     else:
#         Token = r.json()['access_token']
#         file = open(Token_config, 'w')
#         file.write(r.text)
#         file.close()
#         return Token
# def SendMessage(Partyid, Subject, Content):
#     """发送消息"""
#     # 获取token信息
#     try:
#         file = open(Token_config, 'r')
#         Token = json.load(file)['access_token']
#         file.close()
#     except:
#         Token = GetTokenFromServer(Corpid, Secret)
#     # 发送消息
#     Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
#     Data = {
#         "toparty": Partyid,
#         "msgtype": "text",
#         "agentid": Agentid,
#         "text": {"content": Subject + '\n' + Content},
#         "safe": "0"
#     }
#     r = requests.post(url=Url, data=json.dumps(Data), verify=False)
#     # 如果发送失败，将重试三次
#     n = 1
#     while r.json()['errcode'] != 0 and n < 4:
#         n = n + 1
#         Token = GetTokenFromServer(Corpid, Secret)
#         if Token:
#             Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
#             r = requests.post(url=Url, data=json.dumps(Data), verify=False)
#             print(r.json())
#     return r.json()

# if __name__ == '__main__':
#     # 部门id
#     Partyid = '1'
#     # 消息标题
#     Subject = '自应用程序代码测试'
#     # 消息内容
#     Content = 'str(sys.argv[3])'
#     Status = SendMessage(Partyid, Subject, Content)
#     print(Status)
