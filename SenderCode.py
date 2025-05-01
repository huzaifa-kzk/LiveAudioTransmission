
import pyaudio 
import socket

#"""Python script for sender(host)"""
CHUNK= 1024
FORMAT= pyaudio.paInt16 
CHANNELS= 1
RATE= 44100

# Audio stream setup
p = pyaudio.PyAudio()
stream= p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#	UDP socket setup
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 

 
IP= "192.168.1.2" # Or whatever you saw in ipconfig
PORT= 5000
print("Sending audio...") 
while True:
    data= stream.read(CHUNK)
    sock.sendto(data, (IP, PORT))



