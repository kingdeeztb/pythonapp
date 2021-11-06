
import pyttsx3
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

engine = pyttsx3.init()
#语速
rate=engine.getProperty('rate')
print(f'语音速率：{rate}')
engine.setProperty('rate', 180)

#音量
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
#音色
engine.setProperty('voice', 'zh')

f=open("/home/tianbo/pythonApp/a.txt",'r')
line = f.readline()
engine.say(line)

engine.runAndWait()


#######################################################






# def use_pyttsx3():
#     # 创建对象
#     engine = pyttsx3.init()
#     # 获取当前语音速率
#     rate = engine.getProperty('rate')
#     print(f'语音速率：{rate}')
#     # 设置新的语音速率
#     engine.setProperty('rate', 200)
#     # 获取当前语音音量
#     volume = engine.getProperty('volume')
#     print(f'语音音量：{volume}')
#     # 设置新的语音音量，音量最小为 0，最大为 1
#     engine.setProperty('volume', 1.0)
#     # 获取当前语音声音的详细信息
#     voices = engine.getProperty('voices')
#     print(f'语音声音详细信息：{voices}')
#     # 设置当前语音声音为女性，当前声音不能读中文
#     engine.setProperty('voice', voices[1].id)
#     # 设置当前语音声音为男性，当前声音可以读中文
#     engine.setProperty('voice', voices[0].id)
#     # 获取当前语音声音
#     voice = engine.getProperty('voice')
#     print(f'语音声音：{voice}')
#     # 语音文本
#     path = 'test.txt'
#     with open(path, encoding='utf-8') as f_name:
#         words = str(f_name.readlines()).replace(r'\n', '')
#     # 将语音文本说出来
#     engine.say(words)
#     engine.runAndWait()
#     engine.stop()


# if __name__ == '__main__':
#     use_pyttsx3()


#######################################################



# # 语音播报模块
# import pyttsx3 

# # aiff文件转换成mp3编码文件模块
# from pydub import AudioSegment

# # 模块初始化
# engine = pyttsx3.init() 

# # 语音播报内容
# content = "人生苦短，我用Python"

# # 输出文件格式
# outFile = 'out.aiff' 

# print('准备开始语音播报...')

# # 设置要播报的Unicode字符串
# engine.say() 

# # 等待语音播报完毕 
# engine.runAndWait()

# # 将文字输出为 aiff 格式的文件
# engine.save_to_file(content, outFile)

# # 将文件转换为mp3格式
# AudioSegment.from_file(outFile).export("Python.mp3", format="mp3")

###########################################################

# import pyttsx3
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# engine = pyttsx3.init()
# engine.setProperty('voice', 'zh')
# f = open(r"/home/tianbo/pythonApp/a.txt", 'r')
# line = f.readline()
# while line:
#  line = f.readline()
#  engine.say(line)
# engine.runAndWait()
# f.close()