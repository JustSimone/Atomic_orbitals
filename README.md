# Atomic Orbital
This library contains the basic tools to plot the atomic orbitals using spherical harmonics as well as the vibrating function psi of the orbitals of a hydrogenlike atom, given the three integer positive numbers n, l and ml, respectively main quantic number, orbital quantic number and magnetic quantic number.

## How to use the library
After downloading the source you'll need to go in the source folder and run the commaind 
```
python3 orb.py n ml p s
```
where n, ml, p and s are the four aruments defined as follow
- n is the n quantic number (l = n-1);
- ml is the ml quantic number;
- p can be eather a 0, to print only the spherical harmonics, a 1, to print only the probability function, or a 2, to print both (the default value will be 0);
- s can be both a 0, to not save the frame, or a one to save the frame;

sostitute the letters with the numbers and send the command. For example:
```
python3 orb.py 3 0 0 1
```


## Spherical harmonics
The shape of the Spherical harmonics is given by the absolute value of the following complex function:
$$Y_{l, m_l} (\theta, \phi) = (-1)^{m_l} \[ \frac{2l+1}{4\pi}\frac{(l-m_l)!}{(l+m_l)!}\]^{\frac{1}{2}}P^{m_l}_l(\cos\theta)e^{im_l\phi}$$
where $P^{m_l}_l(\cos\theta)$ is the Legendre Polynomial with of l degree and $m_l$ order.

## hydrogenlike atomic orbitals
The shape of this orbital are not constant, in fact they depend on the radius from the center of the atom. In general, the function used to compute the orbitals depends on the form of the potential chosen, and it is solution of the Schrödinger equation in the spherical coordinates system.
$$\frac{\partial^2 \phi}{\partial r^2} + \frac{2}{r} \frac{\partial\phi}{\partial r} + \frac{1}{r^2 \sin^2{\theta}}\left[ \sin{\theta} \frac{\partial}{\partial r} \left ( \sin{\theta}\frac{\partial \phi}{\partial \theta} \right) + \frac{\partial^2 \phi}{\partial \varphi^2} \right] + \frac{2m}{\hbar^2}(2w +U)\phi = 0$$
Given the fact that it is a differential equation of partial derivatives and the agolar part is independent from the radial one it is possible to rewrite the solution as the multiplication of two separate functions
$$\phi (r, \varphi, \theta) = \chi(r)\Upsilon (\varphi, \theta)$$
where $\Upsilon$ is a spherical harmonic and its equation is given in the previous paragraph, while $\chi$ is:
$$\chi_{n,l}(r) = \left [ \frac{2Z}{r_Bn} \frac{(n-l-1)!}{2n(n+l)!} \right ]^{1/2}\left ( \frac{2Zr}{r_Bn} \right )^{l+1} e^{-\frac{-Zr}{r_Bn}} L\left ( \frac{2Zr}{r_Bn} \right )$$
where $L^{2l+1}_{n-l-1} \left ( \frac{2Zr}{r_Bn} \right)$ is Laguerre Polynomial.
## Strcture of the code
The main file is orb.py, in which we fine the function orb() that takes as imput the $n$ and $m_l$ and gives as output both the atomic orbital and the spherical harmonic. In the case of the first, there is a slider which allows to move between different radiuses of the orbital.
To save a picture of the harmonic it is neccessary to change the value of the function print() from 0 to 1, as said in the code's comments.
To make the code more user friendly, for those who just want to get the image of the atomic orbitals you may use terminal arguments shown in the first section.

## Library
To use this class it is necessary to install:
- numpy
- matplotlib
- scipy
