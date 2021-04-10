import os, sys
import playsound
import time
import xunfei_api

def tell_joke(joke_id, title, detail):
    filename = f"{joke_id}.wav"
    speaker_path = os.path.dirname(__file__)
    full_path = f'{speaker_path}/audios/{filename}'

    #判断声音文件是否已经生成过，如果已经存在了，直接返回
    if os.path.exists(full_path):
        print('文件已经生成，直接返回')
        playsound.playsound(full_path, block=True)
    else:
        text = f'{title}, {detail}'
        xunfei_api.generate_audio(joke_id, text)

        #循环判断，等待文件生成
        while(not os.path.exists(full_path)):
            time.sleep(0.1)
        
        playsound.playsound(full_path, block=True)

if __name__ == '__main__':
    tell_joke(9527, '结婚以后', '女：为什么从前你对我百依百顺，可结婚才三天，你就跟我吵了两天的架？男：因为我的忍耐是有限度的。')
