# Atomic Orbital
This library contains the basic tools to plot the atomic orbitals using spherical harmonics, giving as input the magnetic quantum number ml and the orbital quantum number l.

## Spherical harmonics
The shape of the Spherical harmonics is given by the following function:
$$Y_{l, m_l} (\theta, \phi) = (-1)^{m_l} \[ \farc{2l+1}{4\pi}\frac{(l-m_l)!}{(l+m_l)!}\]^{\farc{1}{2}}P^{m_l}_l(\cos\theta)e^{im_l\phi}$$
where $P^{m_l}_l(\cos\theta)$ is the Legendre Polynomial with of l degree and $m_l$ order.
