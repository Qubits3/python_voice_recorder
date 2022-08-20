import datetime

import sounddevice as sd
from numpy import ndarray
from scipy.io.wavfile import write

fs = 48000
seconds = 10
my_recording: ndarray


def record_audio():
    global my_recording
    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write("C:\\Users\\Metin\\Desktop\\" + str(datetime.datetime.now().strftime("%d-%b-%Y (%H.%M.%S)")) + ".wav", fs,
          my_recording)


def stop_recording():
    sd.stop()
