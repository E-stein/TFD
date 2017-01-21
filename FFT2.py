
# importation des librairies
from numpy import linspace, mean
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np
from math import exp
from scipy.signal import butter, lfilter
from scipy.signal import freqz
from random import randrange as rd
import serial



def butter_bandpass(lowcut, highcut, fs, order=9):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=9):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# nom du fichier a etudier
nomfile = open('727.wav','r')

# lecture du fichier son 8 Khz mono
rate,signal = read(nomfile)

# définition du vecteur temps
dt = 1./rate
FFT_size = 2**18
NbEch = signal.shape[0]

t = linspace(0,(NbEch-1)*dt,NbEch)
t = t[0:FFT_size]

print(rate)
# calcul de la TFD par l'algo de FFT

 # soustraction de la valeur moyenne du signal
signal = signal[0:FFT_size, 0]
signal = signal - mean(signal)# la fréquence nulle ne nous intéresse pas
signal_FFT = abs(fft(signal))  # on ne récupère que les composantes réelles


# récupération du domaine fréquentiel en passant la période d'échantillonnage
signal_freq = fftfreq(signal.size, dt)

# extraction des valeurs réelles de la FFT et du domaine fréquentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

seuil = 2.5e7
freq = range(10)
magnitude = []
for i in range(10): magnitude.append(rd(0,10))

fft = list(zip(freq,magnitude))
fft_filtre = []
for elem in fft:
    if elem[1] >= seuil:    #si la magnitude dépasse le seuil
        fft_filtre.append(elem)
    else:
        fft_filtre.append((elem[0], 0))

print(fft)
print(fft_filtre)

fs = 44100
lowcut = 500.0
highcut = 1250.0


plt.figure(1)

#affichage du signal
plt.subplot(211)
plt.title('Signal reel et son spectre')
plt.plot(t,signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')
plt.clf()
for order in [3, 6, 9]:
    b, a = butter_bandpass(lowcut, highcut, fs, order=9)
    w, h = freqz(b, a, worN=2000)
    plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = 9")
plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(True)
plt.legend(loc='best')


#affichage du spectre du signal
plt.subplot(212)
Fmax = 10000
plt.xlim(0,Fmax)
plt.plot(signal_freq,signal_FFT)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')



plt.show()

ser=serial.Serial('/dev/ttyACM0',9600)
ser.write('012')
print('OK')
