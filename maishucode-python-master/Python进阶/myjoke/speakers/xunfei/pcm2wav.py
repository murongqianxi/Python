import sys
import wave


def pcm_to_wav(pcmpath, filename):
    with open(pcmpath, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    with wave.open(filename+'.wav', 'wb') as wavfile:
        wavfile.setparams((2, 2, 9000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)

if __name__ == '__main__':
    pcm_to_wav('speakers/xunfei/demo.pcm', 'demo')
