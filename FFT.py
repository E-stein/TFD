
# importation des librairies
from numpy import linspace, mean
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np


# nom du fichier a etudier
nomfile = open('727.wav','r')

# lecture du fichier son 8kHz mono
rate,signal = read(nomfile)


# definition du vecteur temps
dt = 1./rate
FFT_size = 2**18
NbEch = signal.shape[0]

t = linspace(0,(NbEch-1)*dt,NbEch)
t = t[0:FFT_size]


# calcul de la TFD par l'algo de FFT

signal = signal[0:FFT_size, 0]# soustraction de la valeur moyenne du signal
signal = signal - mean(signal) # on supprime la frequence nulle
signal_FFT = abs(fft(signal))  # on ne recupere que les composantes reelles



# recuperation du domaine frequentiel en passant la periode d'echantillonnage(44100 Hz)
signal_freq = fftfreq(signal.size, dt)

# extraction des valeurs reelles de la FFT et du domaine frequentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]


a = signal_FFT.tolist()
b = signal_freq.tolist()
liste=[]
for i in range(0,20):
    liste.append(b[a.index(max(a))])
    for i in range(0, 29):
        a.remove(max(a))

print(liste)
d = liste
d = map(int, d)
e = max(d) - min(d)
print(e)
liste1 = []

if e > 500:
    for i in range(0,5):
        liste1.append(min(d))
        c = min(d)
        c += 100
        while min(d) < c:
            print("oui")
            d.remove(min(d))
            print(d)
    print(min(d))
    print(c)
else:
    for i in range(0,5):
        liste1.append(min(d))
        c = min(d)
        c += 20
        while min(d) < c:
            print("ouii")
            d.remove(min(d))
            print(d)
    print(min(d))
    print(c)



print(liste1)

plt.figure(1)

#affichage du signal
plt.subplot(211)
plt.title('Signal reel et son spectre')
plt.plot(t,signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')


#affichage du spectre du signal
plt.subplot(212)
Fmax = 10000
plt.xlim(0,Fmax)
plt.plot(signal_freq,signal_FFT)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')

plt.show()
