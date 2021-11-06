# coding=utf-8
from aip import AipSpeech
import requests

from pydub import AudioSegment#第三方 sudo apt install  ffmpeg 
import wave

from pydub.playback import play#第三方
from playsound import playsound  # 默认音频模块 
import os  #apt install mpg123

APP_ID = '22970698'
API_KEY = 'LkQsgSWeITSic9bsAFWM3X68'
SECRET_KEY = 'knnf8kAsd8LWq3VGEuKcR6ZntSyQAI5o'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print(client)

##############音频转换函数       
# def trans_mp3_to_wav(filepath):
#     song = AudioSegment.from_mp3(filepath)
#     song.export("/home/tianbo/audio.wav", format="wav")

# musicPath = r"/home/tianbo/audio.mp3" 
# trans_mp3_to_wav(musicPath)  

########金山词霸api接入########
# def get_msg():
#     url = 'http://open.iciba.com/dsapi/'   # 金山词霸每日一句 api 链接
#     html = requests.get(url)
#     content = html.json()['content']   # 获取每日一句英文语句
#     note = html.json()['note']   # 获取每日一句英文的翻译语句
#     return content, note

#########需要转换的文字#################
#content, note = get_msg() 
# f=open("/home/tianbo/pythonApp/a.txt",'r')
# data=f.read().splitlines()
cut_enter=""#删除文本中的回车符号
filepath="/home/tianbo/pythonapp/l语音合成朗读/a.txt"
with open(filepath,"r") as f:
    line=f.read().splitlines()    
    for in_enter in line:
        cut_enter=cut_enter+in_enter
    print(cut_enter)
    # 中文：zh 粤语：ct 英文：en
    #发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    result = client.synthesis(cut_enter, 'zh', 1, {'vol': 5, 'per': 4, 'spd': 5, })


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)

##播放音频 os方式，audiosegment 方式，
musicPath = r"/home/tianbo/pythonapp/l语音合成朗读/audio.mp3" 

########方法一
# os.system("mpg123 " + musicPath)   #apt install mpg123

########方法二
song = AudioSegment.from_mp3(musicPath)
play(song)

#########方法三,不可用
# playsound(musicPath)

