import pyaudio
 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
auth_key = "24899fb6434e4111a7aed2f4698fdce6"
# starts recording
stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   #auth_key = "24899fb6434e4111a7aed2f4698fdce6"
   frames_per_buffer=FRAMES_PER_BUFFER
)