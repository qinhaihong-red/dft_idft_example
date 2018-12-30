import numpy as np
import cv2
import cv_helper as ch
import matplotlib.pyplot as plt
%matplotlib inline

img_path=ch.get_img_path('lena')
lena=cv2.imread(img_path,0)
N=lena.shape[0]#here shape[0]==shape[1]
lena_dft=np.fft.fft2(lena)
lena_idft=np.fft.ifft2(lena_dft)

def dft(img,N,h,k):
    F=np.zeros((N,N),dtype=np.complex128)
    w0=2*np.pi/N
    for a in range(N):
        for b in range(N):
            mag=img[a,b]
            theta=-w0*(a*h+b*k)
            F[a,b]=np.complex128(mag*np.cos(theta)+mag*np.sin(theta)*1j)

    return F.sum()

def idft(F,N,a,b):
    I=np.zeros((N,N),dtype=np.complex128)
    w0=2*np.pi/N
    for h in range(N):
        for k in range(N):
            mag=np.abs(F[h,k])
            theta1=np.angle(F[h,k])
            theta2=w0*(a*h+b*k)
            theta=theta1+theta2
            I[h,k]=np.complex128(mag*np.cos(theta)+mag*np.sin(theta)*1j)

    return I.sum()/(N*N)

#test it
print('dft:\n',lena_dft[55,128],'\n',dft(lena,N,55,128))
print('idft:\n',lena_idft[200,255],'\n',idft(lena_dft,N,200,255))