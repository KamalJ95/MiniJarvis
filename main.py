import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander


running = True


def say(text):
    subprocess.call('say ' + text, shell=True)


"""Play MP3"""
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    """Stream to stream the audio"""
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    """Creating a data stream variable equal to the initial chunk"""
    data_stream = wf.readframes(chunk)

    """Read it and whilst there is some left, keep reading."""
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    """Close and terminate stream"""
    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


def initSpeech():
    print("Listening...")
    play_audio("PEP/audio/unconvinced.wav")

    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)

    play_audio("PEP/audio/quite-impressed(1).wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Sorry I couldn't catch that.")

    print("You said:")
    print(command)
    if command == "quit":
        global running
        running = False

    cmd.discover(command)


while running:
    initSpeech()









