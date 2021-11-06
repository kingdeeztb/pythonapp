from aip import AipFace
import base64
import json


""" 你的 APPID AK SK """
APP_ID = '20627081'
API_KEY = 'NYTI5D4FOBRiTL8UIzVeqQRY'
SECRET_KEY = 'dAoogXPAG4voKgk9O5WFkKqdKtb3u6gU'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

f = open("C:\\Users\\w_zhangtb\\Desktop\\timg_2.jpg", "rb")  # 转为二进制格式
image = base64.b64encode(f.read())  # 使用base64进行加密
image64 = str(image, 'utf-8')

imageType = "BASE64"
userId = "tao_liu"
groupId = "no_clothes"

options = {}
options["face_field"] = "age,beauty,expression,face_shape,gender,glasses,landmark72,race,quality,eye_status,emotion,face_type"
options["max_face_num"] = 2
options["face_type"] = "LIVE"
options["liveness_control"] = "LOW"

""" 调用用户信息查询 """
baidu_result_userinfo = client.getUser(userId, groupId)
groupIdList = "tao_liu,taotao"
""" 调用人脸搜索 M:N 识别 """
baidu_result_shibie = client.multiSearch(image64, imageType, groupIdList)
'''图片基金本信息'''
baidu_result_baseinfo = client.detect(image64, imageType, options)

# print(baidu_result_shibie)
""" 调用人脸搜索 M:N 识别 """
print(baidu_result_shibie["result"]["face_list"]
      [0]['user_list'][0]['group_id'])
print(baidu_result_shibie["result"]["face_list"][0]['user_list'][0]['user_id'])

'''图片基金本信息'''
print("年龄为", baidu_result_baseinfo["result"]["face_list"][0]['age'], '岁')
print("性别为", baidu_result_baseinfo["result"]["face_list"][0]['gender']['type'])
print("人种为", baidu_result_baseinfo["result"]["face_list"][0]['race']['type'])
print("颜值评分为", baidu_result_baseinfo["result"]
      ["face_list"][0]['beauty'], '分/100分')
print("是否带眼镜", baidu_result_baseinfo["result"]
      ["face_list"][0]['glasses']['type'])


groupIdList = "tao_liu,taotao"

""" 调用人脸搜索 """
""" 如果有可选参数 """
options = {}
options["max_face_num"] = 3
options["match_threshold"] = 70
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
options["user_id"] = "liutao"
options["max_user_num"] = 3

""" 带参数调用人脸搜索 """
baidu_result_search = client.search(image64, imageType, groupIdList, options)

if baidu_result_search["result"] == None:
    print("没有找到匹配项")
else:
    print("相似度为:", baidu_result_search["result"]
          ["user_list"][0]['score'], '分/100分')
