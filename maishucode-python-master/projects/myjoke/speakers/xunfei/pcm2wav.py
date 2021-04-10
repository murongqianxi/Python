import sys
import wave
import os

def pcm_to_wav(pcmpath, target_filename):
    '''把pcm格式的音频转成wav'''
    with open(pcmpath, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    with wave.open(target_filename, 'wb') as wavfile:
        wavfile.setparams((2, 2, 8000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)

# 测试代码
if __name__ == '__main__':
    folder = os.path.dirname(__file__)
    source = f'{folder}/audios/temp.pcm'
    target = f'{folder}/audios/test.wav'
    pcm_to_wav(source, target)
