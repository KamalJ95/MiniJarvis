import pyaudio
import wave


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


play_audio("PEP/audio/quite-impressed.wav")


