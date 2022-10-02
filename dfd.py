import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
N = 5000 # Number of samplepoints

T = 1.0 / 1000.0 # sample spacing

x = np.linspace(0.0, N*T, N)

y = [7*np.sin(t*4*np.pi)*np.exp(((t-10)**2)/10) for t in x]

plt.plot(x,y)

plt.xlim(-2,2)

plt.title(r'Rectangular function')

plt.savefig('fourrier_transform_rectangular.png', bbox_inches='tight')

plt.close()

yf = scipy.fftpack.fft(y)

yf = np.fft.fftshift(yf)

xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)

fig, ax = plt.subplots()

ax.plot(xf, np.abs(yf) )

plt.xlim(-10,10)
plt.title('FFT (rectangular function) power spectrum')

plt.grid()

plt.savefig('fourrier_transform_rectangular_abs.png', bbox_inches='tight')

plt.close()

fig, ax = plt.subplots()

ax.plot(xf, np.real(yf) )

plt.xlim(-10,10)
plt.title('FFT (rectangular function) real')

plt.grid()

plt.savefig('fourrier_transform_rectangular_real.png', bbox_inches='tight')

plt.close()

fig, ax = plt.subplots()

ax.plot(xf, np.imag(yf) )

plt.xlim(-10,10)
plt.title('FFT (rectangular function) img')

plt.grid()

plt.savefig('fourrier_transform_rectangular_imag.png', bbox_inches='tight')

plt.close()