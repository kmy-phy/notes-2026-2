---
title: "Part II — Special Relativity I (midterm range)"
---

<div class="lang-switch"><a class="on">English</a><a href="../sr1-ko/">한국어</a></div>

<div class="running-head"><span>Modern Physics</span><span>Part II · Relativity I</span></div>

# Part II — Special Relativity I { .part-title }

<p class="source-note">Lecture notes, midterm range · <a class="pdf-link" href="notes.pdf" download="Modern-Physics-Relativity-I.pdf">Download this part as PDF</a></p>

**In this part.** The Lorentz transformation is a rotation in spacetime with an imaginary angle. From it follow the relativity of simultaneity and the limits causality puts on it, the twin paradox, and the four-vectors whose squares are the same in every frame, which make collisions easy to solve with energy–momentum conservation. Sections 6–11 continue in [Special Relativity II](../sr2/).

!!! quote "Conventions used in this part."
    - $S$ is the lab frame. A primed frame $S'$ moves relative to $S$ with velocity $v$ along $x$; $\beta = v/c$.
    - $\gamma(v) = \gamma_v = \dfrac{1}{\sqrt{1 - v^2/c^2}}$.
    - $L_0$ is a proper length (measured at rest); $\lambda$ is a line charge density and $\lambda_0$ its value in the lab; $I = \lambda v$.
    - $\hat n$ is an outward unit normal, $d\tau$ a volume element.

---

## 1 The Lorentz Transformation as a Rotation

A rotation of the axes by $\theta$ takes $(x, y)$ to

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}.
$$

Replace the second coordinate by an imaginary time, $y \to ict$. A frame $S'$ moving with velocity $v$ has its $ct'$-axis along $x = vt$, which in the rotated picture means $\tan\theta' = -x/(ict)$, i.e.

$$
\theta' = \tan^{-1}\!\left(i\frac{v}{c}\right) = i\tanh^{-1}\beta \equiv i\phi .
$$

!!! info "Remark — hyperbolic functions"
    From $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$ and $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$:

    $$
    \cos(i\phi) = \cosh\phi, \qquad \sin(i\phi) = i\sinh\phi, \qquad \cosh^2\phi - \sinh^2\phi = 1 ,
    $$

    and $\tan^{-1}x = \frac{1}{2i}\ln\frac{1+ix}{1-ix}$, $\tanh^{-1}x = \frac12\ln\frac{1+x}{1-x}$, so $\tan^{-1}(ix) = i\tanh^{-1}x$.

With $\beta = \tanh\phi$: $\cosh^2\phi = \dfrac{1}{1-\beta^2} = \gamma^2$, so $\cosh\phi = \gamma$ and $\sinh\phi = \gamma\beta$. The rotation becomes

$$
\begin{pmatrix} x' \\ ict' \end{pmatrix} = \begin{pmatrix} \cosh\phi & i\sinh\phi \\ -i\sinh\phi & \cosh\phi \end{pmatrix}\begin{pmatrix} x \\ ict \end{pmatrix}
= \begin{pmatrix} \gamma & i\gamma\beta \\ -i\gamma\beta & \gamma \end{pmatrix}\begin{pmatrix} x \\ ict \end{pmatrix}.
$$

!!! abstract "Lorentz transformation"
    $$
    x' = \gamma(x - vt), \qquad t' = \gamma\left(t - \frac{v}{c^2}x\right).
    $$

The parameter $\phi$ is called the **rapidity**. Rotations preserve $x^2 + y^2$; with $y = ict$ the preserved quantity is $x^2 - c^2t^2$.

---

## 2 Causality and Spacetime Diagrams

Let an event (say, the emission of a signal) happen at $(x_1, t_1)$ and another at $(x_2, t_2)$ in $S$. In $S'$,

$$
\Delta t' = \frac{\Delta t - \frac{v}{c^2}\Delta x}{\sqrt{1 - v^2/c^2}} .
$$

The order of the events reverses ($\Delta t' < 0$ with $\Delta t > 0$) when $\Delta t < \frac{v}{c^2}\Delta x$, i.e. $\dfrac{c\Delta t}{\Delta x} < \dfrac{v}{c} < 1$. This needs $c\Delta t < \Delta x$.

- If the events are causally connected (a signal no faster than light can go from one to the other), then $c\Delta t \ge \Delta x$ and the order is the same in every frame.
- If not, $c\Delta t < \Delta x$ is possible, and different frames may disagree about which came first.

On a spacetime diagram ($x$ horizontal, $ct$ vertical), the lines $x = \pm ct$ form the **light cone**. Events inside it, relative to the origin, are **timelike** separated and can be causally connected; events outside are **spacelike** separated. The axes of $S'$ are the $ct'$-axis $x = vt$ and the $x'$-axis $ct = \beta x$, tilted symmetrically toward the light line. Lines parallel to the $x'$-axis are lines of simultaneity in $S'$.

!!! info "Remark — simultaneity is not absolute"
    Two events on a line of simultaneity of $S'$ are simultaneous in $S'$ but not in $S$. Every paradox below comes down to this.

---

## 3 The Twin Paradox

A twin travels at $v = 0.6c$ to a star $6$ light-years away and returns; $\gamma = 1/0.8 = 1.25$.

- **Earth frame $S$.** Each leg takes $6/0.6 = 10$ years: the traveller turns around at the event $(x, ct) = (6, 10)$ and returns at $ct = 20$.
- **Traveller.** On each leg the distance is contracted to $6 \times 0.8 = 4.8$ light-years, which takes $4.8/0.6 = 8$ years. The round trip takes $16$ years.

The traveller is younger by $4$ years. The situation is not symmetric: the traveller changes inertial frame at the turnaround.

**The view from the outbound frame $S'$.** Using $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$, the turnaround $S(6, 10)$ is $S'(0, 8)$. The line of simultaneity through it hits the Earth's worldline at $ct = 6.4$: just before turning, the traveller says Earth's clock reads $6.4$ years. Just after turning, in the inbound frame, the line of simultaneity through the same event hits Earth's worldline at $ct = 13.6$. The traveller's notion of "Earth's now" jumps by $7.2$ years during the turnaround, and $6.4 + 7.2 + 6.4 = 20$.

---

## 4 Four-Vectors

Quantities are either **covariant** (they transform by the Lorentz transformation, like $(ct, x)$) or **invariant** (the same in every frame): the proper time $\tau$, the proper length $L_0$, the rest mass $m$, the charge $q$.

Proper time is the key invariant: two clocks $A$ and $B$ that each measure their own $\tau$ give each frame's time as $t_A = \gamma_A\tau$, $t_B = \gamma_B\tau$, and every frame agrees on $\tau$.

!!! note "Definition 4.1 (Position four-vector)"
    $\mathbb{X} = (ct, x, y, z) = (x_0, x_1, x_2, x_3)$, with the invariant square

    $$
    |\mathbb{X}|^2 = x_0^2 - (x_1^2 + x_2^2 + x_3^2) .
    $$

!!! abstract "Proposition 4.2"
    For two events, $|\Delta\mathbb X|^2 = (\Delta x_0)^2 - (\Delta x_1)^2$ is the same in $S$ and $S'$.

!!! success "Proof"
    $$
    (\Delta x_0')^2 - (\Delta x_1')^2 = \gamma^2\big[(\Delta x_0 - \beta\Delta x_1)^2 - (\Delta x_1 - \beta\Delta x_0)^2\big]
    = \gamma^2\big[(\Delta x_0)^2(1 - \beta^2) - (\Delta x_1)^2(1 - \beta^2)\big] = (\Delta x_0)^2 - (\Delta x_1)^2 . \;\square
    $$

Dividing $\Delta\mathbb X$ by the invariant $\Delta\tau$ gives new four-vectors.

!!! note "Definition 4.3 (Four-velocity, four-momentum)"
    $$
    \mathbb V = \frac{d\mathbb X}{d\tau} = (\gamma c, \gamma\vec v), \quad |\mathbb V|^2 = \gamma^2c^2(1 - \beta^2) = c^2;
    \qquad
    \mathbb P = m\mathbb V = (\gamma mc, \gamma m\vec v) = \left(\frac{E}{c}, \vec p\right).
    $$

    (Here $\frac{dx_1}{d\tau} = \frac{dx_1}{dt}\frac{dt}{d\tau} = v\gamma$.)

For $v \ll c$, $P_0 = mc(1 - v^2/c^2)^{-1/2} = mc + \frac12 mv^2/c + \cdots$, so $cP_0 = mc^2 + \frac12 mv^2 + \cdots = E$: the time component is the energy over $c$, including the rest energy $mc^2$.

!!! abstract "Energy–momentum relation"
    $|\mathbb P|^2 = \dfrac{E^2}{c^2} - p^2 = m^2c^2$, so

    $$
    E^2 = (pc)^2 + (mc^2)^2 .
    $$

For light, $m = 0$, $v = c$: $\gamma m v$ is $0\cdot\infty$, so we define the photon's four-momentum directly as $\mathbb K = (E/c, \vec p)$ with $|\mathbb K|^2 = 0$, i.e. $E = pc$. With $E = hf = \hbar\omega$ and $p = h/\lambda = \hbar k$,

$$
\mathbb K = \left(\frac{\hbar\omega}{c}, \hbar\vec k\right), \qquad \omega = ck .
$$

---

## 5 Collisions with Four-Momentum

Four-momentum is conserved in collisions, and $|\mathbb P|^2$ is invariant. Squaring a conservation law and evaluating the invariant in the most convenient frame is the main technique.

!!! example "Example 5.1 (A photon absorbed by a particle)"
    A photon of energy $\hbar\omega$ hits a particle of mass $m$ at rest and is absorbed, leaving one particle of mass $M$:

    $$
    \mathbb K + \mathbb P = \mathbb P_f, \qquad \mathbb K = \left(\tfrac{\hbar\omega}{c}, \hbar k\right),\ \mathbb P = (mc, 0).
    $$

    Squaring, $|\mathbb K|^2 + |\mathbb P|^2 + 2\mathbb K\cdot\mathbb P = |\mathbb P_f|^2$, with $|\mathbb K|^2 = 0$, $|\mathbb P|^2 = m^2c^2$, $|\mathbb P_f|^2 = M^2c^2$, $\mathbb K\cdot\mathbb P = \hbar\omega m$:

    $$
    2\hbar\omega m = (M^2 - m^2)c^2 .
    $$

!!! example "Example 5.2 (Antiproton production threshold)"
    A proton is accelerated onto a proton at rest, producing three protons and one antiproton: $p + p \to p + p + p + \bar p$. What is the minimum energy $E$ of the incoming proton?

    At threshold the four products move together, so in their centre-of-momentum frame $\mathbb P_f' = (4mc, \vec 0)$ and $|\mathbb P_f|^2 = 16m^2c^2$. With $\mathbb P_1 = (E/c, \vec p)$, $\mathbb P_2 = (mc, \vec 0)$:

    $$
    |\mathbb P_1 + \mathbb P_2|^2 = m^2c^2 + m^2c^2 + 2mE = 16m^2c^2 \;\Longrightarrow\; E = 7mc^2 .
    $$

    The kinetic energy needed is $6mc^2$, three times the rest energy of the pair that is created.
