 ###########语音相关导入##################
from aip import AipSpeech #
import requests
from pydub import AudioSegment  # 第三方 sudo apt install  ffmpeg
from pydub.playback import play  # 第三方
from playsound import playsound  # 默认音频模块
import os  # apt install mpg123

APP_ID = '22970698'
API_KEY = 'LkQsgSWeITSic9bsAFWM3X68'
SECRET_KEY = 'knnf8kAsd8LWq3VGEuKcR6ZntSyQAI5o'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
print(client)

#########需要转换的文字#################
stringval="百度，你好！百度，你好！百度，你好！ "
print(stringval)
# 中文：zh 粤语：ct 英文：en
# 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
result = client.synthesis(
    stringval, 'zh', 1, {'vol': 5, 'per': 4, 'spd': 5, })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('str_audio.wav', 'wb') as f:
        f.write(result)
# 播放音频 os方式，audiosegment 方式，
musicPath = r"/home/tianbo/pythonapp/调用外设(摄像头等)/baidutest.wav"

# 方法二 播放声音
# song = AudioSegment.from_mp3(musicPath)
# play(song)

# 读取文件

# 1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
# 1737	英语		无标点	不支持自定义词库
# 1637	粤语		有标点	不支持自定义词库
# 1837	四川话		有标点	不支持自定义词库
# 1936	普通话远场	远场模型	有标点	不支持

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
result = client.asr(get_file_content(musicPath), 'wav', 16000, {'dev_pid': 1537, })
print(result)
print(result['result'][0])      