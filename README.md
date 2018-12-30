# Example of Computing DFT&iDFT On Image

 An example just shows how to compute dft&idft on images to better understand the Discrete Fourier Transform . Without taking any efficiency consideration, to keep it simple and clear.
 
Then compare the results with np.fft.fft2.

## Formula:
### DFT: $F(h,k)=\sum_{a=0}^{N-1} \sum_{b=0}^{N-1} f(a,b)e^{\frac{-j2\pi}{N}(ah+bk)}$

### iDFT：$f(a,b)=\frac{1}{N^2}\sum_{h=0}^{N-1} \sum_{k=0}^{N-1} F(h,k)e^{\frac{j2\pi}{N}(ah+bk)}$

## DFT Steps:
- consider f(a,b) as complex number(though it is a real pixel value of 2D image) and compute its magnitude as:$\|f(a,b)\|=np.abs(f(a,b))$, which means for a complex number C:   $magnitude(C)=sqrt\{(C.real)^2+(C.imag)^2\}$


- compute phase as $\theta = -(\frac{2\pi}{N}(ah+bk))$


- store the temp complex value as:$F(h,k)_{a,b} = \|f(a,b)\|cos\theta+j\|f(a,b)\|sin\theta$


- sum the temp to get final:$F(h,k) = \sum_{a=0}^{N-1} \sum_{b=0}^{N-1} F(h,k)_{a,b}$

## iDFT Steps:
almost like DFT Steps.