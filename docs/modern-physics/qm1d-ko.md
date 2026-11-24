---
title: "1부 — 5장: 1차원 양자역학"
---

<div class="lang-switch"><a href="../qm1d/">English</a><a class="on">한국어</a></div>

<div class="running-head"><span>현대물리학</span><span>1부 · 5장</span></div>

# 5장 — 1차원 양자역학 { .part-title #chapter-5-quantum-mechanics-in-one-dimension }

<p class="source-note">5장 학습지 (중간고사 범위, 교과서 §5.1–5.11) · <a class="pdf-link" href="notes.pdf" download="현대물리학-5장.pdf">이 장을 PDF로 보기</a></p>

**이 장에서는.** 파동함수 $\Psi(x,t)$와 그 통계적 의미, 운동량과 에너지를 연산자로 바꾸는 규칙으로 읽는 슈뢰딩거 방정식, 변수분리와 시간에 무관한 방정식, 그리고 대표적인 1차원 문제인 무한 퍼텐셜 우물, 유한 퍼텐셜 우물, 터널링, 사다리 연산자로 푸는 조화진동자를 다룬다. 6장(수소 원자)은 이것을 바로 이어받는다.

!!! quote "이 장에서 쓰는 규약."
    - $\hbar = h/2\pi$. $m$은 입자의 질량, $U(x)$(또는 $V(x)$)는 퍼텐셜 에너지이다.
    - $\Psi(x,t)$는 전체 파동함수, $\psi(x)$는 공간 부분, $\phi(t)$는 시간 부분이다.
    - $\langle Q\rangle = \int \Psi^* \hat Q\,\Psi\,dx$, $\sigma_Q^2 = \langle Q^2\rangle - \langle Q\rangle^2$.
    - 무한 우물의 고유함수는 $0 < x < L$에서 $\psi_n = \sqrt{2/L}\,\sin(n\pi x/L)$이다.

---

## 5.0 수학적 도구 { #50-mathematical-tools }

### 테일러 급수와 오일러 공식 { #taylor-series-and-eulers-formula }

매끄러운 함수는 $0$ 근처에서 $f(x) = a_0 + a_1x + a_2x^2 + \cdots$, $a_n = f^{(n)}(0)/n!$로 전개된다. 특히

$$
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots, \qquad
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots .
$$

!!! abstract "정리 5.0.1 (오일러 공식)"
    $$
    e^{ix} = \cos x + i\sin x .
    $$

!!! success "증명"
    $e^{ix} = \sum (ix)^n/n!$을 전개하면 $a_0 = 1$, $a_1 = i$, $a_2 = -\frac{1}{2!}$, $a_3 = -\frac{i}{3!}, \dots$이다. 실수 항은 $\cos x$의 급수이고, 허수 항은 $\sin x$의 급수에 $i$를 곱한 것이다. $\square$

이 밖에 자주 쓰는 도구: 전미분(예: $PV = nRT \Rightarrow P\,dV + V\,dP = nR\,dT$), 치환적분(예: $u = x^2$로 $\int_0^{\sqrt\pi} x\sin(x^2)\,dx = \tfrac12\int_0^\pi \sin u\,du = 1$), 부분적분 $\int uv'\,dx = uv - \int u'v\,dx$, 극좌표·구면좌표 $dx\,dy = r\,dr\,d\theta$, $dx\,dy\,dz = r^2\sin\theta\,dr\,d\theta\,d\phi$.

### 감마 함수 { #the-gamma-function }

!!! abstract "보조정리 5.0.2"
    $a > 0$이면 $\displaystyle \lim_{x\to\infty} x e^{-ax} = 0$.

!!! success "증명"
    $e^{ax} = 1 + ax + \frac{(ax)^2}{2} + \cdots > \frac{a^2x^2}{2}$이므로 $0 < \dfrac{x}{e^{ax}} < \dfrac{2}{a^2x} \to 0$. $\square$

부분적분을 반복하면(경계항은 보조정리 5.0.2에 의해 사라진다)

$$
\int_0^\infty e^{-x}dx = 1, \quad \int_0^\infty xe^{-x}dx = 1, \quad \int_0^\infty x^2e^{-x}dx = 2, \quad \int_0^\infty x^3e^{-x}dx = 6 .
$$

!!! note "정의 5.0.3 (감마 함수)"
    $$
    \Gamma(p) = \int_0^\infty x^{p-1}e^{-x}\,dx \quad (p > 0), \qquad p\text{가 정수이면 } \Gamma(p) = (p-1)! .
    $$

!!! abstract "명제 5.0.4"
    $\Gamma(p+1) = p\,\Gamma(p)$이고, $\Gamma(\tfrac12) = \sqrt\pi$이다.

!!! success "증명"
    부분적분으로 $\Gamma(p+1) = \big[-x^pe^{-x}\big]_0^\infty + p\int_0^\infty x^{p-1}e^{-x}dx = p\Gamma(p)$.

    $x = u^2$로 두면 $\Gamma(\tfrac12) = \int_0^\infty x^{-1/2}e^{-x}dx = 2\int_0^\infty e^{-u^2}du$이다. 제곱하고 제1사분면에서 극좌표로 바꾸면

    $$
    \Gamma(\tfrac12)^2 = 4\int_0^\infty\!\!\int_0^\infty e^{-(x^2+y^2)}dx\,dy = 4\int_0^{\pi/2}\!\!\int_0^\infty e^{-r^2}r\,dr\,d\theta = 4\cdot\frac{\pi}{2}\cdot\frac12 = \pi . \qquad\square
    $$

!!! info "참고 — 정사각형과 원"
    $\int_0^\infty\!\int_0^\infty dx\,dy$에서 $\int_0^{\pi/2}\!\int_0^\infty r\,dr\,d\theta$로 가는 단계는 무한히 큰 정사각형을 무한히 큰 사분원으로 바꾼다. 이렇게 빨리 줄어드는 피적분함수에서는 두 극한이 같다.

---

## 5.1 파동함수와 슈뢰딩거 방정식 { #51-the-wavefunction-and-the-schrodinger-equation }

### 파동과 복소 파동함수 { #waves-and-complex-wavefunctions }

$x$ 방향으로 속력 $v$로 진행하는 파동은 $y = A\sin(kx-\omega t)$로, 더 일반적으로는 $A\cos(kx-\omega t) + iA\sin(kx-\omega t) = Ae^{i(kx-\omega t)}$로 쓸 수 있고, $Ae^{i(kx-\omega t)} + Be^{-i(kx+\omega t)}$는 양쪽 방향을 모두 포함한다. 이들은 모두 고전적 파동방정식 $\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{v^2}\dfrac{\partial^2 y}{\partial t^2}$을 만족한다.

고전적으로는 실수부만 물리적 의미가 있다. 양자역학에서 $\Psi(x,t)$는 일반적으로 복소수이며 그 자체로는 측정할 수 없다. 의미가 있는 것은 확률밀도 $|\Psi|^2 = \Psi^*\Psi$이다.

드브로이의 $p = h/\lambda = \hbar k$와 플랑크의 $E = hf = \hbar\omega$를 쓰면, 파동 $\Psi = Ae^{i(px - Et)/\hbar}$는 에너지 $E$, 운동량 $p$인 자유 입자($U = 0$)를 나타낸다.

### 방정식 유도 { #deriving-the-equation }

$$
\frac{\partial^2\Psi}{\partial x^2} = -k^2\Psi = -\frac{p^2}{\hbar^2}\Psi, \qquad
\frac{\partial\Psi}{\partial t} = -i\omega\Psi = -\frac{iE}{\hbar}\Psi .
$$

따라서 $\Psi$에 작용할 때 운동량과 에너지는 연산자처럼 행동한다.

$$
\hat p = \frac{\hbar}{i}\frac{\partial}{\partial x}, \qquad \hat p^2 = -\hbar^2\frac{\partial^2}{\partial x^2}, \qquad \hat E = i\hbar\frac{\partial}{\partial t} .
$$

$E = T + U = \dfrac{p^2}{2m} + U$에 $\Psi$를 곱하고 $p$와 $E$를 이 연산자로 바꾸면:

!!! abstract "슈뢰딩거 방정식"
    $$
    i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + U\Psi
    \qquad\text{(3차원: } -\tfrac{\hbar^2}{2m}\nabla^2\Psi + U\Psi\text{)} .
    $$

!!! info "참고 — 정리가 아니라 공리"
    위의 "유도"는 논리적 비약이 큰, 그럴듯함을 보이는 논증이다. 이 방정식은 이전의 법칙에서 연역된 것이 아니다. 예측이 측정과 맞기 때문에 기본 원리로 받아들인다.

### 통계적 해석 { #statistical-interpretation }

시각 $t$에 입자를 $x$와 $x + dx$ 사이에서 발견할 확률은 $|\Psi(x,t)|^2\,dx$이고, $a$와 $b$ 사이에서는 $\int_a^b |\Psi|^2dx$이다. $|\Psi|^2$이 크다는 것은 거기서 입자 *전체*를 발견할 확률이 크다는 뜻이지, 입자의 일부가 거기 있다는 뜻이 아니다.

확률밀도함수 $f(x)$에 대해: $\int f = 1$, $\langle x\rangle = \int xf\,dx$, $\langle g(x)\rangle = \int g f\,dx$, $\sigma^2 = \langle x^2\rangle - \langle x\rangle^2$.

!!! note "정의 5.1.1 (규격화)"
    $\displaystyle \int_{-\infty}^\infty |\Psi(x,t)|^2\,dx = 1$. 규격화할 수 없는 파동함수는 물리적 의미가 없다.

!!! example "예제 5.1.2"
    $0 < x < 1$에서 $\Psi = ax$, 그 밖에서는 $0$.

    (a) $\int_0^1 a^2x^2dx = a^2/3 = 1$이므로 $a = \sqrt3$.
    (b) $P(0.5 < x < 0.6) = 3\int_{0.5}^{0.6}x^2dx = 0.6^3 - 0.5^3 = 0.091$.
    (c) $\langle x\rangle = 3\int_0^1 x^3dx = 3/4$.

**물리적인 파동함수의 조건.** $\Psi$와 $\partial\Psi/\partial x$는 모든 곳에서 연속이고 일가함수이며, $\Psi$는 규격화 가능하므로 $x \to \pm\infty$에서 $\Psi \to 0$이다.

### 중첩 { #superposition }

왜 $|\Psi|^2$만 다루지 않는가? 이중 슬릿에서 슬릿 1만 열면 $P_1 = |\Psi_1|^2$, 슬릿 2만 열면 $P_2 = |\Psi_2|^2$이지만, 둘 다 열면

$$
|\Psi_1 + \Psi_2|^2 = P_1 + P_2 + \Psi_1^*\Psi_2 + \Psi_2^*\Psi_1 \neq P_1 + P_2 .
$$

교차항이 간섭무늬이다. 더해지는 것은 진폭이지 확률이 아니다.

### 연산자와 기댓값 { #operators-and-expectation-values }

$$
\langle Q\rangle = \int_{-\infty}^\infty \Psi^*\hat Q\,\Psi\,dx .
$$

연산자를 $\Psi^*$와 $\Psi$ 사이에 두는 이유는, 물리량이 연산자이고 연산자는 일반적으로 교환하지 않기 때문이다($\hat A\hat B \neq \hat B\hat A$). **해밀토니안** $\hat H = \dfrac{\hat p^2}{2m} + U$는 위치와 운동량으로 쓴 에너지이며, 퍼텐셜이 시간에 의존하지 않으면 전체 에너지이다.

!!! example "예제 5.1.3 (가우스 파속)"
    $\Psi(x,0) = Ae^{-ax^2}$ (규격화하려면 $a > 0$이어야 한다).

    (a) $\int A^2e^{-2ax^2}dx = A^2\sqrt{\pi/2a} = 1$이므로 $A = (2a/\pi)^{1/4}$.

    (b) 대칭성에 의해 $\langle x\rangle = 0$, $\langle p\rangle = 0$이다. $\int x^2e^{-2ax^2}dx = \frac{1}{4a}\sqrt{\pi/2a}$를 쓰면

    $$
    \langle x^2\rangle = \frac{1}{4a}, \qquad
    \langle p^2\rangle = -\hbar^2\int \Psi\,\Psi''\,dx = \hbar^2 a .
    $$

    (c) $\sigma_x\sigma_p = \sqrt{\tfrac{1}{4a}}\sqrt{\hbar^2a} = \dfrac{\hbar}{2}$. 불확정성 원리가 등호로 성립한다. 가우스 함수는 최소 불확정 상태이다.

---

## 5.7 시간에 무관한 슈뢰딩거 방정식 { #57-the-time-independent-schrodinger-equation }

<p class="lecture-tag">교과서 §5.7</p>

$U$가 시간에 의존하지 않으면 $\Psi(x,t) = \psi(x)\phi(t)$로 놓아 본다. 슈뢰딩거 방정식을 $\psi\phi$로 나누면

$$
i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + U = E .
$$

좌변은 $t$에만, 우변은 $x$에만 의존하므로 둘 다 상수이고, 이 상수는 (우변에서 보듯) 에너지 $E$이다. 시간 방정식의 해는 $\phi(t) = e^{-iEt/\hbar}$이고 $|\phi|^2 = 1$이므로, 시간 인자는 더 이상 확률밀도에 영향을 주지 않는다.

!!! abstract "시간에 무관한 슈뢰딩거 방정식"
    $$
    -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + U\psi = E\psi, \qquad\text{즉}\qquad \hat H\psi = E\psi .
    $$

변수분리된 각 해 $\Psi_n = \psi_n e^{-iE_nt/\hbar}$는 **정상상태**이다. 시간에 따라 변하지만 확률밀도는 변하지 않는다.

!!! info "참고 — 정상상태의 에너지는 확정되어 있다"
    $\langle H\rangle = \int\psi^*\hat H\psi\,dx = E$이고 $\langle H^2\rangle = E^2$이므로 $\sigma_H = 0$이다. 변수분리된 해는 확정된 에너지를 가진다.

일반해는 변수분리된 해들의 일차결합이다.

$$
\Psi(x,t) = \sum_n c_n\psi_n(x)e^{-iE_nt/\hbar}.
$$

### 고윳값과 고유함수 { #eigenvalues-and-eigenfunctions }

$\hat Q\psi_n = Q_n\psi_n$이면 $Q_n$은 $\hat Q$의 **고윳값**, $\psi_n$은 **고유함수**이다. 시간에 무관한 방정식을 푼다는 것은 $\hat H$의 고윳값(에너지)과 고유함수를 찾는 것이다.

!!! example "예제 5.7.1"
    $\dfrac{d^2}{dx^2}e^{2x} = 4e^{2x}$이므로 고윳값은 $4$이다.

| 물리량 | 연산자 |
|---|---|
| 위치 $x$ | $x$ |
| 운동량 $p$ | $\dfrac{\hbar}{i}\dfrac{\partial}{\partial x}$ |
| 퍼텐셜 에너지 $U(x)$ | $U(x)$ |
| 운동 에너지 $p^2/2m$ | $-\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2}$ |
| 전체 에너지 $E$ | $i\hbar\dfrac{\partial}{\partial t}$ |
| 해밀토니안 $H$ | $-\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2} + U(x)$ |

---

## 5.8 상자 속 입자 { #58-particle-in-a-box }

<p class="lecture-tag">교과서 §5.8</p>

$0 < x < L$에서 $U = 0$, 밖에서 $U = \infty$이므로 $\psi(0) = \psi(L) = 0$이다. 안에서는 $k = \sqrt{2mE}/\hbar$로 $\psi'' = -k^2\psi$이고 $\psi = Ae^{ikx} + Be^{-ikx}$이다.

- $\psi(0) = 0$에서 $B = -A$이므로 $\psi = 2iA\sin kx$.
- $\psi(L) = 0$에서 $kL = n\pi$, $n = 1, 2, 3, \dots$ ($n = 0$이면 $\psi \equiv 0$이고, $-n$은 상수배를 제외하고 같은 상태이다.)

!!! abstract "정리 5.8.1"
    $$
    E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \qquad \psi_n(x) = \sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L} .
    $$

대신 $\psi = A\sin kx + B\cos kx$로 써도 같은 결과가 나온다($\psi(0) = 0$에서 $B = 0$).

!!! abstract "명제 5.8.2 (정규직교성)"
    $\displaystyle \int_0^L \psi_m^*\psi_n\,dx = \delta_{mn}$.

!!! success "증명"
    $\sin\frac{m\pi x}{L}\sin\frac{n\pi x}{L} = \frac12\big[\cos\frac{(m-n)\pi x}{L} - \cos\frac{(m+n)\pi x}{L}\big]$이고, $m \neq n$이면 두 코사인 모두 $[0, L]$에서 적분하면 $0$이다. $m = n$이면 첫째 항이 $\frac12$이 되어 $\frac{2}{L}\cdot\frac{L}{2} = 1$이다. $\square$

### 운동량 { #momentum }

$\langle p\rangle = \int\psi_n\frac{\hbar}{i}\psi_n'\,dx = 0$이고 $\langle p^2\rangle = 2mE_n = (n\pi\hbar/L)^2$이므로

$$
\sigma_p = \frac{n\pi\hbar}{L} .
$$

고전적으로는 $p = \pm\sqrt{2mE_n} = \pm n\pi\hbar/L$이다. 사실 $\psi_n$은 운동량 고유함수가 **아니다**. $\hat p\psi_n \propto \cos$이지 $\propto \psi_n$이 아니다. 그러나

$$
\psi_n = \sqrt{\frac2L}\,\frac{1}{2i}\left(e^{in\pi x/L} - e^{-in\pi x/L}\right)
$$

로, $p = \pm\hbar k = \pm n\pi\hbar/L$인 두 운동량 고유함수 $e^{\pm ikx}$의 중첩이며 각각의 확률은 $\tfrac12$이다.

!!! example "예제 5.8.3 (상자 속의 불확정성)"
    $\langle x\rangle = L/2$, $\langle x^2\rangle = \dfrac{L^2}{3} - \dfrac{L^2}{2\pi^2n^2}$이므로

    $$
    \sigma_x\sigma_p = \frac{\hbar}{2}\sqrt{\frac{\pi^2n^2}{3} - 2} \ \ge\ \frac{\hbar}{2}\sqrt{\frac{\pi^2}{3} - 2} \approx 0.57\hbar > \frac{\hbar}{2} .
    $$

### 중첩과 $|c_n|^2$ { #superpositions-and-c_n2 }

변수분리된 해는 시간에 무관한 방정식을 만족한다. $\frac{1}{\sqrt2}(\psi_1 + \psi_2)$ 같은 결합은 (에너지가 하나가 아니므로) 만족하지 않지만, 시간 인자를 붙이면 전체 슈뢰딩거 방정식을 만족한다. $|c_n|^2$은 에너지를 측정했을 때 $E_n$이 나올 확률이므로 $\sum|c_n|^2 = 1$이고, 정규직교성에 의해

$$
\langle H\rangle = \sum_n |c_n|^2E_n .
$$

!!! example "예제 5.8.4"
    $\Psi = 0.5\psi_1 + c_2\psi_2$이면 $0.25 + |c_2|^2 = 1$이어야 하므로 $|c_2| = \sqrt3/2$.

!!! example "예제 5.8.5 (출렁이는 확률밀도)"
    $\Psi(x,0) = \frac{\sqrt3}{2}\psi_1 + \frac12\psi_2$이면

    $$
    |\Psi(x,t)|^2 = \frac34\psi_1^2 + \frac14\psi_2^2 + \frac{\sqrt3}{2}\psi_1\psi_2\cos\frac{(E_2 - E_1)t}{\hbar} .
    $$

    교차항에서 두 시간 인자가 상쇄되지 않으므로 위치 확률밀도는 각진동수 $(E_2 - E_1)/\hbar$로 진동한다. 각 에너지의 확률 $|c_n|^2$은 변하지 않는다. 나중에 시계를 $t = 0$으로 다시 맞추면 각 $c_n$에 위상이 곱해질 뿐이다.

---

## 5.9 유한 퍼텐셜 우물 { #59-the-finite-potential-well }

<p class="lecture-tag">교과서 §5.9</p>

$|x| < a$에서 $U = 0$, $|x| > a$에서 $U = V_0$이고, 속박 상태는 $0 < E < V_0$이다.

$U$가 대칭이면 $|\psi|^2$도 대칭이어야 하므로 $\psi$를 우함수나 기함수로 잡을 수 있다.

| 영역 | 방정식 | 일반해 | 물리적인 해 |
|---|---|---|---|
| I: $x < -a$ | $\psi'' = \kappa^2\psi$, $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ | $Ce^{\kappa x} + De^{-\kappa x}$ | $Ce^{\kappa x}$ ($x \to -\infty$에서 유한) |
| II: $-a < x < a$ | $\psi'' = -k^2\psi$, $k = \sqrt{2mE}/\hbar$ | $A\cos kx + B\sin kx$ | $A\cos kx$ (우함수) |
| III: $x > a$ | 대칭성 이용 | | $Ce^{-\kappa x}$ |

$x = -a$에서 $\psi$와 $\psi'$의 연속: $Ce^{-\kappa a} = A\cos ka$, $\kappa Ce^{-\kappa a} = kA\sin ka$. 나누면

$$
\tan ka = \frac{\kappa}{k} = \sqrt{\frac{V_0}{E} - 1} .
$$

$z = ka$, $z_0 = a\sqrt{2mV_0}/\hbar$로 두면:

!!! abstract "우함수 속박 상태"
    $$
    \tan z = \sqrt{\left(\frac{z_0}{z}\right)^2 - 1} .
    $$

이것은 초월방정식이라 $z = \cdots$ 꼴의 명시적인 해가 없고, 허용 에너지는 양변의 그래프가 만나는 점으로 구한다.

- **넓고 깊은 우물** ($z_0$가 큼): 교점이 $z = (2n-1)\pi/2$에 다가가고, $E$는 무한 우물의 에너지에 다가간다.
- **좁고 얕은 우물** ($z_0$가 작음): 교점이 적지만 항상 적어도 하나 있다. 속박 상태는 항상 적어도 하나 존재한다.
- **기함수 상태** (안에서 $\psi = B\sin kx$)는 $-\cot z = \sqrt{(z_0/z)^2 - 1}$을 주는데, $z_0 > \pi/2$일 때만 해가 있다. 기함수 속박 상태는 항상 존재하지는 않는다.

---

## 5.10 터널링 { #510-tunnelling }

| | 무한 우물 | 유한 우물 | 퍼텐셜 장벽 |
|---|---|---|---|
| 벽 밖의 $\psi$ | $0$ | $0$이 아님 (감쇠) | $0$이 아님 (뚫고 지나감) |
| 상태의 종류 | 속박 | 속박 / 산란 | 산란 |
| 에너지 | $E_n = n^2\pi^2\hbar^2/2mL^2$ | 양자화, 초월방정식으로 구함 | 연속 |

$U$가 유한한 곳에서는 $\psi$가 벽 너머에서 0이 되지 않는다. 장벽 안에서 지수적으로 감쇠하다가 반대편으로 나올 수 있다. 이것이 터널링이다.

---

## 5.11 조화진동자: 대수적 방법 { #511-the-harmonic-oscillator-algebraic-method }

<p class="lecture-tag">교과서 §5.11</p>

### 교환자 { #commutators }

$[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$. 시험함수에 작용시키면 $[x, \hat p]f = x\frac{\hbar}{i}f' - \frac{\hbar}{i}(xf)' = i\hbar f$이므로

$$
[x, \hat p] = i\hbar, \qquad [\hat p, x] = -i\hbar .
$$

### 사다리 연산자 { #ladder-operators }

$U = \frac12 m\omega^2x^2$이면 $\hat H = \frac{1}{2m}\big[\hat p^2 + (m\omega x)^2\big]$이다. $f^2 + g^2 = (if + g)(-if + g)$를 흉내 내어

$$
\hat a_\pm = \frac{1}{\sqrt{2\hbar m\omega}}\,(\mp i\hat p + m\omega x)
$$

로 정의한다. 그러면 $\hat a_\pm\hat a_\mp = \dfrac{1}{2\hbar m\omega}\big[\hat p^2 + (m\omega x)^2 \mp im\omega[x, \hat p]\big] = \dfrac{\hat H}{\hbar\omega} \pm \dfrac12$이므로

$$
\hat H = \hbar\omega\left(\hat a_\pm\hat a_\mp \mp \frac12\right), \qquad [\hat a_-, \hat a_+] = 1 .
$$

$\hat a_+$와 $\hat a_-$는 서로의 수반연산자이다: $\int f^*(\hat a_\pm g)\,dx = \int(\hat a_\mp f)^*g\,dx$.

!!! abstract "정리 5.11.1"
    $\hat H\psi = E\psi$이면 $\hat H(\hat a_\pm\psi) = (E \pm \hbar\omega)(\hat a_\pm\psi)$이다.

!!! success "증명"
    $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$을 쓰면 $\hat H(\hat a_+\psi) = \hbar\omega(\hat a_+\hat a_- + \tfrac12)\hat a_+\psi = \hbar\omega\,\hat a_+(\hat a_-\hat a_+ + \tfrac12)\psi = \hat a_+\big(\hbar\omega(\hat a_+\hat a_- + 1 + \tfrac12)\psi\big) = \hat a_+(\hat H + \hbar\omega)\psi = (E + \hbar\omega)\hat a_+\psi$이다. $\hat a_-$도 마찬가지이다. $\square$

따라서 사다리 연산자는 고유함수를 (규격화되지는 않은) 다른 고유함수로 바꾼다. 에너지에는 하한이 있으므로 내림을 끝없이 할 수는 없고, $\hat a_-\psi_0 = 0$인 바닥 상태가 있다.

$$
\frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x\right)\psi_0 = 0
\;\Longrightarrow\; \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0
\;\Longrightarrow\; \psi_0 = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar} .
$$

!!! abstract "정리 5.11.2"
    $$
    E_n = \left(n + \frac12\right)\hbar\omega, \qquad
    \hat a_+\hat a_-\psi_n = n\psi_n, \quad \hat a_-\hat a_+\psi_n = (n+1)\psi_n, \qquad
    \psi_n = \frac{1}{\sqrt{n!}}(\hat a_+)^n\psi_0 .
    $$

!!! success "증명"
    $\hat H\psi_0 = \hbar\omega(\hat a_+\hat a_- + \tfrac12)\psi_0 = \tfrac12\hbar\omega\,\psi_0$이고, 올릴 때마다 $\hbar\omega$씩 더해진다. $\hat H = \hbar\omega(\hat a_+\hat a_- + \frac12)$와 $E_n$에서 $\hat a_+\hat a_-\psi_n = n\psi_n$이고, $\hat a_-\hat a_+ = \hat a_+\hat a_- + 1$에서 $n + 1$을 얻는다.

    규격화를 위해 $\hat a_+\psi_n = c_n\psi_{n+1}$로 두면

    $$
    |c_n|^2 = \int(\hat a_+\psi_n)^*(\hat a_+\psi_n)\,dx = \int\psi_n^*\,\hat a_-\hat a_+\psi_n\,dx = n + 1
    $$

    이므로 $c_n = \sqrt{n+1}$이고 $\psi_n = \frac{1}{\sqrt{n!}}(\hat a_+)^n\psi_0$이다. $\square$

!!! example "예제 5.11.3 ($x$, $p$와 비리얼 결과)"
    $\hat a_\pm$의 정의를 더하고 빼면

    $$
    x = \sqrt{\frac{\hbar}{2m\omega}}\,(\hat a_+ + \hat a_-), \qquad
    \hat p = i\sqrt{\frac{\hbar m\omega}{2}}\,(\hat a_+ - \hat a_-) .
    $$

    그러면 $x^2 = \frac{\hbar}{2m\omega}(\hat a_+^2 + \hat a_+\hat a_- + \hat a_-\hat a_+ + \hat a_-^2)$이다. 제곱항은 $n$을 $\pm2$만큼 바꾸므로 직교성에 의해 $\langle\psi_n|\cdot|\psi_n\rangle$에서 사라지고, $\langle x^2\rangle = \frac{\hbar}{2m\omega}(2n+1)$이며

    $$
    \left\langle\tfrac12 m\omega^2x^2\right\rangle = \frac12\left(n + \frac12\right)\hbar\omega = \left\langle\frac{p^2}{2m}\right\rangle .
    $$

    퍼텐셜 에너지와 운동 에너지가 각각 $E_n$의 절반씩을 가진다.

---

## 중간고사에 자주 나오는 것 { #what-the-midterm-tends-to-ask }

2024년과 2025년 중간고사는 이 장에서 다음과 같이 출제했다.

- **고유상태가 아닌 상태의 무한 우물**: $\Psi(x,0) = Ax(L - x)$를 규격화하고($A = \sqrt{30/L^5}$), $\psi_n$으로 전개하여 $P(E_1) = |c_1|^2 = 960/\pi^6 \approx 0.96$을 구하고, $\langle H\rangle = \sum|c_n|^2E_n = 5\hbar^2/mL^2$을 계산한다. $Ax(L-x)$의 모양이 $\psi_1$과 비슷하기 때문에 $E_1$이 거의 전부를 차지한다.
- **시간 변화**: $c\psi_1 + \frac{\sqrt2}{2}\psi_2$에서 $c$, $\Psi(x,t)$, 실수로 쓴 확률밀도, 그 진동의 주기 $2\pi\hbar/(E_2 - E_1)$을 구한다(예제 5.8.5).
- **조화진동자**: 규격화된 $\psi_0$, $\hat a_-\hat a_+$와 $\hat a_+\hat a_-$의 고윳값, $\hat a_\pm$로 쓴 $x$와 $\hat p$, $\langle V\rangle$와 $\langle T\rangle$(§5.11).
- **해석**: 슈뢰딩거 방정식이 공리인 이유, $|c_n|^2$의 의미, 변수분리된 해의 에너지가 확정된 이유.
