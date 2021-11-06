#!/usr/bin/env python
# -*- coding:utf-8 -*-

###########语音相关导入##################
from aip import AipSpeech #
import requests
from pydub import AudioSegment  # 第三方 sudo apt install  ffmpeg
#######音频相关############
import pyaudio
import wave

from pydub.playback import play  # 第三方
from playsound import playsound  # 默认音频模块
import os  # apt install mpg123
############视频相关导入###############
from cv2 import cv2
import time
from bypy import ByPy
#############启用多线程##############
import threading


bp = ByPy()


APP_ID = '22970698'
API_KEY = 'LkQsgSWeITSic9bsAFWM3X68'
SECRET_KEY = 'knnf8kAsd8LWq3VGEuKcR6ZntSyQAI5o'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
print(client)


times_2 = time.strftime('%Y_%m_%d_%H_%M_%S',
                        time.localtime(time.time()))

# 定义视频名称

def video_names(name, type):
    names = name+'_'+times_2+"."+type
    return names

# 定义视频时间

def time_update():
    time.sleep(0)
    time_new = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
    return(time_new)

# 定义语音朗读

def voice_sound_txt(file_path, music_path):

    #########需要转换的文字#################
    cut_enter = ""  # 删除文本中的回车符号
    filepath = file_path
    with open(filepath, "r") as f:
        line = f.read().splitlines()
        for in_enter in line:
            cut_enter = cut_enter+in_enter
        print(cut_enter)
        # 中文：zh 粤语：ct 英文：en
        # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
        result = client.synthesis(
            cut_enter, 'zh', 1, {'vol': 5, 'per': 3, 'spd': 5, })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    # 播放音频 os方式，audiosegment 方式，
    musicPath = music_path

    # 方法二 播放声音
    song = AudioSegment.from_mp3(musicPath)
    play(song)


def voice_sound_str(string_value, str_music_path):

    #########需要转换的文字#################
    stringval = string_value
    print(stringval)
    # 中文：zh 粤语：ct 英文：en
    # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    result = client.synthesis(
        stringval, 'zh', 1, {'vol': 5, 'per': 3, 'spd': 5, })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('str_audio.mp3', 'wb') as f:
            f.write(result)
    # 播放音频 os方式，audiosegment 方式，
    musicPath = str_music_path

    ########方法一
    # os.system("mpg123 " + musicPath)   #apt install mpg123

    #########方法三,不可用
    # playsound(musicPath)

    # 方法二 播放声音
    song = AudioSegment.from_mp3(musicPath)
    play(song)

# 定义网络摄像头

def ip_cammer(video_full_path=r"http://admin:admin@192.168.22.46:8081/video", video_formate='FLV1', video_logo='请按 Q 退出程序', video_exit='q', video_name=video_names("cammer", "flv")):
    # video_full_path = "http://admin:admin@192.168.25.87:8081/video"
    video_url = video_full_path

    cap = cv2.VideoCapture(video_url)

    fourcc = cv2.VideoWriter_fourcc(*video_formate)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)

    while True:
        try:
            ret, frame = cap.read()
            out.write(frame)

            cv2.putText(frame, video_logo + ' '+time_update(), (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow('CamerShow', frame)
        except Exception as re:

            break
        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
    cap.release()
    cv2.destroyAllWindows()

# 定义本地摄像头

def local_cammer(video_formate, video_logo, video_exit, video_name):
    cap_local = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*video_formate)

    size = (int(cap_local.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap_local.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(str(video_name), fourcc, 25.0, size)

    while True:
        ret, frame_local = cap_local.read()

        # grey = cv2.cvtColor(frame_local, cv2.COLOR_BGR2GRAY)

        out.write(frame_local)

        cv2.putText(frame_local,
                    video_logo + ' '+time_update(),
                    (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

        cv2.imshow('CamerShow_local', frame_local)

        if cv2.waitKey(1) & 0xFF == ord(video_exit):
            break
            key = cv2.waitKey(10)

    cap_local.release()
    cv2.destroyAllWindows()

#定义语音转换

def change_voice_type(voice_file_path,voice_file_type):
    sound = AudioSegment.from_file(voice_file_path, format = voice_file_type) #要转换成wav的文件位置
    # 将读取的波形数据转化为wav
    f = wave.open("audio_new.wav", 'wb')#新wav文件保存位置
    f.setnchannels(1)   # 频道数
    f.setsampwidth(2)   # 量化位数
    f.setframerate(16000)   # 取样频率
    f.setnframes(len(sound._data))   # 取样点数，波形数据的长度
    f.writeframes(sound._data)   # 写入波形数据
    f.close()

#定义语音识别程序（需要和chage_voice_type一起使用，同时需要调用百度api接口）

def wav_voice_changeto_txt(vocies_file_path):
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    music_path=vocies_file_path       #读取符合百度api识别的wav格式文件。
    # 识别本地文件
    result = client.asr(get_file_content(vocies_file_path), 'wav', 16000, {'dev_pid': 1537, })
    # print(result)
    print(result['result'][0])    

########开始录音函数###############
def start_audio(time=10, save_file="test.wav"):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = time  # 需要录制的时间
    WAVE_OUTPUT_FILENAME = save_file  # 保存的文件名

    p = pyaudio.PyAudio()  # 初始化
    print("ON start voice")

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # 创建录音文件
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)  # 开始录音

    print("OFF end voice")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # 保存
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

########使用多线程，边录音，边录像############
threads = []
threads.append(threading.Thread(target=start_audio))
threads.append(threading.Thread(target=ip_cammer))

    
# 程序调用执行入口

if __name__ == "__main__":        
    # url = 'http://admin:admin@192.168.22.46:8081/video'
    # file_path = "/home/tianbo/pythonapp/l语音合成朗读/a.txt"#要读取的文本文档位置
    # music_path = "audio.mp3"
    # wav_music_path="test.wav"
    # str_music_path = "str_audio.mp3"

    # types = 'FLV1'#视频格式
    # logo = '请按 Q 退出程序'#退出程序快捷键
    # # voice_sound_str(logo, str_music_path)#语音提示（自定义字符串）
    # exit_button = 'q'
    # #voice_sound_txt(file_path, music_path)#语音提示（读取文本）
    # w = video_names("cammer", "flv")

    #change_voice_type(music_path,'mp3')
    #wav_voice_changeto_txt(wav_music_path)
    #ip_cammer()

    for t in threads:
        #print(t)
        t.start()

    # ip_cammer(url, types, logo, exit_button, w)#调用摄像头
    # local_cammer(types, logo, exit_button, w)

    # 百度盘创建文件夹，并进行文件上传。
    # bp.mkdir(remotepath='Python_avi')
    # bp.upload(localpath='/home/tianbo/pythonApp',remotepath='Python_avi',ondup='overwiter')
    # bp.info()

