from gtts import gTTS
import playsound
import os


def get_joke_audio(id, text):
    filename = f"{id}.mp3"
    path = os.path.dirname(__file__)
    print(path)
    full_path = f'{path}/audios/{filename}'
    tts = gTTS(text=text, lang='zh-CN')
    tts.save(full_path)
    return full_path

def tell_joke(id, title, detail):
    text = f'{title}，#{detail}'
    #audio = get_joke_audio(id, text)
    playsound.playsound('/Users/zjueman/git/python/Python进阶/myjoke/speakers/google/audios/9527.mp3', block=True)

if __name__ == '__main__':
    tell_joke(9527, '测试笑话', '测试笑话内容123')


