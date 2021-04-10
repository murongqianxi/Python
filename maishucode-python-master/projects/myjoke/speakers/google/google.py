# 本类是Speaker（发言人)的其中一个实现。所有Speaker都要实现tell_joke接口。
# 其他实现包括：ttsx, xunfei, printer等。

# 谷歌接口库，需要能访问谷歌网络
from gtts import gTTS

# 用来发音
import playsound
import os

def get_joke_audio(joke_id, text):
    # 生成语音文件的名字
    filename = f"{joke_id}.mp3"

    # 生成语音文件的目录：先获取当前文件所在目录，然后放目录下的audios下
    speaker_path = os.path.dirname(__file__)
    full_path = f'{speaker_path}/audios/{filename}'

    # 判断声音文件是否已经生成过，避免重复的网络请求。
    # 如果已经存在了，直接返回文件路径，
    if os.path.exists(full_path):
        print('文件已经生成，直接返回')
        return full_path

    print('声音文件不存在，调用API生成音频文件')
    tts = gTTS(text=text, lang='zh-CN')
    tts.save(full_path)
    return full_path


def tell_joke(joke_id, title, detail):
    text = f'{title}，#{detail}'
    
    # 调用上面的方法生成语音文件
    audio = get_joke_audio(joke_id, text)
    # 调用playsound发音
    playsound.playsound(audio, block=True)

# 测试代码
if __name__ == '__main__':
    tell_joke(9527, '结婚以后', '女：为什么从前你对我百依百顺，可结婚才三天，你就跟我吵了两天的架？男：因为我的忍耐是有限度的。')


