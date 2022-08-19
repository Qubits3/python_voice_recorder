import pyaudio
import wave
import datetime

now = datetime.datetime.now()

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=2, rate=48000, input=True, frames_per_buffer=1024)
frames = []


def record_audio():
    try:
        while True:
            data = stream.read(num_frames=1024, exception_on_overflow=False)
            frames.append(data)
    except IOError:
        pass


def stop_recording():
    if frames.__sizeof__() > 0 and stream.is_active():
        stream.stop_stream()
        stream.close()
        audio.terminate()

        sound_file = wave.open("C:\\Users\\Metin\\Desktop\\" + str(now.strftime("%d-%b-%Y (%H.%M.%S)")) + ".wav", "wb")
        sound_file.setnchannels(2)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(48000)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
