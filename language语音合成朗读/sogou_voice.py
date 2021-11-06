import requests
import json
from playsound import playsound  # 音频模块
appid = '1kDJCy56OrvyvPPjHF5MlkSMoTt'
token = 'X9D7gZjYEH60UB1aFCmsuLAKI0KlTf8Fsi9vzq7p2cH/68sGdxV03zbUjtxpzTL/gpQYHqJyjuoLBi4dXt4VUg=='

text = '你好,请问你叫什么名字'

data = {
    'input': {
      'text': text,
    }, 
    'config': {
      'audio_config': {
          'audio_encoding':'MP3',
          'pitch':0.8,
          'volume':1.3,
          'speaking_rate':1.3
      },
      'voice_config':{
          'language_code':"zh-cmn-Hans-CN",
          'speaker':'female'
      }
    }
}

headers = {
   'Content-Type': 'application/json',
   'Appid': appid,
   'Authorization': 'Bearer ' + token
}

r = requests.post('https://api.zhiyin.sogou.com/apis/tts/v1/synthesize', data=json.dumps(data), headers=headers)

# save to file
file = open("tts.mp3", "bw")
file.write(r.content)
file.close()

print("save finish")
playsound('/home/tianbo/tts.mp3')