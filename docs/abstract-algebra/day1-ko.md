---
title: "1일차 — 유한체 (11월 25일)"
---

<div class="lang-switch"><a href="../day1/">English</a><a class="on">한국어</a></div>

<div class="running-head"><span>현대대수 특강</span><span>1일차 · 유한체</span></div>

# 1일차 — 유한체 { .part-title #day-1-finite-fields }

<p class="source-note">특강, 2026년 11월 25일 · Serre 1장 · <a class="pdf-link" href="notes.pdf" download="현대대수-특강-1일차.pdf">이 날을 PDF로 보기</a></p>

**이 날에는.** 유한체를 다룬다. 프로베니우스 사상, 체 $\mathbb F_q$의 존재와 유일성, 그 곱셈군이 순환군이라는 사실을 본다. 이어서 $\mathbb F_q$의 제곱수, 르장드르 기호, 그리고 이차 상호 법칙에 대한 가우스의 증명을 가우스 합에 관한 첫 번째 보조정리까지 다룬다. 강의에서는 §2(유한체 위의 방정식)를 건너뛰었다. 번호가 Serre와 맞도록 제목은 남겨 두었다.

!!! quote "이 날에 쓰는 규약."
    - 모든 체는 가환이다.
    - 체 $K$에 대해 $1 \mapsto 1$로 보내는 사상 $\mathbb Z \to K$의 상은 정역이므로 $\mathbb Z$ 또는 어떤 소수 $p$에 대한 $\mathbb Z/p\mathbb Z$와 동형이다. 그 분수체는 $\mathbb Q$ 또는 $\mathbb Z/p\mathbb Z = \mathbb F_p$와 동형이다. 첫째 경우 $\operatorname{char} K = 0$, 둘째 경우 $\operatorname{char} K = p$라고 한다.
    - $\operatorname{char} K = p \neq 0$이면, $p$는 $n \cdot 1 = 0$을 만족하는 가장 작은 정수 $n > 0$이다.
    - $K^*$는 $K$의 0이 아닌 원소들이 이루는 곱셈군이다.
    - $p$는 언제나 소수, $q = p^f$는 그 거듭제곱이다.

---

## 1 유한체 { #1-finite-fields }

### 1.1 유한체 { #11-finite-fields }

!!! abstract "보조정리 (프로베니우스 사상)"
    $\operatorname{char} K = p$이면, $\sigma\colon K \to K$, $x \mapsto x^p$는 단사 준동형사상이고 그 상은 $K^p = \{x^p \mid x \in K\}$이다.

!!! success "증명"
    $K$가 가환이므로 $\sigma(xy) = (xy)^p = x^p y^p = \sigma(x)\sigma(y)$이다. 이항정리에 의해

    $$
    \sigma(x + y) = (x + y)^p = x^p + \binom{p}{1}x^{p-1}y + \cdots + \binom{p}{p-1}xy^{p-1} + y^p = x^p + y^p = \sigma(x) + \sigma(y)
    $$

    이다. $0 < k < p$이면 $p \mid \binom{p}{k}$이기 때문이다. 마지막으로 $\sigma(x) = 0$이면 $x^p = 0$이다. $x \neq 0$이라면 양변에 $(x^{-1})^p$를 곱해 $1 = 0$을 얻으므로 $x = 0$이다. 따라서 $\ker\sigma = \{0\}$이고 $\sigma$는 단사이다. $\square$

!!! info "비고"
    $K$가 유한체이거나 대수적으로 닫힌 체이면 $\sigma$는 $K$의 자기동형사상이다. $K$가 유한이면 단사 사상 $K \to K$는 전사이다. $K$가 대수적으로 닫혀 있으면 임의의 $y \in K$에 대해 방정식 $X^p - y = 0$이 $K$ 안에 근 $z$를 가지므로 $z^p = y$, 즉 $y$는 상에 들어 있다.

!!! abstract "정리 1"
    i) $K$가 유한체이면 $\operatorname{char} K = p \neq 0$이고 $|K| = p^f$이다. 여기서 $f = [K : \mathbb F_p]$이다.

    ii) $p$가 소수, $q = p^f$이고 $\Omega$가 표수 $p$인 대수적으로 닫힌 체라 하자. $\Omega$의 부분체 중 원소가 $q$개인 것 $\mathbb F_q$가 유일하게 존재하며, $\mathbb F_q = \{x \in \Omega \mid x^q - x = 0\}$이다.

    iii) 원소가 $q = p^f$개인 유한체는 모두 $\mathbb F_q$와 동형이다.

!!! success "i)의 증명"
    유한체는 $\mathbb Q$를 포함할 수 없으므로 표수는 소수 $p$이고 $\mathbb F_p$를 포함한다. 그러면 $K$는 $\mathbb F_p$ 위의 $f = [K : \mathbb F_p]$차원 벡터공간이므로 $|K| = p^f$이다. $\square$

!!! success "ii)의 증명"
    $\Omega$가 대수적으로 닫혀 있고 $\operatorname{char}\Omega = p$, $q = p^f$라 하자.

    $$
    \mathbb F_q = \{x \in \Omega \mid x^q - x = 0\}
    $$

    로 놓는다. 다항식 $X^q - X$의 도함수는 $qX^{q-1} - 1 = -1 \neq 0$이므로 중근이 없고, $\Omega$가 대수적으로 닫혀 있으므로 근이 정확히 $q$개 있다. 즉 $|\mathbb F_q| = q$이다. 사상 $\sigma\colon \Omega \to \Omega$, $x \mapsto x^q$는 (프로베니우스 사상의 거듭제곱이므로) 자기동형사상이고, $\mathbb F_q$는 그 고정점의 집합이므로 부분체이다.

    유일성을 보이자. $K$가 원소 $q$개인 $\Omega$의 부분체이면 $K^*$는 원소가 $q - 1$개인 군이므로 모든 $x \in K^*$에 대해 $x^{q-1} = 1$이고, 따라서 모든 $x \in K$에 대해 $x^q = x$이다. 그러므로 $K \subseteq \mathbb F_q$이고, 둘 다 원소가 $q$개이므로 $K = \mathbb F_q$이다. $\square$

*iii)의 증명.* 강의에서 생략했다.

!!! info "비고"
    ii)의 유일성은 고정된 대수적으로 닫힌 체 $\Omega$ 안에서의 유일성이다. iii)의 유일성은 동형을 제외한 유일성이다.

### 1.2 유한체의 곱셈군 { #12-the-multiplicative-group-of-a-finite-field }

!!! abstract "정리 2"
    소수 $p$와 $q = p^f$에 대해, $\mathbb F_q$의 곱셈군 $\mathbb F_q^*$는 위수 $q - 1$인 순환군이다.

이 정리는 다음 군론의 보조정리에 기댄다.

!!! abstract "보조정리 2"
    $H$가 위수 $n$인 유한군이라 하자. $n$의 모든 약수 $d$에 대해 집합 $\{x \in H \mid x^d = 1\}$의 원소가 많아야 $d$개이면, $H$는 순환군이다.

!!! success "정리 2의 증명"
    $H = \mathbb F_q^*$, $n = q - 1$로 놓는다. $n$의 각 약수 $d$에 대해 방정식 $x^d = 1$은 체 $\mathbb F_q$ 위의 $d$차 다항식 방정식이므로 해가 많아야 $d$개이다. 보조정리 2에 의해 $H$는 순환군이다. $\square$

!!! info "비고"
    이 증명은 체의 곱셈군의 유한 부분군이 모두 순환군임을 보여 준다.

보조정리 2를 증명하려면 다음 보조정리가 필요하다.

!!! abstract "보조정리 1"
    정수 $n \geq 1$에 대해 $n = \sum_{d \mid n} \phi(d)$이다. 여기서 $\phi$는 오일러 $\phi$ 함수이다.

!!! success "보조정리 1의 증명"
    각 $d \mid n$에 대해 $C_d$를 $\mathbb Z/n\mathbb Z$의 위수 $d$인 유일한 부분군이라 하고, $\Phi_d$를 $C_d$의 생성원들의 집합이라 하자. 그러면 $|\Phi_d| = \phi(d)$이다. $\mathbb Z/n\mathbb Z$의 각 원소는 $C_d$ 중 정확히 하나, 곧 자신이 생성하는 부분군의 생성원이므로

    $$
    \mathbb Z/n\mathbb Z = \bigsqcup_{d \mid n} \Phi_d,
    \qquad
    n = |\mathbb Z/n\mathbb Z| = \Big|\bigsqcup_{d \mid n}\Phi_d\Big| = \sum_{d \mid n}\phi(d). \qquad \square
    $$

!!! example "예제 ($n = 12$)"
    $\mathbb Z/12\mathbb Z$에서:

    | $d$ | $C_d$ | $\Phi_d$ | $\phi(d)$ |
    |---|---|---|---|
    | 1 | $\{0\}$ | $\{0\}$ | 1 |
    | 2 | $\{0, 6\}$ | $\{6\}$ | 1 |
    | 3 | $\{0, 4, 8\}$ | $\{4, 8\}$ | 2 |
    | 4 | $\{0, 3, 6, 9\}$ | $\{3, 9\}$ | 2 |
    | 6 | $\{0, 2, 4, 6, 8, 10\}$ | $\{2, 10\}$ | 2 |
    | 12 | $\mathbb Z/12\mathbb Z$ | $\{1, 5, 7, 11\}$ | 4 |

    실제로 $1 + 1 + 2 + 2 + 2 + 4 = 12$이다.

!!! success "보조정리 2의 증명"
    $d \mid n$이라 하자. $H$가 위수 $d$인 원소 $z$를 가지면 $\langle z\rangle = \{1, z, \dots, z^{d-1}\}$는 위수 $d$인 순환군이고 $\langle z\rangle \subseteq \{x \in H \mid x^d = 1\}$이다. 가정에 의해 오른쪽 집합의 원소는 많아야 $d$개이므로 두 집합은 같다. 즉 $y^d = 1$인 $y \in H$는 모두 $\langle z\rangle$에 속한다. 특히 위수 $d$인 원소는 모두 $\langle z\rangle$의 생성원이고, 그런 것은 정확히 $\phi(d)$개이다.

    따라서 $H$에서 위수 $d$인 원소의 개수는 $0$ 또는 $\phi(d)$이다. $H$의 모든 원소는 $n$의 어떤 약수 $d$를 위수로 가지므로 이 개수들을 모두 더하면 $n$이다. 어느 하나라도 $0$이면 그 합은 $\sum_{d\mid n}\phi(d) = n$(보조정리 1)보다 작아져 모순이다. 그러므로 모든 $d \mid n$에 대해 $H$에는 위수 $d$인 원소가 정확히 $\phi(d)$개 있다. 특히 위수 $n$인 원소가 $\phi(n) \geq 1$개 있으므로 $H$는 순환군이다. $\square$

---

## 2 유한체 위의 방정식 { #2-equations-over-a-finite-field }

### 2.1 거듭제곱의 합 { #21-power-sums }

<div class="admonition skipped" markdown>
이 절은 강의에서 다루지 않았으므로 이 노트에서도 건너뛴다. $u \geq 1$이 $q - 1$로 나누어떨어지면 $\sum_{x \in K} x^u = -1$, 그렇지 않으면 $0$임을 보이는 절이다. 1일차의 뒷부분은 이 절에 기대지 않는다.
</div>

### 2.2 슈발레 정리 { #22-chevalleys-theorem }

<div class="admonition skipped" markdown>
이 절은 강의에서 다루지 않았으므로 이 노트에서도 건너뛴다. 슈발레–워닝 정리($\sum \deg f_\alpha < n$인 다항식들의 공통근의 개수는 $p$로 나누어떨어진다)와 이차형식에 관한 그 따름정리들이 들어 있다. 1일차의 뒷부분은 이 절에 기대지 않는다.
</div>

---

## 3 이차 상호 법칙 { #3-quadratic-reciprocity-law }

### 3.1 유한체의 제곱수 { #31-squares-in-finite-fields }

$q = p^f$라 하자. $\mathbb F_q^*$는 위수 $q - 1$인 순환군이므로 모든 $x \in \mathbb F_q^*$에 대해 $x^{q-1} = 1$임을 떠올리자.

!!! abstract "정리 4"
    (a) $p = 2$이면 $\mathbb F_q$의 모든 원소는 제곱수이다.

    (b) $p \neq 2$이면 제곱수들 $\mathbb F_q^{*2} = \{x^2 \mid x \in \mathbb F_q^*\}$는 $\mathbb F_q^*$에서 지표 $2$인 부분군을 이루며, 이는 $\{\pm 1\}$에 값을 갖는 준동형사상 $x \mapsto x^{(q-1)/2}$의 핵이다. 요약하면 수열

    $$
    1 \longrightarrow \mathbb F_q^{*2} \longrightarrow \mathbb F_q^* \longrightarrow \{\pm 1\} \longrightarrow 1
    $$

    은 완전열이다. 즉 각 자리에서 나가는 사상의 핵이 들어오는 사상의 상과 같다.

!!! success "(a)의 증명"
    $p = 2$이면 사상 $x \mapsto x^2$는 프로베니우스 사상이고, 유한체 $\mathbb F_q$의 자기동형사상이다. 특히 전사이다. $\square$

!!! success "(b)의 증명"
    $p \neq 2$이고 $\Omega$를 $\mathbb F_q$의 대수적 폐포라 하자. $x \in \mathbb F_q^*$에 대해 $y^2 = x$인 $y \in \Omega$를 고르면

    $$
    y^{q-1} = x^{(q-1)/2} = \pm 1, \qquad \big(x^{(q-1)/2}\big)^2 = x^{q-1} = 1\text{이므로}
    $$

    이다. 따라서 $x$가 $\mathbb F_q$에서 제곱수일 필요충분조건은 $y \in \mathbb F_q^*$인 것이고, 이는 $y^{q-1} = 1$인 것과 동치이다(정리 1 ii)에 의해 $\mathbb F_q^*$는 정확히 $y^{q-1} = 1$인 $y \in \Omega$들의 집합이다). 그러므로 $\mathbb F_q^{*2}$는 $\{\pm 1\}$에 값을 갖는 사상 $x \mapsto x^{(q-1)/2}$의 핵이다.

    제곱 사상 $\mathbb F_q^* \to \mathbb F_q^*$의 핵은 $\{\pm 1\}$이고, $p \neq 2$이므로 원소가 두 개이다. 따라서 그 상 $\mathbb F_q^{*2}$는 원소가 $(q-1)/2$개이고 지표는 $2$이다. 특히 사상 $x \mapsto x^{(q-1)/2}$는 $\{\pm 1\}$ 위로의 전사이다. $\square$

### 3.2 르장드르 기호 { #32-legendre-symbol }

!!! note "정의 (르장드르 기호)"
    소수 $p \neq 2$와 $x \in \mathbb F_p^*$에 대해 **르장드르 기호**는

    $$
    \left(\frac{x}{p}\right) = x^{(p-1)/2} \in \{\pm 1\}
    $$

    이다.

!!! info "비고"
    - 관례로 $\left(\frac{0}{p}\right) = 0$으로 두어 기호를 $\mathbb F_p$ 전체로 확장한다.
    - $x \in \mathbb Z$의 $\mathbb F_p$에서의 상이 $x'$이면 $\left(\frac{x}{p}\right) = \left(\frac{x'}{p}\right)$로 정의한다. 그러면 $\left(\frac{x}{p}\right)\left(\frac{y}{p}\right) = \left(\frac{xy}{p}\right)$가 성립한다.
    - $\left(\frac{x}{p}\right) = 1$은 $x \in \mathbb F_p^{*2}$와 동치이다(정리 4).
    - $x \in \mathbb F_p^*$이고 $y \in \Omega$가 $x$의 제곱근이면 $\left(\frac{x}{p}\right) = y^{p-1}$이다.

    정리하면

    $$
    \left(\frac{x}{p}\right) =
    \begin{cases}
    0 & x \equiv 0 \pmod p,\\
    1 & \text{어떤 } y \not\equiv 0\text{에 대해 } x \equiv y^2 \pmod p,\\
    -1 & \text{그 밖의 경우.}
    \end{cases}
    $$

$n$이 홀수일 때 $\mathbb Z/2\mathbb Z$의 원소 $\varepsilon(n)$, $\omega(n)$을 다음과 같이 정의한다.

$$
\varepsilon(n) \equiv \frac{n-1}{2} \pmod 2 =
\begin{cases} 0 & n \equiv 1 \pmod 4,\\ 1 & n \equiv -1 \pmod 4,\end{cases}
\qquad
\omega(n) \equiv \frac{n^2-1}{8} \pmod 2 =
\begin{cases} 0 & n \equiv \pm 1 \pmod 8,\\ 1 & n \equiv \pm 5 \pmod 8.\end{cases}
$$

$\varepsilon\colon (\mathbb Z/4\mathbb Z)^* \to \mathbb Z/2\mathbb Z$와 $\omega\colon (\mathbb Z/8\mathbb Z)^* \to \mathbb Z/2\mathbb Z$는 준동형사상이다.

!!! abstract "정리 5"
    i) $\left(\frac{1}{p}\right) = 1$.

    ii) $\left(\frac{-1}{p}\right) = (-1)^{\varepsilon(p)}$.

    iii) $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$.

!!! info "비고"
    정리 5는 다음과 같이 말할 수도 있다.

    - $-1$이 법 $p$에 대한 제곱수일 필요충분조건은 $p \equiv 1 \pmod 4$이다.
    - $2$가 법 $p$에 대한 제곱수일 필요충분조건은 $p \equiv \pm 1 \pmod 8$이다.

i)과 ii)는 정의에서 바로 나온다: $1^{(p-1)/2} = 1$, $(-1)^{(p-1)/2} = (-1)^{\varepsilon(p)}$. iii)만 증명한다. (이 증명은 2일차에 다루었다.)

!!! success "iii)의 증명"
    $\alpha \in \Omega$를 1의 원시 $8$제곱근이라 하고 $y = \alpha + \alpha^{-1}$로 두자. $\alpha^4 = -1$이므로 $\alpha^2 + \alpha^{-2} = \alpha^{-2}(\alpha^4 + 1) = 0$이고, 따라서

    $$
    y^2 = \alpha^2 + \alpha^{-2} + 2 = 2
    $$

    이다. 즉 $y$는 $2$의 제곱근이므로 위의 비고에 의해 $\left(\frac{2}{p}\right) = y^{p-1}$이다. 프로베니우스 사상에 의해 $y^p = \alpha^p + \alpha^{-p}$이고, $\alpha^p$는 $p$를 $8$로 나눈 나머지에만 의존한다.

    $p \equiv \pm 1 \pmod 8$이면 $\alpha^p = \alpha^{\pm 1}$이므로 $y^p = \alpha + \alpha^{-1} = y$이다. $y^2 = 2$이므로 $y \neq 0$이고, $y^{p-1} = 1$, 즉 $\left(\frac{2}{p}\right) = 1$이다.

    $p \equiv \pm 5 \pmod 8$이면 $\alpha^p = \alpha^{\pm 5}$이므로 $\alpha^4 = -1$을 쓰면

    $$
    y^p = \alpha^5 + \alpha^{-5} = -(\alpha + \alpha^{-1}) = -y
    $$

    이고, $\left(\frac{2}{p}\right) = y^{p-1} = -1$이다. 두 경우 모두 $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$이다. $\square$

### 3.3 이차 상호 법칙 { #33-quadratic-reciprocity-law }

!!! abstract "정리 6 (가우스, 이차 상호 법칙)"
    $\ell$과 $p$가 $2$가 아닌 서로 다른 두 소수이면

    $$
    \left(\frac{\ell}{p}\right) = \left(\frac{p}{\ell}\right)(-1)^{\varepsilon(\ell)\varepsilon(p)}
    $$

    이다.

여기서 $\left(\frac{\ell}{p}\right)$은 법 $p$로, $\left(\frac{p}{\ell}\right)$은 법 $\ell$로 계산한다.

$\Omega$를 $\mathbb F_p$의 대수적 폐포라 하고, $w \in \Omega$를 1의 원시 $\ell$제곱근이라 하자. $w^\ell = 1$이므로 $x \in \mathbb F_\ell$에 대해 $w^x$가 잘 정의된다. **가우스 합**을 다음과 같이 만든다.

$$
y = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^x \in \Omega .
$$

Serre는 이 합에 관한 보조정리 두 개를 증명한다. 1일차는 첫 번째에서 끝났다.

!!! abstract "보조정리 1"
    $y^2 = (-1)^{\varepsilon(\ell)}\,\ell$이다. (기호를 남용하여 $\ell$은 체 $\mathbb F_p$에서의 $\ell$의 상도 나타낸다.)

!!! success "증명"
    제곱을 전개하고 $u = x + z$, $t = z$로 놓으면

    $$
    y^2 = \sum_{x, z \in \mathbb F_\ell}\left(\frac{xz}{\ell}\right)w^{x+z} = \sum_{u, t \in \mathbb F_\ell}\left(\frac{t(u-t)}{\ell}\right)w^u
    $$

    이다. $t = 0$인 항은 0이다. $t \neq 0$이면 $t(u - t) = (-1)\,t^2\,(1 - ut^{-1})$이고, 기호는 곱셈적이며 $\left(\frac{t^2}{\ell}\right) = 1$이므로

    $$
    y^2 = \sum_{u \in \mathbb F_\ell,\ t \in \mathbb F_\ell^*}\left(\frac{-1}{\ell}\right)\left(\frac{t^2}{\ell}\right)\left(\frac{1 - ut^{-1}}{\ell}\right)w^u
    = (-1)^{\varepsilon(\ell)}\sum_{u \in \mathbb F_\ell,\ t \in \mathbb F_\ell^*}\left(\frac{1 - ut^{-1}}{\ell}\right)w^u
    $$

    이다(정리 5 ii)). 따라서

    $$
    (-1)^{\varepsilon(\ell)}y^2 = \sum_{u \in \mathbb F_\ell} C_u\,w^u, \qquad C_u = \sum_{t \in \mathbb F_\ell^*}\left(\frac{1 - ut^{-1}}{\ell}\right).
    $$

    $u = 0$이면 모든 항이 $\left(\frac{1}{\ell}\right) = 1$이므로 $C_0 = \ell - 1$이다. $u \neq 0$이면 $t$가 $\mathbb F_\ell^*$를 돌 때 $s = 1 - ut^{-1}$은 $\mathbb F_\ell - \{1\}$을 돌므로

    $$
    C_u = \sum_{s \in \mathbb F_\ell - \{1\}}\left(\frac{s}{\ell}\right) = \sum_{s \in \mathbb F_\ell^*}\left(\frac{s}{\ell}\right) - \left(\frac{1}{\ell}\right) = 0 - 1 = -1
    $$

    이다. $\mathbb F_\ell^*$에는 제곱수와 제곱수가 아닌 수가 같은 개수만큼 있기 때문이다(정리 4). 그러므로

    $$
    (-1)^{\varepsilon(\ell)}y^2 = (\ell - 1) - \sum_{u \in \mathbb F_\ell^*}w^u = \ell
    $$

    이다. $w$가 1의 원시 $\ell$제곱근이므로 $\sum_{u \in \mathbb F_\ell}w^u = \frac{w^\ell - 1}{w - 1} = 0$이고, 따라서 $\sum_{u \in \mathbb F_\ell^*}w^u = -1$이기 때문이다. $\square$

두 번째 보조정리와 증명의 나머지는 [2일차](day2-ko.md#33-quadratic-reciprocity-law-continued)에 있다.
