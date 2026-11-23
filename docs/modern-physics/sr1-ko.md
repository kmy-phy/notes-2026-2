---
title: "2부 — 특수상대론 I (중간고사 범위)"
---

<div class="lang-switch"><a href="../sr1/">English</a><a class="on">한국어</a></div>

<div class="running-head"><span>현대물리학</span><span>2부 · 상대론 I</span></div>

# 2부 — 특수상대론 I { .part-title #part-ii-special-relativity-i }

<p class="source-note">수업 필기, 중간고사 범위 · <a class="pdf-link" href="notes.pdf" download="현대물리학-상대론-I.pdf">이 부를 PDF로 내려받기</a></p>

**이 부에서는.** 로렌츠 변환은 허수 각을 가진 시공간의 회전이다. 여기서 동시성의 상대성과 인과율이 정하는 그 한계, 쌍둥이 역설, 그리고 크기의 제곱이 모든 좌표계에서 같은 4-벡터가 나오며, 4-벡터를 쓰면 충돌 문제를 에너지–운동량 보존으로 쉽게 풀 수 있다. 6–11절은 [특수상대론 II](../sr2-ko/)에서 이어진다.

!!! quote "이 부에서 쓰는 규약."
    - $S$는 실험실 좌표계이다. 프라임 붙은 좌표계 $S'$는 $S$에 대해 $x$ 방향으로 속도 $v$로 움직인다. $\beta = v/c$.
    - $\gamma(v) = \gamma_v = \dfrac{1}{\sqrt{1 - v^2/c^2}}$.
    - $L_0$는 고유 길이(정지 상태에서 잰 길이)이다. $\lambda$는 선전하밀도이고 $\lambda_0$는 실험실에서의 값이다. $I = \lambda v$.
    - $\hat n$은 바깥 방향 단위법선, $d\tau$는 부피요소이다.

---

## 1 회전으로서의 로렌츠 변환 { #1-the-lorentz-transformation-as-a-rotation }

축을 $\theta$만큼 회전하면 $(x, y)$는

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}
$$

로 바뀐다. 둘째 좌표를 허수 시간 $y \to ict$로 바꾸자. 속도 $v$로 움직이는 좌표계 $S'$의 $ct'$축은 $x = vt$를 따라 놓이며, 회전 그림에서는 $\tan\theta' = -x/(ict)$, 즉

$$
\theta' = \tan^{-1}\!\left(i\frac{v}{c}\right) = i\tanh^{-1}\beta \equiv i\phi
$$

이다.

!!! info "참고 — 쌍곡선 함수"
    $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$에서

    $$
    \cos(i\phi) = \cosh\phi, \qquad \sin(i\phi) = i\sinh\phi, \qquad \cosh^2\phi - \sinh^2\phi = 1
    $$

    이고, $\tan^{-1}x = \frac{1}{2i}\ln\frac{1+ix}{1-ix}$, $\tanh^{-1}x = \frac12\ln\frac{1+x}{1-x}$이므로 $\tan^{-1}(ix) = i\tanh^{-1}x$이다.

$\beta = \tanh\phi$이면 $\cosh^2\phi = \dfrac{1}{1-\beta^2} = \gamma^2$이므로 $\cosh\phi = \gamma$, $\sinh\phi = \gamma\beta$이다. 회전은

$$
\begin{pmatrix} x' \\ ict' \end{pmatrix} = \begin{pmatrix} \cosh\phi & i\sinh\phi \\ -i\sinh\phi & \cosh\phi \end{pmatrix}\begin{pmatrix} x \\ ict \end{pmatrix}
= \begin{pmatrix} \gamma & i\gamma\beta \\ -i\gamma\beta & \gamma \end{pmatrix}\begin{pmatrix} x \\ ict \end{pmatrix}
$$

이 된다.

!!! abstract "로렌츠 변환"
    $$
    x' = \gamma(x - vt), \qquad t' = \gamma\left(t - \frac{v}{c^2}x\right).
    $$

매개변수 $\phi$를 **급속도(rapidity)**라 한다. 회전은 $x^2 + y^2$를 보존하고, $y = ict$이면 보존되는 양은 $x^2 - c^2t^2$이다.

---

## 2 인과율과 시공간 도표 { #2-causality-and-spacetime-diagrams }

$S$에서 한 사건(예: 신호를 보냄)이 $(x_1, t_1)$에서, 다른 사건이 $(x_2, t_2)$에서 일어났다고 하자. $S'$에서는

$$
\Delta t' = \frac{\Delta t - \frac{v}{c^2}\Delta x}{\sqrt{1 - v^2/c^2}} .
$$

$\Delta t < \frac{v}{c^2}\Delta x$, 즉 $\dfrac{c\Delta t}{\Delta x} < \dfrac{v}{c} < 1$이면 사건의 순서가 뒤바뀐다($\Delta t > 0$인데 $\Delta t' < 0$). 이를 위해서는 $c\Delta t < \Delta x$여야 한다.

- 두 사건이 인과관계로 연결되어 있으면(빛보다 빠르지 않은 신호가 한쪽에서 다른 쪽으로 갈 수 있으면) $c\Delta t \ge \Delta x$이고, 순서는 모든 좌표계에서 같다.
- 그렇지 않으면 $c\Delta t < \Delta x$일 수 있고, 좌표계에 따라 어느 쪽이 먼저인지가 달라질 수 있다.

시공간 도표($x$ 가로, $ct$ 세로)에서 직선 $x = \pm ct$는 **광원뿔**을 이룬다. 원점에 대해 광원뿔 안의 사건은 **시간꼴** 간격으로 인과관계가 있을 수 있고, 밖의 사건은 **공간꼴** 간격이다. $S'$의 축은 $ct'$축 $x = vt$와 $x'$축 $ct = \beta x$로, 빛의 선을 향해 대칭으로 기운다. $x'$축과 평행한 직선이 $S'$의 동시선이다.

!!! info "참고 — 동시성은 절대적이지 않다"
    $S'$의 동시선 위의 두 사건은 $S'$에서는 동시이지만 $S$에서는 아니다. 아래의 모든 역설은 결국 이것으로 귀결된다.

---

## 3 쌍둥이 역설 { #3-the-twin-paradox }

쌍둥이 한 명이 $v = 0.6c$로 $6$광년 떨어진 별까지 갔다가 돌아온다. $\gamma = 1/0.8 = 1.25$이다.

- **지구 좌표계 $S$.** 편도마다 $6/0.6 = 10$년 걸린다. 여행자는 사건 $(x, ct) = (6, 10)$에서 방향을 바꾸고 $ct = 20$에 돌아온다.
- **여행자.** 편도마다 거리가 $6 \times 0.8 = 4.8$광년으로 수축하고, $4.8/0.6 = 8$년 걸린다. 왕복은 $16$년이다.

여행자가 $4$년 더 젊다. 상황은 대칭이 아니다. 여행자는 반환점에서 관성계를 바꾼다.

**가는 좌표계 $S'$에서 본 모습.** $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$를 쓰면 반환점 $S(6, 10)$은 $S'(0, 8)$이다. 이 점을 지나는 동시선은 지구의 세계선과 $ct = 6.4$에서 만난다. 방향을 바꾸기 직전 여행자는 지구의 시계가 $6.4$년이라고 말한다. 방향을 바꾼 직후, 오는 좌표계에서 같은 사건을 지나는 동시선은 지구의 세계선과 $ct = 13.6$에서 만난다. 반환하는 동안 여행자가 생각하는 "지구의 지금"이 $7.2$년 건너뛰고, $6.4 + 7.2 + 6.4 = 20$이다.

---

## 4 4-벡터 { #4-four-vectors }

물리량은 **공변**(로렌츠 변환으로 바뀌는 것, $(ct, x)$처럼)이거나 **불변**(모든 좌표계에서 같은 것)이다. 불변량의 예: 고유시간 $\tau$, 고유 길이 $L_0$, 정지질량 $m$, 전하 $q$.

고유시간이 핵심 불변량이다. 두 시계 $A$, $B$가 각각 자기의 $\tau$를 재면 각 좌표계의 시간은 $t_A = \gamma_A\tau$, $t_B = \gamma_B\tau$이고, 모든 좌표계가 $\tau$에 동의한다.

!!! note "정의 4.1 (위치 4-벡터)"
    $\mathbb{X} = (ct, x, y, z) = (x_0, x_1, x_2, x_3)$이고, 불변인 크기의 제곱은

    $$
    |\mathbb{X}|^2 = x_0^2 - (x_1^2 + x_2^2 + x_3^2) .
    $$

!!! abstract "명제 4.2"
    두 사건에 대해 $|\Delta\mathbb X|^2 = (\Delta x_0)^2 - (\Delta x_1)^2$은 $S$와 $S'$에서 같다.

!!! success "증명"
    $$
    (\Delta x_0')^2 - (\Delta x_1')^2 = \gamma^2\big[(\Delta x_0 - \beta\Delta x_1)^2 - (\Delta x_1 - \beta\Delta x_0)^2\big]
    = \gamma^2\big[(\Delta x_0)^2(1 - \beta^2) - (\Delta x_1)^2(1 - \beta^2)\big] = (\Delta x_0)^2 - (\Delta x_1)^2 . \;\square
    $$

$\Delta\mathbb X$를 불변량 $\Delta\tau$로 나누면 새로운 4-벡터를 얻는다.

!!! note "정의 4.3 (4-속도, 4-운동량)"
    $$
    \mathbb V = \frac{d\mathbb X}{d\tau} = (\gamma c, \gamma\vec v), \quad |\mathbb V|^2 = \gamma^2c^2(1 - \beta^2) = c^2;
    \qquad
    \mathbb P = m\mathbb V = (\gamma mc, \gamma m\vec v) = \left(\frac{E}{c}, \vec p\right).
    $$

    (여기서 $\frac{dx_1}{d\tau} = \frac{dx_1}{dt}\frac{dt}{d\tau} = v\gamma$이다.)

$v \ll c$이면 $P_0 = mc(1 - v^2/c^2)^{-1/2} = mc + \frac12 mv^2/c + \cdots$이므로 $cP_0 = mc^2 + \frac12 mv^2 + \cdots = E$이다. 시간 성분은 정지 에너지 $mc^2$를 포함한 에너지를 $c$로 나눈 것이다.

!!! abstract "에너지–운동량 관계"
    $|\mathbb P|^2 = \dfrac{E^2}{c^2} - p^2 = m^2c^2$이므로

    $$
    E^2 = (pc)^2 + (mc^2)^2 .
    $$

빛은 $m = 0$, $v = c$라서 $\gamma m v$가 $0\cdot\infty$ 꼴이다. 그래서 광자의 4-운동량을 직접 $\mathbb K = (E/c, \vec p)$, $|\mathbb K|^2 = 0$, 즉 $E = pc$로 정의한다. $E = hf = \hbar\omega$, $p = h/\lambda = \hbar k$를 쓰면

$$
\mathbb K = \left(\frac{\hbar\omega}{c}, \hbar\vec k\right), \qquad \omega = ck .
$$

---

## 5 4-운동량을 이용한 충돌 { #5-collisions-with-four-momentum }

충돌에서 4-운동량은 보존되고 $|\mathbb P|^2$은 불변이다. 보존 법칙을 제곱하고, 불변량을 가장 편한 좌표계에서 계산하는 것이 핵심 기법이다.

!!! example "예제 5.1 (입자에 흡수되는 광자)"
    에너지 $\hbar\omega$인 광자가 정지한 질량 $m$인 입자에 부딪혀 흡수되고, 질량 $M$인 입자 하나가 남는다.

    $$
    \mathbb K + \mathbb P = \mathbb P_f, \qquad \mathbb K = \left(\tfrac{\hbar\omega}{c}, \hbar k\right),\ \mathbb P = (mc, 0).
    $$

    제곱하면 $|\mathbb K|^2 + |\mathbb P|^2 + 2\mathbb K\cdot\mathbb P = |\mathbb P_f|^2$이고, $|\mathbb K|^2 = 0$, $|\mathbb P|^2 = m^2c^2$, $|\mathbb P_f|^2 = M^2c^2$, $\mathbb K\cdot\mathbb P = \hbar\omega m$이므로

    $$
    2\hbar\omega m = (M^2 - m^2)c^2 .
    $$

!!! example "예제 5.2 (반양성자 생성 문턱)"
    양성자를 가속해 정지한 양성자에 충돌시켜 양성자 3개와 반양성자 1개를 만든다: $p + p \to p + p + p + \bar p$. 들어오는 양성자의 최소 에너지 $E$는?

    문턱에서는 생성물 네 개가 같은 속도로 움직이므로, 운동량 중심 좌표계에서 $\mathbb P_f' = (4mc, \vec 0)$, $|\mathbb P_f|^2 = 16m^2c^2$이다. $\mathbb P_1 = (E/c, \vec p)$, $\mathbb P_2 = (mc, \vec 0)$이면

    $$
    |\mathbb P_1 + \mathbb P_2|^2 = m^2c^2 + m^2c^2 + 2mE = 16m^2c^2 \;\Longrightarrow\; E = 7mc^2 .
    $$

    필요한 운동 에너지는 $6mc^2$로, 새로 생기는 입자 쌍의 정지 에너지의 세 배이다.
