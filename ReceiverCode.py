#"""Python script for receiver(client)"""
import pyaudio 
import socket

CHUNK= 1024
FORMAT= pyaudio.paInt16 
CHANNELS= 1
RATE= 44100

p = pyaudio.PyAudio()
 
stream= p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(("0.0.0.0", 5000))
print("Receiving audio...")
while True:
    data, addr = sock.recvfrom(CHUNK*2)
    stream.write(data)
