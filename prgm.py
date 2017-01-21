# -*- coding: utf-8 -*-
# importation des librairies
from numpy import linspace, mean
from scipy.io.wavfile import read
import numpy as np
from scipy.fftpack import fft, fftfreq 
from scipy.signal import freqz
from random import randrange as rd
import matplotlib.pyplot as plt

def FFT(nomson):
    nomfile = open(nomson,'r')
    rate,signal = read(nomfile)
    dt = 1./rate
    FFT_size = 2**18
    NbEch = signal.shape[0]
    t = linspace(0,(NbEch-1)*dt,NbEch)
    t = t[0:FFT_size]
    signal = signal[0:FFT_size, 0]
    signal = signal - mean(signal)
    signal_FFT = abs(fft(signal))
    signal_freq = fftfreq(signal.size, dt)
    signal_FFT = signal_FFT[0:len(signal_FFT)//2]
    signal_freq = signal_freq[0:len(signal_freq)//2]
    a = signal_FFT.tolist()
    b = signal_freq.tolist()
    liste=[]
    for i in range(0,20):
        liste.append(b[a.index(max(a))])
        for i in range(0, 29):
            a.remove(max(a))
    d = liste
    d = map(int, d)
    e = max(d) - min(d)
    nomson = []
    if e > 500:
        for i in range(0,5):
            nomson.append(min(d))
            c = min(d)
            c += 100
            while min(d) < c:
                d.remove(min(d))
    else:
        for i in range(0,5):
            nomson.append(min(d))
            c = min(d)
            c += 20
            while min(d) < c:
                d.remove(min(d))
    return nomson

nomson = "Son1.wav"
liste1 = FFT(nomson)
print(liste1)
nomson = "Son2.wav"
liste2 = FFT(nomson)
print(liste2)
nomson = "Son3.wav"
liste3 = FFT(nomson)
print(liste3)
nomson = "Son4.wav"
liste4 = FFT(nomson)
print(liste4)
liste = []
liste.extend(liste1)
liste.extend(liste2)
liste.extend(liste3)
liste.extend(liste4)



