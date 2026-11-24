---
title: "Part I — Chapter 5: Quantum Mechanics in One Dimension"
---

<div class="lang-switch"><a class="on">English</a><a href="../qm1d-ko/">한국어</a></div>

<div class="running-head"><span>Modern Physics</span><span>Part I · Chapter 5</span></div>

# Chapter 5 — Quantum Mechanics in One Dimension { .part-title }

<p class="source-note">Chapter 5 worksheets (midterm range, textbook §5.1–5.11) · <a class="pdf-link" href="notes.pdf" download="Modern-Physics-Chapter-5.pdf">This chapter as PDF</a></p>

**In this chapter.** The wavefunction $\Psi(x,t)$ and its statistical meaning; the Schrödinger equation, read as the rule that turns momentum and energy into operators; separation of variables and the time-independent equation; and the standard one-dimensional problems: the infinite well, the finite well, tunnelling, and the harmonic oscillator solved with ladder operators. Chapter 6 (the hydrogen atom) builds directly on this.

!!! quote "Conventions used in this chapter."
    - $\hbar = h/2\pi$; $m$ is the particle's mass; $U(x)$ (or $V(x)$) is the potential energy.
    - $\Psi(x,t)$ is a full wavefunction; $\psi(x)$ its spatial part; $\phi(t)$ its time part.
    - $\langle Q\rangle = \int \Psi^* \hat Q\,\Psi\,dx$; $\sigma_Q^2 = \langle Q^2\rangle - \langle Q\rangle^2$.
    - Infinite-well eigenfunctions are $\psi_n = \sqrt{2/L}\,\sin(n\pi x/L)$ on $0 < x < L$.

---

## 5.0 Mathematical Tools

### Taylor series and Euler's formula

A smooth function can be expanded about $0$ as $f(x) = a_0 + a_1x + a_2x^2 + \cdots$ with $a_n = f^{(n)}(0)/n!$. In particular

$$
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots, \qquad
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots .
$$

!!! abstract "Theorem 5.0.1 (Euler's formula)"
    $$
    e^{ix} = \cos x + i\sin x .
    $$

!!! success "Proof"
    Expanding $e^{ix} = \sum (ix)^n/n!$ gives $a_0 = 1$, $a_1 = i$, $a_2 = -\frac{1}{2!}$, $a_3 = -\frac{i}{3!}, \dots$ The real terms are the series of $\cos x$ and the imaginary terms $i$ times the series of $\sin x$. $\square$

Other tools used throughout: the total differential (e.g. $PV = nRT \Rightarrow P\,dV + V\,dP = nR\,dT$), substitution (e.g. $\int_0^{\sqrt\pi} x\sin(x^2)\,dx = \tfrac12\int_0^\pi \sin u\,du = 1$ with $u = x^2$), integration by parts $\int uv'\,dx = uv - \int u'v\,dx$, and polar/spherical coordinates, $dx\,dy = r\,dr\,d\theta$ and $dx\,dy\,dz = r^2\sin\theta\,dr\,d\theta\,d\phi$.

### The Gamma function

!!! abstract "Lemma 5.0.2"
    $\displaystyle \lim_{x\to\infty} x e^{-ax} = 0$ for $a > 0$.

!!! success "Proof"
    $e^{ax} = 1 + ax + \frac{(ax)^2}{2} + \cdots > \frac{a^2x^2}{2}$, so $0 < \dfrac{x}{e^{ax}} < \dfrac{2}{a^2x} \to 0$. $\square$

Integrating by parts repeatedly, with the boundary terms vanishing by Lemma 5.0.2,

$$
\int_0^\infty e^{-x}dx = 1, \quad \int_0^\infty xe^{-x}dx = 1, \quad \int_0^\infty x^2e^{-x}dx = 2, \quad \int_0^\infty x^3e^{-x}dx = 6 .
$$

!!! note "Definition 5.0.3 (Gamma function)"
    $$
    \Gamma(p) = \int_0^\infty x^{p-1}e^{-x}\,dx \quad (p > 0), \qquad \Gamma(p) = (p-1)! \text{ for integer } p .
    $$

!!! abstract "Proposition 5.0.4"
    $\Gamma(p+1) = p\,\Gamma(p)$, and $\Gamma(\tfrac12) = \sqrt\pi$.

!!! success "Proof"
    By parts, $\Gamma(p+1) = \big[-x^pe^{-x}\big]_0^\infty + p\int_0^\infty x^{p-1}e^{-x}dx = p\Gamma(p)$.

    With $x = u^2$, $\Gamma(\tfrac12) = \int_0^\infty x^{-1/2}e^{-x}dx = 2\int_0^\infty e^{-u^2}du$. Squaring and passing to polar coordinates over the first quadrant,

    $$
    \Gamma(\tfrac12)^2 = 4\int_0^\infty\!\!\int_0^\infty e^{-(x^2+y^2)}dx\,dy = 4\int_0^{\pi/2}\!\!\int_0^\infty e^{-r^2}r\,dr\,d\theta = 4\cdot\frac{\pi}{2}\cdot\frac12 = \pi . \qquad\square
    $$

!!! info "Remark — the square and the disc"
    The step from $\int_0^\infty\!\int_0^\infty dx\,dy$ to $\int_0^{\pi/2}\!\int_0^\infty r\,dr\,d\theta$ replaces an infinitely large square by an infinitely large quarter-disc. For an integrand that decays this fast the two limits agree.

---

## 5.1 The Wavefunction and the Schrödinger Equation

### Waves and complex wavefunctions

A wave travelling along $x$ with speed $v$ can be written $y = A\sin(kx-\omega t)$, or more generally $A\cos(kx-\omega t) + iA\sin(kx-\omega t) = Ae^{i(kx-\omega t)}$, and $Ae^{i(kx-\omega t)} + Be^{-i(kx+\omega t)}$ allows both directions. All of these satisfy the classical wave equation $\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{v^2}\dfrac{\partial^2 y}{\partial t^2}$.

Classically only the real part is physical. In quantum mechanics $\Psi(x,t)$ is in general complex and is not itself measurable; what is meaningful is $|\Psi|^2 = \Psi^*\Psi$, the probability density.

With de Broglie's $p = h/\lambda = \hbar k$ and Planck's $E = hf = \hbar\omega$, the wave $\Psi = Ae^{i(px - Et)/\hbar}$ describes a free particle ($U = 0$) of energy $E$ and momentum $p$.

### Deriving the equation

$$
\frac{\partial^2\Psi}{\partial x^2} = -k^2\Psi = -\frac{p^2}{\hbar^2}\Psi, \qquad
\frac{\partial\Psi}{\partial t} = -i\omega\Psi = -\frac{iE}{\hbar}\Psi .
$$

So, acting on $\Psi$, momentum and energy behave as operators:

$$
\hat p = \frac{\hbar}{i}\frac{\partial}{\partial x}, \qquad \hat p^2 = -\hbar^2\frac{\partial^2}{\partial x^2}, \qquad \hat E = i\hbar\frac{\partial}{\partial t} .
$$

Multiplying $E = T + U = \dfrac{p^2}{2m} + U$ by $\Psi$ and replacing $p$ and $E$ by these operators:

!!! abstract "The Schrödinger equation"
    $$
    i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + U\Psi
    \qquad\text{(three dimensions: } -\tfrac{\hbar^2}{2m}\nabla^2\Psi + U\Psi\text{)} .
    $$

!!! info "Remark — a postulate, not a theorem"
    The "derivation" above is a plausibility argument with large logical gaps. The equation is not deduced from earlier laws; it is accepted as a basic principle because what it predicts agrees with measurement.

### Statistical interpretation

The probability of finding the particle between $x$ and $x + dx$ at time $t$ is $|\Psi(x,t)|^2\,dx$, and between $a$ and $b$ it is $\int_a^b |\Psi|^2dx$. A large $|\Psi|^2$ means a large probability of finding the *whole* particle there, not that part of the particle is there.

For a probability density $f(x)$: $\int f = 1$, $\langle x\rangle = \int xf\,dx$, $\langle g(x)\rangle = \int g f\,dx$, $\sigma^2 = \langle x^2\rangle - \langle x\rangle^2$.

!!! note "Definition 5.1.1 (Normalization)"
    $\displaystyle \int_{-\infty}^\infty |\Psi(x,t)|^2\,dx = 1$. A wavefunction that cannot be normalized has no physical meaning.

!!! example "Example 5.1.2"
    $\Psi = ax$ for $0 < x < 1$ and $0$ elsewhere.

    (a) $\int_0^1 a^2x^2dx = a^2/3 = 1$, so $a = \sqrt3$.
    (b) $P(0.5 < x < 0.6) = 3\int_{0.5}^{0.6}x^2dx = 0.6^3 - 0.5^3 = 0.091$.
    (c) $\langle x\rangle = 3\int_0^1 x^3dx = 3/4$.

**Conditions on a physical wavefunction.** $\Psi$ and $\partial\Psi/\partial x$ are continuous and single-valued everywhere, and $\Psi$ is normalizable, so $\Psi \to 0$ as $x \to \pm\infty$.

### Superposition

Why not work only with $|\Psi|^2$? In the double slit, slit 1 alone gives $P_1 = |\Psi_1|^2$ and slit 2 alone $P_2 = |\Psi_2|^2$, but with both open

$$
|\Psi_1 + \Psi_2|^2 = P_1 + P_2 + \Psi_1^*\Psi_2 + \Psi_2^*\Psi_1 \neq P_1 + P_2 .
$$

The cross terms are the interference pattern. Amplitudes add; probabilities do not.

### Operators and expectation values

$$
\langle Q\rangle = \int_{-\infty}^\infty \Psi^*\hat Q\,\Psi\,dx ,
$$

with the operator placed between $\Psi^*$ and $\Psi$, because physical quantities are operators and operators do not commute in general ($\hat A\hat B \neq \hat B\hat A$). The **Hamiltonian** is $\hat H = \dfrac{\hat p^2}{2m} + U$, the energy written in terms of position and momentum; for a potential that does not depend on time it is the total energy.

!!! example "Example 5.1.3 (Gaussian wave packet)"
    $\Psi(x,0) = Ae^{-ax^2}$ ($a > 0$ is needed for normalizability).

    (a) $\int A^2e^{-2ax^2}dx = A^2\sqrt{\pi/2a} = 1$, so $A = (2a/\pi)^{1/4}$.

    (b) By symmetry $\langle x\rangle = 0$ and $\langle p\rangle = 0$. Using $\int x^2e^{-2ax^2}dx = \frac{1}{4a}\sqrt{\pi/2a}$,

    $$
    \langle x^2\rangle = \frac{1}{4a}, \qquad
    \langle p^2\rangle = -\hbar^2\int \Psi\,\Psi''\,dx = \hbar^2 a .
    $$

    (c) $\sigma_x\sigma_p = \sqrt{\tfrac{1}{4a}}\sqrt{\hbar^2a} = \dfrac{\hbar}{2}$: the uncertainty principle holds with equality. The Gaussian is the minimum-uncertainty state.

---

## 5.7 The Time-Independent Schrödinger Equation

<p class="lecture-tag">Textbook §5.7</p>

If $U$ does not depend on time, try $\Psi(x,t) = \psi(x)\phi(t)$. Dividing the Schrödinger equation by $\psi\phi$,

$$
i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + U = E .
$$

The left side depends only on $t$ and the right side only on $x$, so both equal a constant, which (from the right side) is the energy $E$. The time equation gives $\phi(t) = e^{-iEt/\hbar}$, and $|\phi|^2 = 1$: the time factor no longer affects the probability density.

!!! abstract "Time-independent Schrödinger equation"
    $$
    -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + U\psi = E\psi, \qquad\text{i.e.}\qquad \hat H\psi = E\psi .
    $$

Each separated solution $\Psi_n = \psi_n e^{-iE_nt/\hbar}$ is a **stationary state**: it changes in time, but its probability density does not.

!!! info "Remark — a stationary state has sharp energy"
    $\langle H\rangle = \int\psi^*\hat H\psi\,dx = E$ and $\langle H^2\rangle = E^2$, so $\sigma_H = 0$. A separated solution has a definite energy.

A general solution is a linear combination of separated ones,

$$
\Psi(x,t) = \sum_n c_n\psi_n(x)e^{-iE_nt/\hbar}.
$$

### Eigenvalues and eigenfunctions

If $\hat Q\psi_n = Q_n\psi_n$, then $Q_n$ is an **eigenvalue** and $\psi_n$ an **eigenfunction** of $\hat Q$. Solving the time-independent equation is finding the eigenvalues (energies) and eigenfunctions of $\hat H$.

!!! example "Example 5.7.1"
    $\dfrac{d^2}{dx^2}e^{2x} = 4e^{2x}$: the eigenvalue is $4$.

| Quantity | Operator |
|---|---|
| position $x$ | $x$ |
| momentum $p$ | $\dfrac{\hbar}{i}\dfrac{\partial}{\partial x}$ |
| potential energy $U(x)$ | $U(x)$ |
| kinetic energy $p^2/2m$ | $-\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2}$ |
| total energy $E$ | $i\hbar\dfrac{\partial}{\partial t}$ |
| Hamiltonian $H$ | $-\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2} + U(x)$ |

---

## 5.8 Particle in a Box

<p class="lecture-tag">Textbook §5.8</p>

$U = 0$ for $0 < x < L$ and $U = \infty$ outside, so $\psi(0) = \psi(L) = 0$. Inside, $\psi'' = -k^2\psi$ with $k = \sqrt{2mE}/\hbar$, and $\psi = Ae^{ikx} + Be^{-ikx}$.

- $\psi(0) = 0$ gives $B = -A$, so $\psi = 2iA\sin kx$.
- $\psi(L) = 0$ gives $kL = n\pi$, $n = 1, 2, 3, \dots$ ($n = 0$ gives $\psi \equiv 0$; $-n$ gives the same state up to a constant factor.)

!!! abstract "Theorem 5.8.1"
    $$
    E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad \psi_n(x) = \sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L} .
    $$

Writing $\psi = A\sin kx + B\cos kx$ instead gives the same result ($B = 0$ from $\psi(0) = 0$).

!!! abstract "Proposition 5.8.2 (Orthonormality)"
    $\displaystyle \int_0^L \psi_m^*\psi_n\,dx = \delta_{mn}$.

!!! success "Proof"
    $\sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L} = \frac12\big[\cos\frac{(m-n)\pi x}{L} - \cos\frac{(m+n)\pi x}{L}\big]$, and for $m \neq n$ both cosines integrate to $0$ over $[0, L]$. For $m = n$ the first term is $\frac12$ and gives $\frac{2}{L}\cdot\frac{L}{2} = 1$. $\square$

### Momentum

$\langle p\rangle = \int\psi_n\frac{\hbar}{i}\psi_n'\,dx = 0$, and $\langle p^2\rangle = 2mE_n = (n\pi\hbar/L)^2$, so

$$
\sigma_p = \frac{n\pi\hbar}{L} .
$$

Classically $p = \pm\sqrt{2mE_n} = \pm n\pi\hbar/L$. In fact $\psi_n$ is **not** a momentum eigenfunction: $\hat p\psi_n \propto \cos$, not $\propto \psi_n$. But

$$
\psi_n = \sqrt{\frac2L}\,\frac{1}{2i}\left(e^{in\pi x/L} - e^{-in\pi x/L}\right),
$$

a superposition of two momentum eigenfunctions $e^{\pm ikx}$ with $p = \pm\hbar k = \pm n\pi\hbar/L$, each with probability $\tfrac12$.

!!! example "Example 5.8.3 (Uncertainty in the box)"
    With $\langle x\rangle = L/2$ and $\langle x^2\rangle = \dfrac{L^2}{3} - \dfrac{L^2}{2\pi^2n^2}$,

    $$
    \sigma_x\sigma_p = \frac{\hbar}{2}\sqrt{\frac{\pi^2n^2}{3} - 2} \ \ge\ \frac{\hbar}{2}\sqrt{\frac{\pi^2}{3} - 2} \approx 0.57\hbar > \frac{\hbar}{2} .
    $$

### Superpositions and $|c_n|^2$

A separated solution satisfies the time-independent equation; a combination such as $\frac{1}{\sqrt2}(\psi_1 + \psi_2)$ does not (it has no single energy), but with its time factors it satisfies the full Schrödinger equation. $|c_n|^2$ is the probability that a measurement of the energy gives $E_n$, so $\sum|c_n|^2 = 1$, and by orthonormality

$$
\langle H\rangle = \sum_n |c_n|^2E_n .
$$

!!! example "Example 5.8.4"
    $\Psi = 0.5\psi_1 + c_2\psi_2$ requires $0.25 + |c_2|^2 = 1$, so $|c_2| = \sqrt3/2$.

!!! example "Example 5.8.5 (A sloshing probability density)"
    For $\Psi(x,0) = \frac{\sqrt3}{2}\psi_1 + \frac12\psi_2$,

    $$
    |\Psi(x,t)|^2 = \frac34\psi_1^2 + \frac14\psi_2^2 + \frac{\sqrt3}{2}\psi_1\psi_2\cos\frac{(E_2 - E_1)t}{\hbar} .
    $$

    The position density oscillates with angular frequency $(E_2 - E_1)/\hbar$, because the two time factors do not cancel in the cross term. The probabilities $|c_n|^2$ of each energy do not change. Resetting the clock to $t = 0$ at a later time only multiplies each $c_n$ by a phase.

---

## 5.9 The Finite Potential Well

<p class="lecture-tag">Textbook §5.9</p>

$U = 0$ for $|x| < a$ and $U = V_0$ for $|x| > a$; bound states have $0 < E < V_0$.

If $U$ is symmetric, $|\psi|^2$ must be symmetric, so $\psi$ can be taken even or odd.

| Region | Equation | General solution | Physical solution |
|---|---|---|---|
| I: $x < -a$ | $\psi'' = \kappa^2\psi$, $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ | $Ce^{\kappa x} + De^{-\kappa x}$ | $Ce^{\kappa x}$ (finite as $x \to -\infty$) |
| II: $-a < x < a$ | $\psi'' = -k^2\psi$, $k = \sqrt{2mE}/\hbar$ | $A\cos kx + B\sin kx$ | $A\cos kx$ (even) |
| III: $x > a$ | by symmetry | | $Ce^{-\kappa x}$ |

Continuity of $\psi$ and $\psi'$ at $x = -a$: $Ce^{-\kappa a} = A\cos ka$ and $\kappa Ce^{-\kappa a} = kA\sin ka$. Dividing,

$$
\tan ka = \frac{\kappa}{k} = \sqrt{\frac{V_0}{E} - 1} .
$$

With $z = ka$ and $z_0 = a\sqrt{2mV_0}/\hbar$:

!!! abstract "Even bound states"
    $$
    \tan z = \sqrt{\left(\frac{z_0}{z}\right)^2 - 1} .
    $$

This is a transcendental equation: it has no explicit solution $z = \cdots$, and the allowed energies are found graphically as intersections of the two sides.

- **Wide, deep well** ($z_0$ large): the intersections approach $z = (2n-1)\pi/2$, and $E$ approaches the infinite-well energies.
- **Narrow, shallow well** ($z_0$ small): there are few intersections, but always at least one. There is always at least one bound state.
- **Odd states** ($\psi = B\sin kx$ inside) give $-\cot z = \sqrt{(z_0/z)^2 - 1}$, which has a solution only if $z_0 > \pi/2$. An odd bound state does not always exist.

---

## 5.10 Tunnelling

| | Infinite well | Finite well | Potential barrier |
|---|---|---|---|
| $\psi$ outside the wall | $0$ | nonzero (decays) | nonzero (tunnels through) |
| types of state | bound | bound / scattering | scattering |
| energies | $E_n = n^2\pi^2\hbar^2/2mL^2$ | quantized, from a transcendental equation | continuous |

Wherever $U$ is finite, $\psi$ does not vanish beyond a wall: it decays exponentially inside a barrier and can emerge on the other side. This is tunnelling.

---

## 5.11 The Harmonic Oscillator: Algebraic Method

<p class="lecture-tag">Textbook §5.11</p>

### Commutators

$[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$. Acting on a test function, $[x, \hat p]f = x\frac{\hbar}{i}f' - \frac{\hbar}{i}(xf)' = i\hbar f$, so

$$
[x, \hat p] = i\hbar, \qquad [\hat p, x] = -i\hbar .
$$

### Ladder operators

With $U = \frac12 m\omega^2x^2$, $\hat H = \frac{1}{2m}\big[\hat p^2 + (m\omega x)^2\big]$. Imitating $f^2 + g^2 = (if + g)(-if + g)$, define

$$
\hat a_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\,(\mp i\hat p + m\omega x) .
$$

Then $\hat a_\pm\hat a_\mp = \dfrac{1}{2\hbar m\omega}\big[\hat p^2 + (m\omega x)^2 \mp im\omega[x, \hat p]\big] = \dfrac{\hat H}{\hbar\omega} \pm \dfrac12$, so

$$
\hat H = \hbar\omega\left(\hat a_\pm\hat a_\mp \mp \frac12\right), \qquad [\hat a_-, \hat a_+] = 1 .
$$

$\hat a_+$ and $\hat a_-$ are adjoints of each other: $\int f^*(\hat a_\pm g)\,dx = \int(\hat a_\mp f)^*g\,dx$.

!!! abstract "Theorem 5.11.1"
    If $\hat H\psi = E\psi$, then $\hat H(\hat a_\pm\psi) = (E \pm \hbar\omega)(\hat a_\pm\psi)$.

!!! success "Proof"
    $\hat H(\hat a_+\psi) = \hbar\omega(\hat a_+\hat a_- + \tfrac12)\hat a_+\psi = \hbar\omega\,\hat a_+(\hat a_-\hat a_+ + \tfrac12)\psi = \hat a_+\big(\hbar\omega(\hat a_+\hat a_- + 1 + \tfrac12)\psi\big) = \hat a_+(\hat H + \hbar\omega)\psi = (E + \hbar\omega)\hat a_+\psi$, using $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$. The case of $\hat a_-$ is the same. $\square$

So a ladder operator turns an eigenfunction into another one, not necessarily normalized. Lowering cannot go on forever (the energy is bounded below), so there is a ground state with $\hat a_-\psi_0 = 0$:

$$
\frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x\right)\psi_0 = 0
\;\Longrightarrow\; \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0
\;\Longrightarrow\; \psi_0 = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar} .
$$

!!! abstract "Theorem 5.11.2"
    $$
    E_n = \left(n + \frac12\right)\hbar\omega, \qquad
    \hat a_+\hat a_-\psi_n = n\psi_n, \quad \hat a_-\hat a_+\psi_n = (n+1)\psi_n, \qquad
    \psi_n = \frac{1}{\sqrt{n!}}(\hat a_+)^n\psi_0 .
    $$

!!! success "Proof"
    $\hat H\psi_0 = \hbar\omega(\hat a_+\hat a_- + \tfrac12)\psi_0 = \tfrac12\hbar\omega\,\psi_0$, and each raising adds $\hbar\omega$. From $\hat H = \hbar\omega(\hat a_+\hat a_- + \frac12)$ and $E_n$, $\hat a_+\hat a_-\psi_n = n\psi_n$; then $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$ gives $n + 1$.

    For the normalization, put $\hat a_+\psi_n = c_n\psi_{n+1}$. Then

    $$
    |c_n|^2 = \int(\hat a_+\psi_n)^*(\hat a_+\psi_n)\,dx = \int\psi_n^*\,\hat a_-\hat a_+\psi_n\,dx = n + 1,
    $$

    so $c_n = \sqrt{n+1}$ and $\psi_n = \frac{1}{\sqrt{n!}}(\hat a_+)^n\psi_0$. $\square$

!!! example "Example 5.11.3 ($x$, $p$ and the virial result)"
    Adding and subtracting the definitions of $\hat a_\pm$,

    $$
    x = \sqrt{\frac{\hbar}{2m\omega}}\,(\hat a_+ + \hat a_-), \qquad
    \hat p = i\sqrt{\frac{\hbar m\omega}{2}}\,(\hat a_+ - \hat a_-) .
    $$

    Then $x^2 = \frac{\hbar}{2m\omega}(\hat a_+^2 + \hat a_+\hat a_- + \hat a_-\hat a_+ + \hat a_-^2)$. The squared terms change $n$ by $\pm2$ and vanish in $\langle\psi_n|\cdot|\psi_n\rangle$ by orthogonality, so $\langle x^2\rangle = \frac{\hbar}{2m\omega}(2n+1)$ and

    $$
    \left\langle\tfrac12 m\omega^2x^2\right\rangle = \frac12\left(n + \frac12\right)\hbar\omega = \left\langle\frac{p^2}{2m}\right\rangle .
    $$

    Potential and kinetic energy each carry half of $E_n$.

---

## What the Midterm Tends to Ask

The 2024 and 2025 midterms drew on this chapter as follows.

- **Infinite well with a non-eigenstate**: for $\Psi(x,0) = Ax(L - x)$, normalize ($A = \sqrt{30/L^5}$); expand in $\psi_n$ and find $P(E_1) = |c_1|^2 = 960/\pi^6 \approx 0.96$; compute $\langle H\rangle = \sum|c_n|^2E_n = 5\hbar^2/mL^2$. The shape of $Ax(L-x)$ is close to $\psi_1$, which is why $E_1$ dominates.
- **Time evolution** of $c\psi_1 + \frac{\sqrt2}{2}\psi_2$: find $c$, $\Psi(x,t)$, the real probability density, and the period $2\pi\hbar/(E_2 - E_1)$ of its oscillation (Example 5.8.5).
- **Harmonic oscillator**: normalized $\psi_0$, eigenvalues of $\hat a_-\hat a_+$ and $\hat a_+\hat a_-$, $x$ and $\hat p$ in terms of $\hat a_\pm$, $\langle V\rangle$ and $\langle T\rangle$ (§5.11).
- **Interpretation**: why the Schrödinger equation is a postulate; what $|c_n|^2$ means; why a separated solution has sharp energy.
